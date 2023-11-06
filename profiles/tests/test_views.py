from django.urls import reverse


def test_profiles_index_view(self):
    response = self.client.get(reverse('profiles_index'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'profiles/profiles_index.html')


def test_profile_view(self):
    response = self.client.get(reverse('profile', args=[self.profile.user.username]))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'profiles/profile.html')
