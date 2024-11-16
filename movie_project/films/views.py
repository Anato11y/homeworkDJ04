from django.shortcuts import render, redirect
from .forms import FilmForm
from .models import Film

def home(request):
    """Главная страница с отображением списка фильмов"""
    films = Film.objects.all()  # Получение всех фильмов из базы данных
    return render(request, 'films/home.html', {'films': films})

def add_film(request):
    """Страница добавления нового фильма"""
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправление на главную страницу
    else:
        form = FilmForm()
    return render(request, 'films/add_film.html', {'form': form})

