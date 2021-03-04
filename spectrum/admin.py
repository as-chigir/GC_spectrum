from . import models
from django.contrib import admin

admin.site.register(models.CommentAds)
admin.site.register(models.Profile)


@admin.register(models.Ads)
class AdsAdmin(admin.ModelAdmin):
    list_display = ('title', 'ads_type', 'author', 'publish')  # что будет отображено в окне админки
    list_filter = ('ads_type', 'author', 'created')  # помогает фильтровать
    search_fields = ('title', 'body', 'author')  # поля, по которым будем искать
    prepopulated_fields = {'slug': ('title',)}  # значение без пробелов по заголовку
    ordering = ('publish', 'ads_type')  # порядок


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('publish', 'title')
