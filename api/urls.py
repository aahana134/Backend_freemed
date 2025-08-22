from django.urls import path
from . import views

urlpatterns = [
    path('free_medicines/', views.get_free_medicines),
    path('disease_medicines/', views.get_disease_medicines),
    path('health_centers/', views.get_health_centers),
]
