from main import models
from main.tests import variables as var


def run_db_append():
    create_animal(var.animals_list)
    create_vaccination(var.vaccination_list)
    create_treatments(var.treatments_list)


def create_owner(users_list):
    for user in users_list:
        if not models.User.objects.filter(username=user["name"]):
            models.User(
                username=user["name"], password=user["password"], email=user["email"]
            ).save()


def create_animal(animals_list):
    for animal in animals_list:
        models.Animal(
            owner=models.User.objects.get(username=animal["owner"]),
            species=animal["species"],
            name=animal["name"],
            birth=animal["birth"],
            breed=animal["breed"],
            gender=animal["gender"],
        ).save()


def create_vaccination(vaccination_list):
    for vaccination in vaccination_list:
        models.Vaccination(
            animal=models.Animal.objects.get(name=vaccination["animal"]),
            date=vaccination["date"],
            vaccine=vaccination["vaccine"],
        ).save()


def create_treatments(treatments_list):
    for treatment in treatments_list:
        models.Treatment(
            animal=models.Animal.objects.get(name=treatment["animal"]),
            parasite_type=treatment["parasite_type"],
            date=treatment["date"],
            medication=treatment["medication"],
            dosage=treatment["dosage"],
        ).save()
