from django.contrib import admin
from .models import Post, Category, Comment  # Import your blog models

# Register your models with the admin site
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)

# Customize admin site titles for better branding
admin.site.site_header = "Nikhil Project Admin"
admin.site.site_title = "Nikhil Project Portal"
admin.site.index_title = "Welcome to the Nikhil Project Dashboard"
