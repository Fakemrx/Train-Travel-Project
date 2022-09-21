from django import forms
from cities.models import City
from routes.models import Route


class RouteForm(forms.Form):
    from_city = forms.ModelChoiceField(label='Откуда', queryset=City.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control js-single-picker'}
    ))
    to_city = forms.ModelChoiceField(label='Куда', queryset=City.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control js-single-picker'}
    ))
    cities = forms.ModelMultipleChoiceField(label='Через города', queryset=City.objects.all(),
                                            required=False, widget=forms.SelectMultiple(
            attrs={'class': 'form-control js-multi-picker'}
        ))
    travelling_time = forms.IntegerField(label='Общ. время', required=False,
                                         widget=forms.NumberInput(attrs={
                                             'class': 'form-control',
                                             'placeholder': 'Введите время в пути',
                                         }
                                         ))
