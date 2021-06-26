from rest_framework import serializers
from .models import Anime, DownloadedAnime


class AnimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Anime
        fields = ('id', 'title', 'episode_count',
                  'anime_url')


class DownloadedAnimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DownloadedAnime
        fields = ('id', 'anime', 'episodes')
