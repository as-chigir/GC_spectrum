from django.test import TestCase


class TestPage(TestCase):
    def test_main_page_works(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertContains(response, 'Главная страница')

    def test_about_page_works(self):
        response = self.client.get('/about/')
        self.assertContains(response, 'Контактные данные')
