from django.contrib.auth.models import Group
from django.test import TestCase
from django.contrib.auth import authenticate

from .models import User


class TestUser(TestCase):
    def setUp(self):
        self.email = 'test@test.com'
        self.password = 'test'
        self.user_group = Group.objects.create(name='user')
        self.user = User.objects.create_user(self.email, self.password)

    def test_user_registration(self):
        self.assertTrue(self.user.groups.filter(name=self.user_group).exists())

    def test_user_login(self):
        login_user = authenticate(email=self.email, password=self.password)
        self.assertTrue(login_user.is_active)
        self.assertFalse(login_user.is_verified)
