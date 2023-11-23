from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('boards/', include('boards.urls')),
    path('exchanges/', include('exchanges.urls')),
    path('search/', include('search.urls')),
    path('news/', include('news.urls')),
    path('quiz/', include('quizzes.urls')),
]
