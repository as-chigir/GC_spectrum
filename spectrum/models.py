from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Ads(models.Model):
    ADS_TYPE = [
        ('Куплю', 'buy'),
        ('Продам', 'sell'),
        ('Отдам даром', 'give_free')
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
        return reverse('spectrum:detailed_ads',
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


class CommentAds(models.Model):
    name = models.CharField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    ads = models.ForeignKey(Ads,
                            on_delete=models.CASCADE,
                            related_name='comments_ads')


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    birth = models.DateTimeField(blank=True, null=True)
    photo = models.ImageField(upload_to="user/%Y/%m/%d", blank=True)


class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Slider(models.Model):
    name = models.CharField(max_length=100,
                            help_text='просто название слайда до 100 символов, оно обязательно',
                            verbose_name='Название слайда')
    title = models.CharField(blank=True,
                             max_length=150,
                             help_text='до 150 символов, заполнять не обязательно',
                             verbose_name='Заголовок на слайде')
    description = models.CharField(blank=True,
                                   max_length=150,
                                   help_text='до 150 символов, заполнять не обязательно',
                                   verbose_name='Текст под заголовком')
    slider_img = models.ImageField(blank=False,
                                   upload_to='slider/',
                                   help_text='изображение окажется до 1920*1024рх, поэтому лучше брать большое',
                                   verbose_name='Добавить изображение')

    class Meta:
        verbose_name = 'Блок 1ю0: Слайдер'
        verbose_name_plural = 'Блок 1ю0: Слайдеры'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('spectrum:board_list_by_category',
                       args=[self.slug])


class Board(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='board')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='board/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('spectrum:board_detail',
                       args=[self.id, self.slug])
