from django.contrib.auth.models import Group
from django.test import TestCase

from .models import Post
from main.models import User


class TestPost(TestCase):
    def setUp(self):
        self.email = 'test@test.com'
        self.password = 'test'
        self.user_group = Group.objects.create(name='user')
        self.user = User.objects.create_user(self.email, self.password)

    def test_post_new(self):
        post = Post.objects.create(title='Test', content='TEST CONTENT', author=self.user)
        self.assertEqual(post.status, 1)
        self.assertEqual(post.slug, 'test')
