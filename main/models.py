from django.db import models


class Animal(models.Model):
    """Класс описывает объект Животное"""

    name = models.CharField(max_length=30, verbose_name="Кличка")
    age = models.PositiveIntegerField(verbose_name="Возраст")
    breed = models.CharField(max_length=30, verbose_name="Порода")
    species = models.CharField(max_length=30, verbose_name="Вид животного")

    class Meta:
        verbose_name = "Животное"
        verbose_name_plural = "Животные"


class Vaccination(models.Model):
    """Класс описывающий объект Вакцинация"""

    date = models.DateField(verbose_name="Дата прививки")
    vaccine = models.CharField(max_length=50, verbose_name="Вакцина")

    class Meta:
        verbose_name = "Вакцинация"
        verbose_name_plural = "Вакцинация"


class AntiParasiteTreatment(models.Model):
    """Класс описывающий объект Обратока от паразитов"""

    parasite_species = models.CharField(max_length=30, verbose_name="Вид паразитов")
    date = models.DateField(verbose_name="Дата обработки")
    medication = models.CharField(max_length=50, verbose_name="Препарат")
    dosage = models.CharField(max_length=10, verbose_name="Дозировка")

    class Meta:
        verbose_name = "Обработка от паразитов"
        verbose_name_plural = "Обработка от паразитов"
