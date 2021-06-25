from django.contrib import admin

from .models import Anime


class AnimeAdmin(admin.ModelAdmin):
    list_display = ('title', 'episode_count', 'anime_url')

# Register your models here.


admin.site.register(Anime, AnimeAdmin)
