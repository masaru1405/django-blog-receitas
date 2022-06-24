from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from receitas.models import Receita

def cadastro(request):
   if request.method == 'POST':
      nome = request.POST['nome']
      email = request.POST['email']
      senha = request.POST['password']
      senha2 = request.POST['password2']
      
      #se nulo (a função strip tira espaços em branco)
      if not nome.strip():
         messages.error(request, 'O campo nome não pode ficar em branco')
         return redirect('cadastro')
      if not email.strip():
         messages.error(request, 'O campo email não pode ficar em branco')
         return redirect('cadastro')
      if senha != senha2:
         messages.error(request, 'As senhas não são iguais')
         return redirect('cadastro')
      #Verifica se o usuario já tem cadastro através do campo email
      if User.objects.filter(email=email).exists():
         messages.error(request, 'Usuário já cadastrado')
         return redirect('cadastro')

      #Criando usuário
      user = User.objects.create_user(username=nome, email=email, password=senha)
      user.save()
      messages.success(request, 'Usuário cadastrado com sucesso!')
      return redirect('login')
   else:
      return render(request, 'usuarios/cadastro.html')


def login(request):
   if request.method == 'POST':
      email = request.POST['email']
      senha = request.POST['password']
      print(email, senha)
      if email == "" or senha == "":
         print("Os campos email e senha não podem ficar em branco")
         return redirect('login')
      if User.objects.filter(email=email).exists():
         #O Django por padrão faz login com o campo username, mas queremos fazer login com email.
         #Busca um objeto User através do email. Desse objeto retorno apenas o valor do username.
         #flat=True retorna valores únicos ao invés de uma tupla
         #https://stackoverflow.com/questions/37205793/django-values-list-vs-values
         nome = User.objects.filter(email=email).values_list('username', flat=True).get()
         print(nome)
         user = auth.authenticate(request, username=nome, password=senha)
         if user is not None:
            auth.login(request, user)
            print("Login realizado com sucesso!")
            return redirect('dashboard')
   return render(request, 'usuarios/login.html')

def logout(request):
   auth.logout(request)
   return redirect('receita.list')


class Dashboard(LoginRequiredMixin, ListView):
   model = Receita
   context_object_name = 'receitas'
   template_name = 'usuarios/dashboard.html'
   login_url = '/usuarios/login'

   def get_queryset(self):
      return self.request.user.receitas.all()


