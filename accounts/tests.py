from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

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


class SignUpTest(TestCase):
    user_model = get_user_model()
    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_sign_up_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign up')
        self.assertNotContains(self.response, 'Hey boy!')

    def test_signup_form(self):
        new_user = self.user_model.objects.create_user(self.username, self.email)

        self.assertEqual(self.user_model.objects.all().count(), 1)
        self.assertEqual(self.user_model.objects.all()[0].username, self.username)
        self.assertEqual(self.user_model.objects.all()[0].email, self.email)
