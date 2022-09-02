from django.core.management.base import BaseCommand
from main.service import load_from_json


class Command(BaseCommand):
    help = 'Заполнить базу из файла'

    def handle(self, *args, **options):
        load_from_json()
