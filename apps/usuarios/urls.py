from django.urls import path
from . import views

urlpatterns = [
   path('cadastro/', views.cadastro, name='cadastro'),
   path('login/', views.login, name='login'),
   path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
   path('logout/', views.logout, name='logout'),
]