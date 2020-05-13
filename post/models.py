from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.utils.text import slugify


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    models.DateTimeField('Created day', auto_now_add=True, blank=True)
    title = models.CharField('Title', max_length=200)
    content = models.TextField('Content')
    slug = models.SlugField('Slug')

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return '"%s" by %s' % (self.title, self.author)
