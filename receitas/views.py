from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Receita

class ReceitasListView(ListView):
   model = Receita
   template_name = 'receitas/list.html'
   context_object_name = 'receitas'

   #retorna apenas as receitas com o campo 'publicada' igual a True
   def get_queryset(self):
      return self.model.objects.order_by('-data_publicacao').filter(publicada=True)
   
class ReceitasDetailView(DetailView):
   model = Receita
   context_object_name = 'receita'
   template_name = 'receitas/detail.html'


def buscar(request):
   #Só pode pesquisar as receitas que foram publicadas
   receitas = Receita.objects.order_by('data_publicacao').filter(publicada=True)

   #'nome_comida' é o parametro do form em search.html (partials)
   if 'nome_comida' in request.GET: #se 'nome_comida' tem algum valor nesta requisicao GET
      search = request.GET['nome_comida']
      if search:
         receitas = receitas.filter(nome_receita__icontains=search)
   
   dados = {
      'receitas': receitas
   }

   return render(request, 'receitas/resultado_busca.html', dados)
