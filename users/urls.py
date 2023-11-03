from django.urls import path
from . import views

urlpatterns = [
    
    #what are these 3 arguments within the path method?urlRoute, nameofapp
    path('users/', views.users, name='users'),
]