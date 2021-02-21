from django.urls import path
from . import views


app_name = 'spectrum'


urlpatterns = [
    path('', views.all_ads_, name='all_ads_'),
    path('', views.all_news_, name='all_news_'),
]
