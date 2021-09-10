# Generated by Django 3.2.7 on 2021-09-10 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Кличка')),
                ('age', models.PositiveIntegerField(verbose_name='Возраст')),
                ('breed', models.CharField(max_length=30, verbose_name='Порода')),
                ('species', models.CharField(max_length=30, verbose_name='Вид животного')),
            ],
        ),
        migrations.CreateModel(
            name='AntiParasiteTreatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parasite_species', models.CharField(max_length=30, verbose_name='Вид паразитов')),
                ('date', models.DateField(verbose_name='Дата обработки')),
                ('medication', models.CharField(max_length=50, verbose_name='Препарат')),
                ('dosage', models.CharField(max_length=10, verbose_name='Дозировка')),
            ],
        ),
        migrations.CreateModel(
            name='Vaccination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата прививки')),
                ('vaccine', models.CharField(max_length=50, verbose_name='Вакцина')),
            ],
        ),
    ]
