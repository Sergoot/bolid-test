import json
from typing import Any

from .models import Sensor

from django.db.models.base import Model
from django.db.models import QuerySet


def load_from_json() -> None:
    """ Сохраняет в базу данных записи из json файла """
    with open('../bolid/data.json', 'r') as f:
        data = f.read()
    data = json.loads(data)
    for censor_data in data:
        num = censor_data.get('num')
        if not Sensor.objects.filter(num=num).exists():
            Sensor.objects.create(
                num=num,
                type=censor_data.get('Sensor_type'),
                name=censor_data.get('name'),
                temperature=censor_data.get('temperature'),
                humidity=censor_data.get('humidity')
            )


def get_all_or_filter(model: Model, **filters: Any) -> QuerySet:
    """ Возвращает QuerySet со всеми атрибутами модели или отфильтрованными по фильтрам атрибутами """
    return model.objects.filter(**filters) if filters else model.objects.all()
