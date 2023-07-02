from django.urls import path
from . import views

urlpatterns = [
    path('', views.myView),
    path('drinks/<str:drink_name>', views.drinks, name="drink_name"),
    path('aboutus/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('book/', views.book, name="book"),
]
