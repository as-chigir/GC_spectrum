from . import models
from django.contrib import admin
from .models import City

admin.site.register(models.CommentAds)
admin.site.register(models.Profile)
admin.site.register(City)


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

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class BoardAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Board, BoardAdmin)
