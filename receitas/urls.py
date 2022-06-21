from django.urls import path
from . import views

urlpatterns = [
   path('', views.ReceitasListView.as_view(), name='receitas.list'),
   path('<int:pk>/', views.ReceitasDetailView.as_view(), name='receitas.detail'),
   path('busca/', views.buscar, name='resultado_busca')
]