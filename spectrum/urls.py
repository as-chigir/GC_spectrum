from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

from django.urls import path
from django.urls import reverse_lazy

from . import views


app_name = 'spectrum'


urlpatterns = [
    path('', views.all_ads_, name='all_ads_'),
    path('news', views.all_news_, name='all_news_'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.detailed_ads_,
         name='detailed_ads'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.detailed_news_,
         name='detailed_news'),
    path('<int:ad_id>/share/', views.share_ads,
         name='share_ads'),
    # вход и выход
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # сброс пароля
    path('password_reset/', auth_views.PasswordResetView.as_view(
        success_url=reverse_lazy('spectrum:password_reset_done')
    ),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
             success_url=reverse_lazy('spectrum:password_reset_complete'),
         ),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('profile/', views.view_profile, name='profile'),
    path('register/', views.register, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
