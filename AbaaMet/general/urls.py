
from django.urls.conf import include
from general import views
from django.urls import path

urlpatterns = [
    path('',views.login, name='login'),
    path('principal/', views.index, name='inicio',)
]