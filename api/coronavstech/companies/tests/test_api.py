import json
from unittest import TestCase

import pytest
from django.test import Client
from django.urls import reverse

from api.coronavstech.companies.models import Company


@pytest.mark.django_db
class BasicCompanyAPITestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()  #using a client to send a request to our django server
        self.companies_url = reverse("companies-list")

    def tearDown(self) -> None:
        pass


class TestGetCompanies(BasicCompanyAPITestCase):
    def setUp(self) -> None:
            self.client = Client()
            self.companies_url = reverse("companies-list")

    def tearDown(self) -> None:
        pass

    def test_zero_companies_should_return_empty_lists(self) -> None:
        response = self.client.get(self.companies_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), [])

    def test_one_company_exists_should_succeed(self) -> None:
        test_company= Company.objects.create(name="Amazon")
        companies_url = reverse("companies-list")
        response = self.client.get(companies_url)
        response_content = json.loads(response.content)[0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content.get("name"), "Amazon")
        self.assertEqual(response_content.get("status"), "Hiring")
        self.assertEqual(response_content.get("application_link"), "")
        self.assertEqual(response_content.get("notes"), "")

        test_company.delete()


class TestPostCompanies(BasicCompanyAPITestCase):
    def test_create_company_without_arguments_should_fail(self) -> None:
        response = self.client.post(path=self.companies_url)
        self.assertEqual(response.status_code, 400)
