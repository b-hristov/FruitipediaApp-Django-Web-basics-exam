from django.shortcuts import render, redirect
from FruitipediaApp.apps.fruit.forms import FruitCreateForm, FruitEditForm, FruitDeleteForm
from FruitipediaApp.apps.fruit.models import Fruit

# Create your views here.


def create_fruit(request):
    if request.method == 'GET':
        form = FruitCreateForm()
    else:
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form
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
    # album = Album.objects.get(pk=pk)

    context = {
        'fruit': fruit,
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
        'fruit': fruit
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
        'fruit': fruit
    }

    return render(
        request,
        'fruit/delete-fruit.html',
        context,
    )
