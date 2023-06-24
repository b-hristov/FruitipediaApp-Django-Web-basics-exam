from django.urls import path
from FruitipediaApp.apps.fruit.views import create_fruit, edit_fruit, delete_fruit, details_fruit

urlpatterns = [
    path('create/', create_fruit, name='create fruit'),
    path('/<int:pk>/details/', details_fruit, name='details fruit'),
    path('/<int:pk>/edit/', edit_fruit, name='edit fruit'),
    path('/<int:pk>/delete/', delete_fruit, name='delete fruit'),
]
