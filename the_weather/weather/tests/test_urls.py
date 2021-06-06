from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import index, delete_city

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, index)

    def test_delete_city_url_is_resolved(self):
        url = reverse('delete_city', args=['Warszawa'])
        self.assertEquals(resolve(url).func, delete_city)