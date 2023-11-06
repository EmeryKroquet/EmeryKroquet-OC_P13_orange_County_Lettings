from django.test import TestCase
from django.contrib.auth.models import User
from .models import Address, Letting, Profile
# from oc_lettings_site.models import Address, Letting, Profile
from faker import Faker
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.fake = Faker()

        # Créez un objet Address
        self.address = Address.objects.create(
            number=self.fake.random_int(min=1, max=9999),
            street=self.fake.street_name(),
            city=self.fake.city(),
            state=self.fake.state_abbr(),
            zip_code=self.fake.random_int(min=10000, max=99999),
            country_iso_code=self.fake.country_code()
        )

        # Créez un objet Letting associé à l'objet Address créé ci-dessus
        self.letting = Letting.objects.create(
            title=self.fake.name(),
            address=self.address
        )

        # Créez un objet User
        self.user = User.objects.create_user(
            username=self.fake.user_name(),
            password=self.fake.password()
        )

        # Créez un objet Profile associé à l'utilisateur
        self.profile = Profile.objects.create(user=self.user, favorite_city=self.fake.city())

    def test_lettings_index_view(self):
        response = self.client.get(reverse('lettings_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/lettings_index.html')

    def test_letting_view(self):
        response = self.client.get(reverse('letting', args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')

    def test_profiles_index_view(self):
        response = self.client.get(reverse('profiles_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profiles_index.html')

    def test_profile_view(self):
        response = self.client.get(reverse('profile', args=[self.profile.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
