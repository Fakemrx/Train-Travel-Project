from django import forms
from trains.models import Train
from cities.models import City


class TrainForm(forms.ModelForm):
    name = forms.CharField(label='Поезд', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите название поезда',
    }))
    travel_time = forms.IntegerField(label='Время', widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите время в пути',
    }))
    from_city = forms.ModelChoiceField(label='Откуда', queryset=City.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control'}
        )
    )
    to_city = forms.ModelChoiceField(label='Куда', queryset=City.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = Train
        fields = '__all__'
