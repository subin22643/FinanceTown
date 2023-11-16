from django.urls import path
from . import views

app_name = "boards"

urlpatterns = [
    path('finance/', views.finance, name="finance"),
    path('finance/<int:finance_pk>/', views.finance_detail, name="finance_detail"),
    path('finance/<int:finance_pk>/like/', views.finance_like, name="finance_like"),
    path('product/', views.product, name="product"),
    path('product/<int:product_pk>', views.product_detail, name="product_detail"),
    path('product/<int:product_pk>/like/', views.product_like, name="product_like"),
    path('finance/comments/<int:finance_pk>/', views.finance_comments, name='finance_comments'),
    path('product/comments/<int:product_pk>/', views.product_comments, name='product_comments'),
    path('comments/<int:comment_pk>/', views.finance_comments, name='finance_comments'),
 
    # path('QnA/', views.QnA, name="QnA"),
    # path('QnA/<int:QnA_pk>', views.QnA_detail, name="QnA_detail"),
    # QnA는 자주 묻는 질문 & 답변 기본으로 출력하고 + 상담 게시판(질문,답변) 으로 구현하기
]