from django.urls import path
from . import views

app_name = "boards"

urlpatterns = [
    path('product/', views.product, name="product"),
    path('product/<int:product_pk>/', views.product_detail, name="product_detail"),
    path('product/<int:product_pk>/like/', views.product_like, name="product_like"),
    path('product/comments/<int:product_pk>/', views.product_comments, name='product_comments'),
    path('product/comments/delete/<int:comment_pk>/', views.product_comments_delete, name='product_comments_delete'),
    path('QnA/', views.QnA, name="QnA"),
    path('QnA/<int:QnA_pk>/', views.QnA_detail, name="QnA_detail"),
    path('QnA/<int:QnA_pk>/like/', views.QnA_like, name="QnA_like"),
    path('QnA/comments/<int:QnA_pk>/', views.QnA_comments, name='QnA_comments'),
    path('QnA/comments/delete/<int:comment_pk>/', views.QnA_comments_delete, name='QnA_comments_delete'),

     # QnA는 자주 묻는 질문 & 답변 기본으로 출력하고 + 상담 게시판(질문,답변) 으로 구현하기
]