# Generated by Django 3.2.6 on 2022-11-22 18:55

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(help_text='Введите имя, максимальное количество символов: 50', max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(help_text='Введите фамилию, максимальное количество символов: 50', max_length=50, verbose_name='Фамилия')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(help_text='Укажите телефон для связи', max_length=128, region=None, verbose_name='Телефон для связи')),
                ('email', models.EmailField(help_text='Введите ваш email', max_length=254, unique=True, verbose_name='Email адрес')),
                ('role', models.CharField(choices=[('user', 'Пользователь'), ('admin', 'Администратор')], default='user', help_text='Выберите роль пользователя', max_length=15, verbose_name='Роль')),
                ('image', models.ImageField(blank=True, help_text='Разместите Ваше фото', null=True, upload_to='photos/', verbose_name='Фото')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
