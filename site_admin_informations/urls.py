from django.urls import path
from .views import admin_informations
urlpatterns = [
    path('', admin_informations),
]