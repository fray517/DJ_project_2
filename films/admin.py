from django.contrib import admin

from .models import Film


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    """Административный интерфейс для модели Film."""

    list_display = ("title", "description", "review")
    search_fields = ("title",)
    list_filter = ("title",)
