from django import forms
from main import models


class AnimalForm(forms.ModelForm):
    class Meta:
        model = models.Animal
        fields = ("species", "name", "birth", "breed", "gender")


class VaccinationForm(forms.ModelForm):
    class Meta:
        model = models.Vaccination
        fields = ("date", "vaccine")


class TreatmentForm(forms.ModelForm):
    class Meta:
        model = models.Treatment
        fields = ("date", "medication", "parasite_type", "dosage")
