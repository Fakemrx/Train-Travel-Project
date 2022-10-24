from django.db import models
from django.urls import reverse


class City(models.Model):
    name = models.CharField(max_length=40, unique=True, verbose_name='Название города')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['name', ]

    # def get_absolute_url(self):
    #     return reverse('cities:home', kwargs={'pk': self.pk})
