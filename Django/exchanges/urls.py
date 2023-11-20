from django.urls import path
from . import views

app_name = 'moneys'
urlpatterns = [
    path('', views.exchange)
]