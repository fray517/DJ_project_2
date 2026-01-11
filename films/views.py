from django.shortcuts import redirect, render

from .forms import FilmForm
from .models import Film


def add_film(request):
    """Представление для добавления нового фильма."""

    if request.method == "POST":
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("films_list")
    else:
        form = FilmForm()

    return render(request, "films/add_film.html", {"form": form})


def films_list(request):
    """Представление для отображения списка всех фильмов."""

    films = Film.objects.all()
    return render(request, "films/films_list.html", {"films": films})

