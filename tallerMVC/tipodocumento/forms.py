from django import forms
from .models import td

class tdForm(forms.ModelForm):

    class Meta:
         model = td

         fields = [
              'nombre',
              'descripcion'
         ]
         labels = {
              'nombre':'Nombre',
              'descripcion':'Descripción',
         }
         widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','required':''}),
            'descripcion': forms.TextInput(attrs={'class':'form-control','required':''}),
        
         }
