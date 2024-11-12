from django.urls import path
from . import views

urlpatterns = [
    path('', views.doador, name = "doador"),
    path('pesquisamaterial/',views.PesquisaMaterial, name="pesquisamaterial")
]
