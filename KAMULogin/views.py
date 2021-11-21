from django.shortcuts import render, redirect
from .models import BlogPosts, Comment
from .forms import CommentForm, PostForm
from django.http import HttpResponseRedirect

# Create your views here.
def loginpage (request):
    return render(request, 'Login_page.html')

def frontpage (request):
    post = BlogPosts.objects.all()
    return render(request, 'frontpage.html',{'BlogPosts': post})

def post_detail (request, slug: object):
    posts = BlogPosts.objects.get(slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = posts
            comment.save()

            return redirect('post_detail', slug=posts.slug)
    else:
        form = CommentForm()

    return render(request, 'post_detail.html',{'BlogPosts': posts, 'form': form})


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect('frontpage')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})

def showcomment(request):
    com = Comment.objects.all()
    return render(request, 'post_details.html', {'Comment': com})





