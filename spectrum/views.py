from django.shortcuts import render
from . import models


def all_ads_(request):
    all_ads = models.Ads.objects.all()
    return render(request, "ads/all_ads.html",
                  {"ads": all_ads})


def all_news_(request):
    all_news = models.News.objects.all()
    return render(request, "news/all_news.html",
                  {"news": all_news})


