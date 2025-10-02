from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post, Category, Comment


def home(request):
    # Query all posts from the database, newest first
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})


def post_detail(request, post_id):
    # Get a single post by id or return 404 if not found
    post = get_object_or_404(Post, pk=post_id)
    # Also get all comments related to this post
    comments = post.comments.all().order_by('created_at')

    if request.method == "POST":
        # Extract author and comment content from form submission
        author = request.POST.get('author')
        content = request.POST.get('content')
        if author and content:
            # Create and save new comment
            Comment.objects.create(post=post, author=author, content=content)
            # Refresh the page to show the new comment
            return redirect('post_detail', post_id=post.id)

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})


def category_posts(request, category_id):
    # Get the category by id or 404 if not found
    category = get_object_or_404(Category, pk=category_id)
    # Get all posts linked to this category
    posts = Post.objects.filter(category=category).order_by('-created_at')
    return render(request, 'blog/category_posts.html', {'category': category, 'posts': posts})


def signup(request):
    # Handle user signup using built-in UserCreationForm
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def profile(request):
    user = request.user
    user_posts = user.post_set.all().order_by('-created_at')  # fetch posts by user
    return render(request, 'registration/profile.html', {'user': user, 'posts': user_posts})
