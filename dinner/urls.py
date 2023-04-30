from django.urls import path
from . import views

urlpatterns = [
    path('user', views.signup),
    path('add/<str:nickname>',views.addBook),
    path('mybooks/<str:nickname>', views.getMyBooks),
    path('books', views.getAllBooks),
]