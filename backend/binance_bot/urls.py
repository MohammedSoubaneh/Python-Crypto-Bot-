from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.Order)
    path('buy/', views.Buy )
]