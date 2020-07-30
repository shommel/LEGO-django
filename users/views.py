from django.shortcuts import render
from .forms import RegistrationForm, UpdateForm
from django.contrib.auth.models import User

def register(request):
	#registering a new user
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = RegistrationForm()

	context = {'form': form}
	return render(request, 'users/register.html', context)


def update(request, id):
	#updating a user's info with corresponding id 
	user = User.objects.get(id=id)

	if request.method == "POST":
		form = UpdateForm(request.POST, instance=user)
		if form.is_valid():
			form.save()
	else:
		form = UpdateForm(instance=user)

	context = {'form' : form}
	return render(request, 'users/edit.html', context)


def delete(request, id):
	#deleting a user with corresponding id 
	user = User.objects.get(id=id)
	user.delete()

	return render(request, 'users/deleted.html', {})


	