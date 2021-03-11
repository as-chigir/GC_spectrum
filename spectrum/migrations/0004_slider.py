# Generated by Django 3.1.7 on 2021-03-11 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spectrum', '0003_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='просто название слайда до 100 символов, оно обязательно', max_length=100, verbose_name='Название слайда')),
                ('title', models.CharField(blank=True, help_text='до 150 символов, заполнять не обязательно', max_length=150, verbose_name='Заголовок на слайде')),
                ('description', models.CharField(blank=True, help_text='до 150 символов, заполнять не обязательно', max_length=150, verbose_name='Текст под заголовком')),
                ('sliderimg', models.ImageField(help_text='изображение окажется до 1920*1024рх, поэтому лучше брать большое', upload_to='slider/', verbose_name='Добавить изображение')),
            ],
            options={
                'verbose_name': 'Блок 1ю0: Слайдер',
                'verbose_name_plural': 'Блок 1ю0: Слайдеры',
            },
        ),
    ]