from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from .views import SignUpPageView
from .forms import CustomUserCreationForm


class CustomUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='test_user',
            email='test@email.com',
            password='test_pass'
        )

        self.assertEqual(user.username, 'test_user')
        self.assertEqual(user.email, 'test@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='test_admin',
            email='test_admin@email.com',
            password='test_admin_pass'
        )

        self.assertEqual(admin_user.username, 'test_admin')
        self.assertEqual(admin_user.email, 'test_admin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignUpTestPage(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_sign_up_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Sign up')
        self.assertNotContains(self.response, 'Hey boy!')

    def test_signup_form(self):
        form = self.response.context.get('form')

        self.assertIsInstance(form, CustomUserCreationForm)

    def test_signup_view(self):
        view = resolve('/accounts/signup/')

        self.assertEqual(view.func.__name__, SignUpPageView.as_view().__name__)
