from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница (список фильмов)
    path('add/', views.add_film, name='add_film'),  # Добавление фильма
]

