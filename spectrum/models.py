from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Ads(models.Model):
    ADS_TYPE = [
        ('Куплю', 'buy'),
        ('Продам', 'sell'),
        ('Отдам даром', 'give_free'),
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

    def get_absolute_url(self):
        return reverse('spectrum:detailed_ads',  # name из path в urls.py проекта
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])


class News(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='user_news')
    publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('spectrum:detailed_news',   # name из path в urls.py проекта
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])
