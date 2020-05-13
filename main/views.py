from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from .models import User


def verify(request, uuid):
    try:
        user = User.objects.get(verification_uuid=uuid, is_verified=False)
    except User.DoesNotExist:
        raise Http404("User does not exist or is already verified")

    user.is_verified = True
    user.save()

    return HttpResponseRedirect(
        reverse('post:post_list_view')
    )
