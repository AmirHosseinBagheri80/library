from django.urls import path,include
from . import views

urlpatterns = [
    path('list', views.books),
    path('detail', views.detail),
]

