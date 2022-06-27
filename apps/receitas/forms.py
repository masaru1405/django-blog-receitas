from django import forms
from .models import Receita, Categoria

class ReceitaForm(forms.ModelForm):
   #Formato checkbox
   #categoria = forms.ModelChoiceField(queryset=Categoria.objects, empty_label=None, widget=forms.CheckboxSelectMultiple)

   class Meta:
      model = Receita
      fields = ['nome_receita', 'ingredientes', 'modo_preparo', 'tempo_preparo', 'rendimento', 'categoria', 'foto_receita', 'publicada']