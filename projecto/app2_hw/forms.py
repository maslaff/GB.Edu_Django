from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(initial="Name", max_length=100)
    description = forms.CharField(initial="Description", widget=forms.Textarea)
    price = forms.DecimalField(initial=0, max_digits=8, decimal_places=2)
    quantity = forms.IntegerField(initial=0)
    img = forms.ImageField()
