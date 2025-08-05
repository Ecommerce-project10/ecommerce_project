from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    image= forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'quantity']
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        product = super().save(commit=False)
        if self.user:
            product.user = self.user
        if commit:
            product.save()
        return product