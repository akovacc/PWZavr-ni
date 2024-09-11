from django.test import TestCase
from main.models import Author, News


class Testmodels(TestCase):

    def setUp(self):
        self.news1 = News.objects.create(
            title = 'some-news',
            content = 'TestContent',
            publication_date = 'TestDate',
        )

    def test_news(self):
        self.assertEquals(self.news1.title, "some-news")
