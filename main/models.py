from django.db import models
from django.contrib.auth.models import User


class Animal(models.Model):
    """Класс описывает объект Животное"""

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец")
    species = models.CharField(max_length=30, verbose_name="Вид животного")
    name = models.CharField(max_length=30, verbose_name="Кличка")
    birth = models.DateField(verbose_name="Дата рождения")
    breed = models.CharField(max_length=30, verbose_name="Порода")
    gender = models.CharField(
        max_length=10, choices=[("Ж", "Женский"), ("М", "Мужской")], verbose_name="Пол"
    )

    class Meta:
        verbose_name = "Животное"
        verbose_name_plural = "Животные"

    def __str__(self):
        return self.name


class Vaccination(models.Model):
    """Класс описывающий объект Вакцинация"""

    animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE, verbose_name="Животное"
    )
    date = models.DateField(verbose_name="Дата прививки")
    vaccine = models.CharField(max_length=50, verbose_name="Вакцина")

    class Meta:
        verbose_name = "Вакцинация"
        verbose_name_plural = "Вакцинация"

    def __str__(self):
        return f"{self.date}"


class Treatment(models.Model):
    """Класс описывающий объект Обратока от паразитов"""

    animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE, verbose_name="Животное"
    )
    parasite_type = models.CharField(
        max_length=10,
        choices=[("Гельминты", "Гельминты"), ("Клещи", "Клещи")],
        verbose_name="Вид паразитов",
    )
    date = models.DateField(verbose_name="Дата обработки")
    medication = models.CharField(max_length=50, verbose_name="Препарат")
    dosage = models.CharField(max_length=10, verbose_name="Дозировка")

    class Meta:
        verbose_name = "Обработка от паразитов"
        verbose_name_plural = "Обработка от паразитов"

    def __str__(self):
        return f"{self.date}"
