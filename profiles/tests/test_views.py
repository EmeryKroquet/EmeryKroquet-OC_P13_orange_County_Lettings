from django.test import TestCase
from django.urls import reverse
from faker import Faker
from django.contrib.auth.models import User
from .models import Profile


class TestProfilesView(TestCase):

    def setUp(self):
        self.fake = Faker()
        self.favorite_city = self.fake.city()
        self.user = User.objects.create(
            username=self.fake.name(),
            password=self.fake.password(),
            email=self.fake.email(),
        )

        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city=self.favorite_city
        )

    def test_profile_display(self):
        response = self.client.get(reverse("profiles:profile", args=[self.profile.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")
        self.assertContains(response, f"<title>{self.profile.user.username}</title>")

    def test_index(self):
        response = self.client.get(reverse("profiles:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/index.html")
        self.assertContains(response, "<title>Profiles</title>")
