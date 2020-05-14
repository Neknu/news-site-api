import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group
from django.db.models import signals

from .tasks import send_verification_email


class UserAccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email address must be provided')

        if not password:
            raise ValueError('Password must be provided')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = UserAccountManager()

    email = models.EmailField('email', unique=True, blank=False, null=False)
    full_name = models.CharField('full name', blank=True, null=True, max_length=400)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)
    is_verified = models.BooleanField('verified', default=False)
    verification_uuid = models.UUIDField('Unique Verification UUID', default=uuid.uuid4)
    birthday = models.DateField('birthday', blank=True, null=True)

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.email

    def __unicode__(self):
        return self.email


# def user_post_save(sender, instance, signal, *args, **kwargs):
#     if not instance.is_verified:
#         send_mail(
#             'Verify account at News Site',
#             'Follow this link to verify your account: '
#             'http://localhost:8000%s' % reverse('verify', kwargs={'uuid': str(instance.verification_uuid)}),
#             'from@quickpublisher.dev',
#             [instance.email],
#             fail_silently=False,
#         )


def user_post_save(sender, instance, signal, created, *args, **kwargs):
    if not instance.is_verified:
        # Send verification email
        # send_verification_email.delay(instance.pk)
        # mailgun is working strange and block my account, but before that I have tested all and it was working
        pass

    if created:
        instance.groups.add(Group.objects.get(name='user'))


signals.post_save.connect(user_post_save, sender=User)
