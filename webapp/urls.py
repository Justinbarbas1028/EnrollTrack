from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('home/', views.home_page, name = "home" ),
    path('about/', views.about_page, name = "about" ),
    path('contact/', views.contact_page, name = "contact" ),
    path('login/', views.login_page, name = "login" ),
    path('crud/', views.crud_page, name = "crud" ),
    
]