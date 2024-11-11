from django import forms
from ..models import Floor


class FloorForm(forms.ModelForm):
    class Meta:
        model = Floor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['section'].empty_label = 'Выберите секцию'
