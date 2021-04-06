from . import models
from django.contrib import admin
from .models import City

admin.site.register(models.CommentAds)
admin.site.register(models.Profile)
admin.site.register(City)


@admin.register(models.Ads)
class AdsAdmin(admin.ModelAdmin):
    list_display = ('title', 'ads_type', 'author', 'publish')
    list_filter = ('ads_type', 'author', 'created')
    search_fields = ('title', 'body', 'author')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('publish', 'ads_type')


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('publish', 'title')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'updated']
    list_filter = ['created', 'updated']
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
