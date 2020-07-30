from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class UpdateForm(UserChangeForm):

	#only want user to be able to update username and email
	email = forms.EmailField()
	password = None
	class Meta:
		model = User
		fields = ['username', 'email']