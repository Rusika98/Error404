from django.contrib import admin
from .models import BlogPosts
from .models import Comment

# Register your models here.
admin.site.register(BlogPosts)
admin.site.register(Comment)
