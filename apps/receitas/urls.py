from django.urls import path
from . import views

urlpatterns = [
   path('', views.ReceitaListView.as_view(), name='receita.list'),
   #path('', views.list, name='receita.list'),
   path('<int:pk>/', views.ReceitaDetailView.as_view(), name='receita.detail'),
   path('busca/', views.buscar, name='resultado_busca'),
   path('criar/', views.ReceitaCreateView.as_view(), name='receita.create'),
   path('editar/<int:pk>/', views.ReceitaUpdateView.as_view(), name='receita.update'),
   path('deletar/<int:pk>', views.ReceitaDeleteView.as_view(), name='receita.delete')
]