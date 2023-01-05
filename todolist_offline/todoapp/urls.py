from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('documentation/', views.doc, name='doc'),
    path('payment/',views.payment,name='payment'),
    path('delete/<str:pk>',views.delete,name='delete'),
    path('register/',views.register,name='register'),
    path('login/', views.login, name='login'),
    path('logout/',views.LogoutPage, name='logout')
]