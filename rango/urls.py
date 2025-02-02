from django.urls import path
from . import views

app_name = "rango"  # Namespace for the app

urlpatterns = [
    path("", views.index, name="index"),  # Example route for the index view
    path("about/", views.about, name = "about")
]
