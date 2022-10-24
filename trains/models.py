from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from cities.models import City


class Train(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Название поезда')
    travel_time = models.PositiveSmallIntegerField(verbose_name='Время в пути')
    from_city = models.ForeignKey(City, related_name='from_city_set',
                                  on_delete=models.CASCADE, verbose_name='Из какого города',
                                  null=True, blank=True
                                  )
    to_city = models.ForeignKey(City, related_name='to_city_set',
                                on_delete=models.CASCADE, verbose_name='В какой город',
                                null=True, blank=True
                                )

    def __str__(self):
        return f'Поезд №{self.name}. Едет из г. {self.from_city} в г. {self.to_city}'

    def clean(self):
        if self.from_city == self.to_city:
            raise ValidationError('Измените конечную точку назначения')
        qs = Train.objects.filter(travel_time=self.travel_time, from_city=self.from_city,
                                  to_city=self.to_city).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError('Измените время в пути')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('trains:detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Поезд'
        verbose_name_plural = 'Поезда'
        ordering = ['travel_time']
