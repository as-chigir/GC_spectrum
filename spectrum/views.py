from django.shortcuts import get_object_or_404
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


def detailed_ads_(request, year, month, day, slug):
    detailed_ads = get_object_or_404(models.Ads,
                                     publish__year=year,
                                     publish__month=month,
                                     publish__day=day,
                                     slug=slug)
    return render(request, "ads/detailed_ads.html",
                  {"ad": detailed_ads})


def detailed_news_(request, year, month, day, slug):
    detailed_news = get_object_or_404(models.Ads,
                                      publish__year=year,
                                      publish__month=month,
                                      publish__day=day,
                                      slug=slug)
    return render(request, "news/detailed_news.html",
                  {"new": detailed_news})
