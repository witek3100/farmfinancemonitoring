from datetime import date

from django import forms
from .models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'date', 'category', 'cost', 'type', 'invoice_number',
            'flock', 'amount', 'unit_price', 'water_usage', 'forage_type', 'payment_deadline', 'drug_name'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'category': forms.Select(attrs={'id': 'category-select'}),
        }
        labels = {
            'Data wystawienia faktury', 'Koszt', 'Typ (Koszt/Przychód)', 'Numer faktury',
            'Kategoria', 'Rzut', 'Ilość', 'Cena jednostkowa', 'Zużycie wody', 'Rodzaj Paszy', 'Termin zapłaty'
        }

    def __init__(self, *args, **kwargs):
        super(InvoiceForm, self).__init__(*args, **kwargs)

        today = date.today().strftime('%Y-%m-%d')
        self.fields['date'].widget.attrs.update({'placeholder': today})

        self.fields['amount'].required = False
        self.fields['unit_price'].required = False
        self.fields['water_usage'].required = False
        self.fields['payment_deadline'].required = False
        self.fields['forage_type'].required = False
        self.fields['drug_name'].required = False
        self.fields['unit_price'].required = False


