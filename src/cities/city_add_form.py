from django.forms import ModelForm
from .models import City


class CityAddForm(ModelForm):
    class Meta:
        model = City
        fields = [
            'name',
        ]
