from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from .serializers import AnimeSerializer, DownloadedAnimeSerializer
from .models import Anime, DownloadedAnime
from .filters import CaseInsensitiveOrderingFilter
from django.db.models import Count
import json
# Create your views here.


class AnimeView(viewsets.ModelViewSet):
    serializer_class = AnimeSerializer
    filter_backends = [CaseInsensitiveOrderingFilter]
    ordering = ['title']

    def get_queryset(self):
        queryset = Anime.objects.all()
        anime_url = self.request.query_params.get('anime_url')
        title = self.request.query_params.get('title')
        if anime_url is not None:
            queryset = queryset.filter(anime_url=anime_url)
        if title is not None:
            queryset = queryset.filter(title=title)
        return queryset

    def list(self, request, *args, **kwargs):
        response = super().list(self, request, *args, **kwargs)
        response.data[-1]['count'] = Anime.objects.count()
        return response


class DownloadedAnimeView(viewsets.ModelViewSet):
    serializer_class = DownloadedAnimeSerializer

    def get_queryset(self):
        queryset = DownloadedAnime.objects.all()
        anime = self.request.query_params.get('anime')
        if anime is not None:
            queryset = queryset.filter(anime=anime)
        return queryset
