from django.contrib.auth.models import User
from django.shortcuts import render
from main import models

def index(request):
    
    animals_list = models.Animal.objects.filter(owner=User.objects.get(username=request.user.username))

    context = {
        'animals_list': animals_list
    }
    return render(request, "main/index.html", context)

def animal_card(request, name):
    context = {
        'name': name
    }
    return render(request, "main/animal_card.html", context)

def procedures_list(request, name, procedures):
    context = {
        'name': name,
        'procedures': procedures
    }
    return render(request, "main/procedures_list.html", context)

