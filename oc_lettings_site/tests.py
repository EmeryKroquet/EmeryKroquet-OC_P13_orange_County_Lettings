from django.test import TestCase
from django.urls import reverse
from faker import Faker

from .models import Address, Letting


class TestLettingsView(TestCase):

    def setUp(self):
        self.fake = Faker()
        self.address = Address.objects.create(
            number=self.fake.building_number(),
            street=self.fake.street_name(),
            city=self.fake.city(),
            state=self.fake.country(),
            zip_code=self.fake.postcode(),
            country_iso_code=self.fake.country_code()
        )

        self.letting = Letting.objects.create(
            title=self.fake.name(),
            address=self.address
        )

    def test_letting_display(self):

        response = self.client.get(reverse("lettings:letting", args=[self.letting.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/letting.html")
        self.assertContains(response, f"<title>{self.letting.title}</title>")

    def test_index(self):
        response = self.client.get(reverse("lettings:index"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/index.html")
        self.assertContains(response, "<title>Lettings</title>")
