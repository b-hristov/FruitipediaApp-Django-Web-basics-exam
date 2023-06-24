from django.shortcuts import render, redirect

from FruitipediaApp.apps.fruit.models import Fruit
from FruitipediaApp.apps.profiles.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm
from FruitipediaApp.apps.common.views import get_profile

# Create your views here.


def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form
    }

    return render(
        request,
        'profiles/create-profile.html',
        context,
    )


def details_profile(request):
    profile = get_profile()
    posts_count = Fruit.objects.count()

    context = {
        'profile': profile,
        'posts_count': posts_count,
    }

    return render(
        request,
        'profiles/details-profile.html',
        context,
    )


def edit_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
        'profile': profile
    }

    return render(
        request,
        'profiles/edit-profile.html',
        context
    )


def delete_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': profile
    }

    return render(
        request,
        'profiles/delete-profile.html',
        context
    )
