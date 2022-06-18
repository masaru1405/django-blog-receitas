from django.contrib import admin
from .models import Receita, Categoria

admin.site.site_header = "Sistema Interno - Blog Receitas"
#admin.site.site_title = "Blog Receitas-ADMIN"
#admin.site.index_title = "Blog Receitas-ADMIN"

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
   list_display = ['id', 'nome_receita', 'tempo_preparo', 'pessoa', 'publicada']
   list_display_links = ['id', 'nome_receita']
   list_editable = ['publicada']
   search_fields = ['nome_receita']
   #list_filter = ['categoria']
   list_per_page = 5


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
   list_display = ['tipo_categoria']
   list_filter = ['tipo_categoria']
   search_fields = ['tipo_categoria']
