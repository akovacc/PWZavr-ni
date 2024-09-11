from django.test import TestCase, Client
from django.urls import reverse
from main.models import Author, News


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.homepage_url = reverse('homepage')
        self.news_q_url = reverse('news_q', args=['some-news'])

        self.news1 = News.objects.create(
            title = 'some-news',
            content = 'TestContent',
            publication_date = 'TestDate',
        )
        

    def test_project_homepage_GET(self):
        client = Client()

        response = client.get(self.homepage_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_project_news_GET(self):
        client = Client()

        response = client.get(self.news_q_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'news_list.html')
