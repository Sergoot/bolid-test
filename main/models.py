from django.db import models


class Sensor(models.Model):
    """ Модель датчика """
    name = models.CharField('Имя датчика', max_length=256)
    type = models.SmallIntegerField('Тип датчика')
    num = models.SmallIntegerField('Порядковый номер', unique=True)
    temperature = models.SmallIntegerField('Рабочая температура', null=True)
    humidity = models.SmallIntegerField('Влажность', null=True)

    def __str__(self):
        return f"Датчик №{self.num} {self.name}, тип: {self.type}"

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
        db_table = 'sensors'
        ordering = ('num',)

