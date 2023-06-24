from django.shortcuts import render
from FruitipediaApp.apps.profiles.models import Profile
from FruitipediaApp.apps.fruit.models import Fruit

# Create your views here.


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def get_fruits():
    try:
        return Fruit.objects.all()
    except Fruit.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()
    if profile:
        context = {
            'created_user': profile
        }
        return render(
            request,
            'common/index.html',
            context
        )

    return render(
        request,
        'common/index.html',
    )


def dashboard(request):
    fruits = get_fruits()
    if fruits:
        context = {
            'fruits': fruits
        }
        return render(
            request,
            'common/dashboard.html',
            context
        )
    return render(
        request,
        'common/dashboard.html',
    )

