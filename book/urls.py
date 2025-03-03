from django.urls import path,include
from . import views

urlpatterns = [
    path('google',views.google),
    path('list', views.books, name='book-list'),
    path('list-st',views.list_st),
    path('standard-list',views.standard_book_list,name='standard_book_list'),
    path('detail/<id>', views.detail,name='book-detail'),
]

