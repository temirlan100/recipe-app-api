from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@test.com', password='test_pass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email successful"""
        email = "test@test.com"
        password = "Testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user normalized"""
        email = "test@TEST.com"
        user = get_user_model().objects.create_user(email, "test123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user without email and raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            "test@test.com",
            "test123"
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
