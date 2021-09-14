from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from main import models, forms


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
    if request.method == "POST":
        form = forms.VaccinationForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = forms.VaccinationForm()
    return render(
        request,
        "main/add_vaccination.html",
        {
            "form": form,
        },
    )


def add_treatment(request, pk):
    if request.method == "POST":
        form = forms.TreatmentForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = forms.TreatmentForm()
    return render(
        request,
        "main/add_treatment.html",
        {
            "form": form,
        },
    )


def add_animal(request):
    if request.method == "POST":
        form = forms.AnimalForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = forms.AnimalForm()
    return render(
        request,
        "main/add_animal.html",
        {
            "form": form,
        },
    )


def login(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
    else:
        form = forms.LoginForm()
    return render(
        request,
        "main/login.html",
        {
            "form": form,
        },
    )
