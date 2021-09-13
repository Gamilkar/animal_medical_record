from django.urls import path
from main import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_animal/", views.add_animal, name="add_animal"),
    path("<int:pk>/", views.animal_card, name="animal_card"),
    path("<int:pk>/vaccinations", views.vaccinations, name="vaccinations"),
    path("<int:pk>/treatments", views.treatments, name="treatments"),
    path("<int:pk>/add_vaccination", views.add_vaccination, name="add_vaccination"),
    path("<int:pk>/add_treatment", views.add_treatment, name="add_treatment"),
]
