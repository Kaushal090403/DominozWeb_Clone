from django import forms
from .models import OrderModel, ToppingModel

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = ['Order_Number', 'Pizza', 'Pizza_size', 'Toppings']
        widgets = {
            'Toppings': forms.CheckboxSelectMultiple(attrs={'class': 'form-checkbox'}),
        }

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['Toppings'].queryset = ToppingModel.objects.all()
        self.fields['Toppings'].label = "Choose your toppings"
        self.fields['Toppings'].help_text = "Select one or more toppings for your pizza."

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-input w-full border border-gray-300 rounded-md py-2 px-3 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Enter your name'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-input w-full border border-gray-300 rounded-md py-2 px-3 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Enter your email'
        })
    )
    subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-input w-full border border-gray-300 rounded-md py-2 px-3 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Subject'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-input w-full border border-gray-300 rounded-md py-2 px-3 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Your message'
        })
    )

class PizzaOrderForm(forms.Form):
    toppings = forms.ModelMultipleChoiceField(
        queryset=ToppingModel.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-checkbox'
        })
    )
