from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
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


@login_required
def add_post(request):
    if request.method == "POST":
        form = AddPost(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.published = True
            new_post.owner = request.user
            new_post.save()
            return redirect('index')
    else:
        form = AddPost()
    context = {'form': form}
    return render(request, 'post/add_post.html', context)


@login_required
def del_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if not request.user == post.owner:
        return redirect('get_post', pk=pk)
    post.delete()
    return redirect('index')


@login_required
def updated_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if not request.user == post.owner:
        return redirect('get_post', pk=pk)

    if request.method == "POST":
        form = AddPost(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddPost(instance=post)
    context = {'form': form}
    return render(request, 'post/add_post.html', context)
