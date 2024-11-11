from django import forms
from ..models import Apartment


class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].empty_label = 'Выберете тип квартиры'
        self.fields['floor'].empty_label = 'Выберете этаж'
        self.fields['section'].empty_label = 'Выберете секцию'
        self.fields['building'].empty_label = 'Выберете корпус'