from django.contrib import admin
from .models import Receita, Categoria

admin.site.site_header = "Sistema Interno - Blog Receitas"
#admin.site.site_title = "Blog Receitas-ADMIN"
#admin.site.index_title = "Blog Receitas-ADMIN"

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
   list_display = ['id', 'nome_receita', 'tempo_preparo', 'user', 'publicada']
   list_display_links = ['id', 'nome_receita']
   list_editable = ['publicada']
   search_fields = ['nome_receita']
   list_filter = ['user']
   list_per_page = 10

   #campos editáveis no painel admin (na hora de criar iremos ter estes campos)
   fields = ['nome_receita', 'ingredientes', 'modo_preparo', 'tempo_preparo', 'rendimento', 'categoria', 'data_publicacao', 'data_modificacao', 'publicada', 'foto_receita', 'user']

   readonly_fields = ['data_publicacao', 'data_modificacao']
   
   #já deixa marcado o usuário que está logado no campo 'user'
   def get_changeform_initial_data(self, request):
      form = super(ReceitaAdmin, self).get_changeform_initial_data(request)
      form['user'] = request.user.pk
      return form


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
   list_display = ['tipo_categoria']
   list_filter = ['tipo_categoria']
   search_fields = ['tipo_categoria']
