from django.urls import path
from . import views

app_name = "CherryPickingPicture"

urlpatterns = [
    path('', views.main, name='main'),
    path('Login', views.login, name='login'),
]

