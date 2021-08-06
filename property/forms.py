from django import forms

from .models import PropertyBook


class PropertyBookForm(forms.ModelForm):
    date_from = forms.DateField(
        widget=forms.DateInput(attrs={'id': 'checkin_date', 'autocomplete': 'off'}))
    date_to = forms.DateField(
        widget=forms.DateInput(attrs={'id': 'checkin_date', 'autocomplete': 'off'}))

    class Meta:
        model = PropertyBook
        fields = ['date_from', 'date_to', 'guest', 'children']
