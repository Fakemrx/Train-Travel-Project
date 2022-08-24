from django import forms
from .models import Train


class TrainForm(forms.ModelForm):
    name = forms.CharField(label='Поезд', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите название поезда',
    }))
    travel_time = forms.IntegerField(label='Время', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите время в пути',
    }))
    from_city = forms.ChoiceField(label='Город', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Выберите начальный город',
    }))
    to_city = forms.ChoiceField(label='Город', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Выберите конечный город',
    }))

    class Meta:
        model = Train
        fields = [
            'name',
            'travel_time',
            'from_city',
            'to_city'
        ]
