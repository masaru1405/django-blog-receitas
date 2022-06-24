from django import forms
from .models import Receita

class ReceitaForm(forms.ModelForm):
   class Meta:
      model = Receita
      fields = ['nome_receita', 'ingredientes', 'modo_preparo', 'tempo_preparo', 'rendimento', 'categoria', 'foto_receita', 'publicada']