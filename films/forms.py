from django import forms

from .models import Film


class FilmForm(forms.ModelForm):
    """Форма для добавления фильма."""

    class Meta:
        model = Film
        fields = ["title", "description", "review"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите название фильма"
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Введите описание фильма"
                }
            ),
            "review": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Введите отзыв о фильме"
                }
            ),
        }
        labels = {
            "title": "Название фильма",
            "description": "Описание фильма",
            "review": "Отзыв",
        }
