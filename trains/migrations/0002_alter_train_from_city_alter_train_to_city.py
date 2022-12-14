# Generated by Django 4.1 on 2022-08-26 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('cities', '0001_initial'),
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='from_city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='from_city_set', to='cities.city', verbose_name='Из какого города'),
        ),
        migrations.AlterField(
            model_name='train',
            name='to_city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='to_city_set', to='cities.city', verbose_name='В какой город'),
        ),
    ]
