from typing import Text
from django import forms
from django.shortcuts import get_object_or_404
from menu.models import *

### CLASSIFICAÇAO DOS ITENS
class FormClassificacoes(forms.ModelForm):
    class Meta:
        model = Classificacoes
        fields = ['nome_classificacao']
        labels = {'nome_classificacao':('Ex: Petiscos ')}
class FormClassificacao(forms.ModelForm):
    class Meta:
        model = Item_classificacao
        fields = ['text','classificacao']
        labels = {'text':('Categoria: '),'classificacao':('Classificação: ')}
        help_texts = {'text': ('Ex: Petiscos')}
        
### ITENS
class FormItens(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ['item_nome','classificacao','descricao','preco','img']
        labels = {'item_nome':('Nome do item: '), 'classificacao':('Classificação: '),'descricao':('Descrição:'),'preco':('Preco:'),'img':('Imagem do produto')}
    
## FORMULÁRIO PARA EDIÇAO DE ITENS  
class FormEditItens(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ['item_nome','classificacao','descricao','preco','img']
        labels = {'item_nome':('Nome do item: '), 'classificacao':('Classificação: '),'descricao':('Descrição:'),'preco':('Preco:'),'img':('Imagem do produto')}
     
    


        

        