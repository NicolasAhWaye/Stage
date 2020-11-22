from django import forms


class ContactForm(forms.Form):
    GTIN = forms.CharField(
        label='GTIN',
        max_length=14,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    Date = forms.DateField(
        label='Date',
        widget=forms.DateInput(attrs={'class': 'form-control'}),
        required=True)
