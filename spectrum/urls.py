from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'spectrum'


urlpatterns = [
    path('', views.all_ads_, name='all_ads_'),
    path('', views.all_news_, name='all_news_'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.detailed_ads_,
         name='detailed_ads'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.detailed_news_,
         name='detailed_news'),
    path('<int:ad_id>/share/', views.share_ads,
         name='share_ads'),
    path('login/', auth_views.LoginView.as_view(), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
]
