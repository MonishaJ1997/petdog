
from django import forms
from .models import OrderForm

class OrderFormModel(forms.ModelForm):
    class Meta:
        model = OrderForm
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email (for order updates)'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country/Region'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'apartment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apartment, suite (Optional)'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pincode'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'save_for_next': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'payment_method': forms.RadioSelect(attrs={'class': 'form-check-input'}),
        }

    # Example custom validation
    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if not phone.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        if len(phone) < 10:
            raise forms.ValidationError("Phone number must be at least 10 digits.")
        return phone

    def clean_pincode(self):
        pincode = self.cleaned_data.get("pincode")
        if not pincode.isdigit():
            raise forms.ValidationError("Pincode must be numeric.")
        if len(pincode) != 6:
            raise forms.ValidationError("Pincode must be exactly 6 digits.")
        return pincode
