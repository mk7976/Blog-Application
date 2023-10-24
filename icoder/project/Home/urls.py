from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="home"),
    path('contact/', views.Contact, name="contact"),
    path('about/', views.About, name="about"),
    path('signof/', views.Signof, name="signof"),
    path('login/', views.login, name="login"),
    path('logout/login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),

]
