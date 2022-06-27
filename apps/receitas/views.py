from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView
from django.views.generic.edit import DeleteView
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
#from django.contrib.messages.views import SuccessMessageMixin

from .models import Receita
from .forms import ReceitaForm

class ReceitaDeleteView(DeleteView):
   model = Receita
   context_object_name = 'receita'
   success_url = reverse_lazy('dashboard')
   template_name = 'receitas/delete.html'


class ReceitaListView(ListView):
   model = Receita
   template_name = 'receitas/list.html'
   context_object_name = 'receitas'
   paginate_by = 2

   #retorna apenas as receitas com o campo 'publicada' igual a True
   def get_queryset(self):
      return self.model.objects.order_by('-data_publicacao').filter(publicada=True)

""" def list(request):
   receitas = Receita.objects.order_by('-data_publicacao').filter(publicada=True)
   paginator = Paginator(receitas, 2)

   #identifica a 'page' atual
   page_number = request.GET.get('page') 
   page_object = paginator.get_page(page_number)
   page_object.adjusted_elided_pages = paginator.get_elided_page_range(page_number)
   context = {'page_obj': page_object}
   return render(request, 'receitas/list.html', context) """

class ReceitaUpdateView(LoginRequiredMixin, UpdateView):
   model = Receita
   success_url = reverse_lazy('dashboard')
   form_class = ReceitaForm
   template_name = 'receitas/update.html'
   
class ReceitaDetailView(DetailView):
   model = Receita
   context_object_name = 'receita'
   template_name = 'receitas/detail.html'

class ReceitaCreateView(LoginRequiredMixin, CreateView):
   model = Receita
   form_class = ReceitaForm
   template_name = 'receitas/create.html'
   success_url = reverse_lazy('dashboard')
   login_url = '/usuarios/login'

   def form_valid(self, form):
      self.object = form.save(commit=False)
      self.object.user = self.request.user
      self.object.save()
      #https://stackoverflow.com/questions/39999956/django-how-to-send-a-success-message-using-a-updateview-cbv
      messages.success(self.request, "Receita criada com sucesso!")
      return HttpResponseRedirect(self.get_success_url())


def buscar(request):
   """ Função que realiza uma busca pelo nome da receita que está publicada """
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
