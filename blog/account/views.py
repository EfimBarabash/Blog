from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterUserForm, EditUserForm, EditProfileForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Profile
import json


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=True)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html')
    else:
        form = RegisterUserForm()
    context = {'form': form}
    return render(request, 'account/register.html', context)


@login_required
def get_profile(request, id):
    profile = get_object_or_404(Profile, id=id)
    posts = profile.user.posts.all()
    my_profile = True
    follow = False
    page = request.GET.get('page', default=1)
    if request.user.profile != profile:
        my_profile = False
        follow = request.user.profile.following.filter(id=profile.id).exists()
        print(follow)
    context = {'profile': profile, 'my_profile': my_profile, 'page': page, 'follow': follow, 'posts':posts}
    return render(request, 'profile/profile.html', context)


@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile', id=profile.id)
    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = EditProfileForm(instance=profile)

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'profile/edit_profile.html', context)


@login_required
def get_profile_list_follow(request, profile_id, follow):
    if follow:
        list_follow = Profile.objects.get(id=profile_id).followers.all()
    else:
        list_follow = Profile.objects.get(id=profile_id).following.all()
    context = {'list_follow': list_follow}
    return render(request, 'profile/list_follow.html', context)


@login_required
def following(request):
    data = json.loads(request.body)
    follow_account = Profile.objects.get(user__id=data['user_id'])
    if not request.user.profile.following.filter(id=follow_account.id).exists():
        request.user.profile.following.add(follow_account)
        res = {
            'follow': True
        }
    else:
        request.user.profile.following.remove(follow_account)
        res = {
            'follow': False
        }
    return JsonResponse(data=res)

