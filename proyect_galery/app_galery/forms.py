from django import forms
from . models import Pictures_product

class PictureForm(forms.ModelForm):
    class Meta:
        model = Pictures_product
        fields = ['id', 'nombre', 'description', 'precio', 'imagen']
    
    nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}), max_length=50)
    description = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}), max_length=100)
    precio = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control"}), max_digits=5, decimal_places=2)
    imagen = forms.ImageField(label="Avatar", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))
    