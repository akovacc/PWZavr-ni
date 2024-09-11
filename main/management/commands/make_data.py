import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import News, Author, Category
from main.factories import (
    AuthorFactory,
    CategoryFactory,
    NewsFactory
)

NUM_AUTHORS = 12
NUM_CATEGORIES = 6
NUM_NEWS = 22


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Author, News, Category]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_AUTHORS):
            author = AuthorFactory()

        for _ in range(NUM_CATEGORIES):
            category = CategoryFactory()
            
        for _ in range(NUM_NEWS):
            news = NewsFactory()
