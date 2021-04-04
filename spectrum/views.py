from . import constants
from . import forms
from . import models

from .forms import CityForm
from .forms import UserRegistrationForm

from .models import City

from django.core.mail import send_mail

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from django.contrib.auth import authenticate
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

import requests


def main_(request):
    return render(request, 'menu/main.html')


def about_(request):
    return render(request, 'menu/about.html')


def weather_(request):
    appid = 'b928b3d3e4e846273ace5bd7ccfd081d'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()  # для очистки строки запроса

    cities = City.objects.all()
    all_cities = []
    for city in cities:
        res = requests.get(url.format(city)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }
        all_cities.append(city_info)

    context_weather = {'all_info': all_cities, 'form': form}
    return render(request, 'menu/weather.html', context_weather)


def docs_(request):
    return render(request, 'menu/documents.html')


def all_ads_(request):
    all_ads = models.Ads.objects.all()
    current_page = Paginator(all_ads, 2)  # устанавливаем по 3 объявления на каждой странице
    page = request.GET.get('page')
    try:
        ads = current_page.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, поставим первую страницу
        ads = current_page.page(1)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        ads = current_page.page(current_page.num_pages)
    return render(request, "ads/all_ads.html",
                  {"page": page,
                   "ads": ads})


def all_news_(request):
    all_news = models.News.objects.all()
    return render(request, "news/all_news.html",
                  {"news": all_news})


@login_required
def detailed_ads_(request, year, month, day, slug):
    ads = get_object_or_404(models.Ads,
                            publish__year=year,
                            publish__month=month,
                            publish__day=day,
                            slug=slug)
    if request.method == "POST":
        form = forms.CommentAdsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.material = ads
            comment.save()
            return redirect(ads)
    else:
        form = forms.CommentAdsForm(request.POST)
    return render(request, "ads/detailed_ads.html",
                  {"ads": ads,
                   "form": form})


def share_ads(request, ad_id):  # отправить комментарии
    ad = get_object_or_404(models.Ads, id=ad_id)
    sent = False
    if request.method == "POST":
        form = forms.EmailMaterialForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ad_uri = request.build_absolute_uri(
                ad.get_absolute_url(),
            )
            subject = constants.SHARE_EMAIL_SUBJECT.format(
                cd['name'],
                ad.title,
            )
            body = constants.SHARE_EMAIL_BODY.format(
                title=ad.title,
                uri=ad_uri,
                comment=cd['comment'],
            )

            send_mail(subject, body, 'admin@my.com', [cd['to_email'], ])
            sent = True
    else:
        form = forms.EmailMaterialForm()

    return render(request,
                  'ads/share_ads.html',
                  {'ad': ad, 'form': form, 'sent': sent})


def custom_login_(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['username'],
                password=cd['password'],
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Аутентификация прошла успешно')
                else:
                    return HttpResponse('Учетная запись отключена')
            else:
                return HttpResponse('Неверные данные')
    else:
        form = forms.LoginForm()
        return render(request, 'registration/login.html', {'form': form})


@login_required
def view_profile(request):
    return render(request, 'profile/profile.html', {'user': request.user})


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            models.Profile.objects.create(user=new_user)
            return render(request, 'profile/registration_complete.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'profile/register.html', {'user_form': user_form})


def edit_profile(request):
    if request.method == "POST":
        user_form = forms.UserEditForm(data=request.POST,
                                       instance=request.user)
        profile_form = forms.ProfileEditForm(data=request.POST,
                                             instance=request.user.profile,
                                             files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            """
            if not profile_form.cleaned_data['photo']:
                profile_form.cleaned_data['photo'] = request.user.profile.photo
            profile_form.save()
            return render(request, 'profile/profile.html', {'user': request.user})
            """
    else:
        user_form = forms.UserEditForm(instance=request.user)
        profile_form = forms.ProfileEditForm(instance=request.user.profile)
    return render(request, 'profile/edit_profile.html', {'user_form': user_form,
                                                         'profile_form': profile_form})
