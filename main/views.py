from django.contrib.auth.models import User
from django.shortcuts import render
from main import models


def index(request):

    animals_list = models.Animal.objects.filter(
        owner=User.objects.get(username=request.user.username)
    )

    context = {
        "animals_list": animals_list,
    }
    return render(request, "main/index.html", context)


def animal_card(request, pk):
    animal = models.Animal.objects.get(id=pk)
    context = {"animal": animal}
    return render(request, "main/animal_card.html", context)


def vaccinations(request, pk):
    vaccinations = models.Vaccination.objects.filter(animal=pk)
    context = {
        "vaccinations": vaccinations,
    }
    return render(request, "main/vaccinations.html", context)


def treatments(request, pk):
    treatments = models.Treatment.objects.filter(animal=pk)
    context = {
        "treatments": treatments,
    }
    return render(request, "main/treatments.html", context)


def add_vaccination(request, pk):

    context = {
        "status": "ok",
    }
    return render(request, "main/add_vaccination.html", context)


def add_treatment(request, pk):

    context = {
        "status": "ok",
    }
    return render(request, "main/add_treatment.html", context)


def add_animal(request):

    context = {
        "status": "ok",
    }
    return render(request, "main/add_animal.html", context)
