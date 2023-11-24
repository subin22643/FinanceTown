from django.urls import path
from . import views

app_name = 'search'
urlpatterns = [
    path('', views.deposit_index),
    # path('/deposit-products', views.deposit_index), # 인덱스페이지
    path('save-deposit-products', views.save_deposit_products),
    path('deposit-product/<str:fin_prdt_cd>', views.deposit_products_options),
    # path('deposit-products_options/<str:fin_prdt_cd>', views.deposit_products_options),
    # path('deposit-products/top_rate', views.top_rate_deposit),
    path('saving-products', views.saving_index),
    path('save-saving-products', views.save_saving_products),
    path('saving-products-options/<str:fin_prdt_cd>', views.saving_products_options),
    # path('saving-products/top_rate', views.top_rate_saving),
]
