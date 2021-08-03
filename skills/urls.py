from django.urls import path
from .views import admin_skills
urlpatterns = [
    path('manage', admin_skills),
]