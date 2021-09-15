from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import AddPost


def index(request):
    posts = Post.objects.filter(published=True).order_by('-updated_date')
    context = {'posts': posts, 'title': 'Home page'}
    return render(request, 'post/index.html', context)


def get_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    return render(request, 'post/post.html', context)


def add_post(request):
    if request.method == "POST":
        form = AddPost(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.published = True
            new_post.save()
            return redirect('index')
    else:
        form = AddPost()
    context = {'form': form}
    return render(request, 'post/add_post.html', context)


def del_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('index')


def updated_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = AddPost(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddPost(instance=post)
    context = {'form': form}
    return render(request, 'post/add_post.html', context)
