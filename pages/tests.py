from django.test import SimpleTestCase
from django.urls import resolve, reverse

from .views import HomePageView, AboutPageView


class HomepageTest(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'HomePage')

    def test_homepage_contains_not_correct_html(self):
        self.assertNotContains(self.response, 'Hey boy!')

    def test_homepage_url_resolves_homepage_view(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTest(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'About Page')

    def test_aboutpage_contains_not_correct_html(self):
        self.assertNotContains(self.response, 'Hey boy!')

    def test_aboutpage_url_resolves_aboutpage_view(self):
        view = resolve('/about/')
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)
