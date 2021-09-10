from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<str:name>/', views.animal_card, name="animal_card"),
    path('<str:name>/<str:procedures>', views.procedures_list, name="procedures_list"),

]