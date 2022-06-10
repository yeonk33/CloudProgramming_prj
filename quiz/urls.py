from django.contrib import admin
from django.urls import path

from quiz import views

urlpatterns = [
    path('', views.home),
    path('quizpage/', views.quiz),
    path('result/', views.result),

]