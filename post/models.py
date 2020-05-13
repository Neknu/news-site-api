from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

from tinymce import models as tinymce_models

from .utils import get_unique_slug


STATUS_CHOICES = (
    (1, "On review"),
    (2, "Approved"),
    (3, "Declined"),
)


class Post(models.Model):
    title = models.CharField('Title', max_length=200)
    content = tinymce_models.HTMLField('Content')
    slug = models.SlugField('Slug')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    models.DateTimeField('Created day', auto_now_add=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    # is_approved = models.BooleanField('Is post published?', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)

    def __str__(self):
        return '"%s" by %s' % (self.title, self.author)
