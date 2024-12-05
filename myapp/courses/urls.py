from django.urls import path
from .import views

urlpatterns = [
    path('',views.C, name='C'),
    path('E/<str:course_id>/',views.E, name='E'),
]