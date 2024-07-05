from django import forms
from .models import VidaSaludable



class VidaSaludableForm(forms.ModelForm):
    class Meta:
        model = VidaSaludable
        fields = '__all__'
        
