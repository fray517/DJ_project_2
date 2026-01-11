from django.db import models


class Film(models.Model):
    """Модель для хранения информации о фильмах."""

    title = models.CharField(
        max_length=200,
        verbose_name="Название фильма"
    )
    description = models.TextField(
        verbose_name="Описание фильма"
    )
    review = models.TextField(
        verbose_name="Отзыв"
    )

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        ordering = ["title"]

    def __str__(self) -> str:
        return self.title
