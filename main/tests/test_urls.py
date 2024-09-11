from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import homepage, NewsList, AuthorsList, HomePageView


class TestUrls(SimpleTestCase):

    def test_homepage_url_is_resolved(self):
        url = reverse('homepage')
        # print(resolve(url))

        self.assertEquals(resolve(url).func, homepage)

    def test_books_url_is_resolved(self):
        url = reverse('news')

        self.assertEquals(resolve(url).func.view_class, NewsList)

    def test_authors_url_is_resolved(self):
        url = reverse('authors')

        self.assertEquals(resolve(url).func.view_class, AuthorsList)
