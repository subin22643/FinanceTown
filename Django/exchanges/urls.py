from django.urls import path
from . import views

app_name = 'exchanges'
urlpatterns = [
    path('', views.exchange)
]