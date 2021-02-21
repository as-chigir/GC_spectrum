from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Ads(models.Model):
    ADS_TYPE = [
        ('buy', 'Куплю'),
        ('sell', 'Продам'),
        ('give_free', 'Отдам даром'),
    ]
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='user_ads')
    ads_type = models.CharField(
        max_length=30,
        choices=ADS_TYPE,
    )


    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='user_news')
    publish = models.DateTimeField(default=timezone.now)


    # def __str__(self):
    #     return self.title
