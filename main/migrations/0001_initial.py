# Generated by Django 3.2.7 on 2021-09-14 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=30, verbose_name='Вид животного')),
                ('name', models.CharField(max_length=30, verbose_name='Кличка')),
                ('birth', models.DateField(verbose_name='Дата рождения')),
                ('breed', models.CharField(max_length=30, verbose_name='Порода')),
                ('gender', models.CharField(choices=[('Ж', 'Женский'), ('М', 'Мужской')], max_length=10, verbose_name='Пол')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Животное',
                'verbose_name_plural': 'Животные',
            },
        ),
        migrations.CreateModel(
            name='Vaccination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата прививки')),
                ('vaccine', models.CharField(max_length=50, verbose_name='Вакцина')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.animal', verbose_name='Животное')),
            ],
            options={
                'verbose_name': 'Вакцинация',
                'verbose_name_plural': 'Вакцинация',
            },
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parasite_type', models.CharField(choices=[('Гельминты', 'Гельминты'), ('Клещи', 'Клещи')], max_length=10, verbose_name='Вид паразитов')),
                ('date', models.DateField(verbose_name='Дата обработки')),
                ('medication', models.CharField(max_length=50, verbose_name='Препарат')),
                ('dosage', models.CharField(max_length=10, verbose_name='Дозировка')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.animal', verbose_name='Животное')),
            ],
            options={
                'verbose_name': 'Обработка от паразитов',
                'verbose_name_plural': 'Обработка от паразитов',
            },
        ),
    ]
