from django import forms

from .models import User

YEARS= [x for x in range(1930, 2020)]


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    birthday = forms.DateField(initial="2000-01-01", widget=forms.SelectDateWidget(years=YEARS))

    class Meta:
        model = User
        fields = ('email', 'password', 'full_name', 'birthday')
