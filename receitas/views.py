from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from .models import Receita
from .forms import ReceitaForm

class ReceitaListView(ListView):
   model = Receita
   template_name = 'receitas/list.html'
   context_object_name = 'receitas'

   #retorna apenas as receitas com o campo 'publicada' igual a True
   def get_queryset(self):
      return self.model.objects.order_by('-data_publicacao').filter(publicada=True)
   
class ReceitaDetailView(DetailView):
   model = Receita
   context_object_name = 'receita'
   template_name = 'receitas/detail.html'

class ReceitaCreateView(LoginRequiredMixin, CreateView):
   model = Receita
   form_class = ReceitaForm
   template_name = 'receitas/create.html'
   #success_url = 'usuarios/dashboard'
   success_url = reverse_lazy('dashboard')
   login_url = '/usuarios/login'
   #success_message = "%(fields) criado com sucesso!"

   """ def get_success_message(self, cleaned_data):
      print(cleaned_data)
      return "Receita criada com sucesso!" """

   def form_valid(self, form):
      self.object = form.save(commit=False)
      self.object.user = self.request.user
      self.object.save()
      return HttpResponseRedirect(self.get_success_url())


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
