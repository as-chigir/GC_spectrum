from . import models

from django import forms


class EmailMaterialForm(forms.Form):
    name = forms.CharField(max_length=255)
    to_email = forms.EmailField()
    comment = forms.CharField(required=False,
                              widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)  # для закрытия пароля звездочками


class CommentAdsForm(forms.ModelForm):
    class Meta:
        model = models.CommentAds
        fields = ('name', 'body')
