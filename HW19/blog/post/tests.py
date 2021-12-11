from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import *
from model_mommy import mommy

# Create your tests here.


class TestCategory(APITestCase):
    def setUp(self):
        mommy.make(Category)

    def test_category_list_rest(self):
        url = reverse('category')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        # self.assertEqual(len(resp.data), 10)
