from django import forms
from .models import FormData


class FormDataForm(forms.ModelForm):
    class Meta:
        model = FormData
        fields = [
            'kenteken',
            'kmstand',
            'postcode',
            'huisnummer',
            'straatnaam',
            'woonplaats',
            'emailaddress',
            'onderhoud',
            'werkzaamheden',
            'datum',
            'opmerkingen'
        ]