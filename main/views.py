from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from .forms import RegisterForm

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


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:user_login'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = RegisterForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.is_staff = False
            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = RegisterForm()

    return render(request, 'main/registration.html',
                  {'user_form': user_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            if user.is_active and user.is_verified:
                login(request, user)
                return HttpResponseRedirect(reverse('post:post_list_view'))
            else:
                return HttpResponse("Please Verify your account. We send verification url to your email.")
        else:
            print("Someone tried to login and failed.")
            print("They used email: {} and password: {}".format(email, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'main/login.html', {})
