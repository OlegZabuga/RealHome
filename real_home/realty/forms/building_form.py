from django import forms
from ..models import Building


class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['project'].empty_label = 'Выберите проект'