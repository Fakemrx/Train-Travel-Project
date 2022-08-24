from django.db import models
# from src.cities.models import City


class Train(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Название поезда')
    travel_time = models.PositiveSmallIntegerField(verbose_name='Время в пути')
    from_city = models.ForeignKey('cities.City', related_name='from_city_set',
                                  on_delete=models.CASCADE
                                  )
    to_city = models.ForeignKey('cities.City', related_name='to_city_set',
                                on_delete=models.CASCADE
                                )

    def __str__(self):
        return f'Поезд №{self.name} отправляется из {self.from_city} в {self.to_city}.'

    class Meta:
        verbose_name = 'Поезд'
        verbose_name_plural = 'Поезда'
        ordering = ['travel_time']
