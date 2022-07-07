from unittest import TestCase
from django.test import Client


class TestGetCompanies(TestCase):
    def test_zero_companies_should_return_empty_list(self)->None:
        client=Client()