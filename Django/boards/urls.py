from django.urls import path
from . import views

app_name = "boards"

urlpatterns = [
    path('boards/', views.boards, name="boards"),
    path('boards/<int:pk>', views.boardDetail, name="boardDetail"),
]
