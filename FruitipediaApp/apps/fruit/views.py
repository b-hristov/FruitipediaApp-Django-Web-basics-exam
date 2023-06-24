from django.shortcuts import render, redirect
from FruitipediaApp.apps.fruit.forms import FruitCreateForm, FruitEditForm, FruitDeleteForm
from FruitipediaApp.apps.fruit.models import Fruit
from FruitipediaApp.apps.common.views import get_profile

# Create your views here.

profile = get_profile()


def create_fruit(request):
    if request.method == 'GET':
        form = FruitCreateForm()
    else:
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile': profile
    }

    return render(
        request,
        'fruit/create-fruit.html',
        context,
    )


def details_fruit(request, pk):
    fruit = Fruit.objects \
        .filter(pk=pk) \
        .get()

    context = {
        'fruit': fruit,
        'profile': profile
    }

    return render(
        request,
        'fruit/details-fruit.html',
        context,
    )


def edit_fruit(request, pk):
    fruit = Fruit.objects \
        .filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = FruitEditForm(instance=fruit)
    else:
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit,
        'profile': profile
    }

    return render(
        request,
        'fruit/edit-fruit.html',
        context,
    )


def delete_fruit(request, pk):
    fruit = Fruit.objects \
        .filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = FruitDeleteForm(instance=fruit)
    else:
        form = FruitDeleteForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit,
        'profile': profile
    }

    return render(
        request,
        'fruit/delete-fruit.html',
        context,
    )
