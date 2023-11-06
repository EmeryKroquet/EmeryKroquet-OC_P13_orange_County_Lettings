from django.urls import reverse


def test_index_view(self):
    response = self.client.get(reverse('index'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'home/index.html')
