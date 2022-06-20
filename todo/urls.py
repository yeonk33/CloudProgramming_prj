from django.urls import path
from todo import views

urlpatterns = [
    path('', views.mainpage),
    path('list/', views.TodoList.as_view()),
    path('<int:pk>/', views.TodoDetail.as_view()),
    path('category/<str:slug>/', views.cagegories_page),
    path('tag/<str:slug>/', views.tag_page),
    path('create/', views.TodoCreate.as_view()),
    path('update/<int:pk>/', views.TodoUpdate.as_view()),
]