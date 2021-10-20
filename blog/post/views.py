from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Post
from .forms import AddPost, AddComment
import json


def index(request):
    posts = Post.objects.all().order_by('-created_date')
    page = request.GET.get('page', default=1)
    paginator = Paginator(posts, 8)
    page_obj = paginator.page(page)
    context = {'posts': page_obj}
    return render(request, 'post/index.html', context)


@login_required
def liked(request):
    posts = Post.objects.filter(like=request.user.id)
    page = request.GET.get('page', default=1)
    paginator = Paginator(posts, 8)
    page_obj = paginator.page(page)
    context = {'posts': page_obj}
    return render(request, 'post/index.html', context)


@login_required
def by_subscription(request):
    list_id = list(request.user.profile.following.values_list('id', flat=True))
    posts = Post.objects.filter(owner__profile__in=list_id)
    page = request.GET.get('page', default=1)
    paginator = Paginator(posts, 8)
    page_obj = paginator.page(page)
    context = {'posts': page_obj}
    return render(request, 'post/index.html', context)


@login_required
def get_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like = False
    if request.user.is_authenticated:
        like = request.user.like_posts.filter(id=pk).exists()
        print(like)
    context = {'post': post, 'like': like, }
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


@login_required
def add_comment(request, post_id):
    if request.method == "POST":
        comment_form = AddComment(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.owner = request.user
            new_comment.post = Post.objects.get(id=post_id)
            new_comment.save()
            return redirect('get_post', pk=post_id)
    else:
        comment_form = AddComment()
    context = {'comment_form': comment_form, 'post_id': post_id}
    return render(request, 'post/add_comment.html', context)


@login_required
def like_to_post(request):
    data = json.loads(request.body)
    post = Post.objects.get(id=data['post_id'])
    if not post.like.filter(id=request.user.id).exists():
        post.like.add(request.user)
        res = {
            'like': True,
            'like_count': post.like.count()
        }
    else:
        post.like.remove(request.user)
        res = {
            'like': False,
            'like_count': post.like.count()
        }

    return JsonResponse(data=res)
