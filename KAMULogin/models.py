from django.db import models


class BlogPosts(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=225)
    slug = models.SlugField(unique=True)
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

class Comment(models.Model):
    post = models.ForeignKey(BlogPosts, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    body = models.TextField()
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']



