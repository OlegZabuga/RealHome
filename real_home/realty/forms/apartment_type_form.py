from django import forms
from ..models import ApartmentType


class ApartmentTypeForm(forms.ModelForm):
    class Meta:
        model = ApartmentType
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
