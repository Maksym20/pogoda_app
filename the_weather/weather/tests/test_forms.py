from django.test import SimpleTestCase
from ..forms import CityForm


class TestForms(SimpleTestCase):
    
    def test_city_form_no_data(self):
        form = CityForm()
        self.assertFalse(form.is_valid())