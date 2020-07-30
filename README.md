# django-test

## Description
This repo consists of a quick mock up of a LEGO set review blog site built on Django. This is my first project using Django, so some optimizations can be made, but I tried to timebox it to a few hours of watching videos/reading documentation. 

## What can you do?
Currently, the site has the following functionalities:
* Register for an account
* Login with said account information
* Update account info
* Delete an account
* Post a blog entry about a LEGO Set
* View posts by other users
* Page redirection if access to a page is not permitted

More to come...

## Setup 
git clone the repo into the directory of your choice. With most Python projects, setting up a virtualenv is recommended. This helps containerize the project and not install unneccessary packages on your system's python.  

### Installation with virtualenv

Below are the instructions for installing the django app using virtualenv. 

```
cd LEGO-django
virtualenv venv/
source venv/bin/activate
pip3 install -r requirements.txt
```

Assuming no issues with the above commands, you should have your virtualenv set up and the necessary packages installed. 

### Initiating the Django-DB

Before we can launch the site, we have to setup the django-db that will house our data.

```
python3 manage.py makemigrations
python3 manage.py migrate
``` 

### Optional: Creating a Superuser

django gives us the ability to create a ```superuser``` to access some of the builtin admin features in the django backend.
To create a ```superuser``` account, use the following instructions:

```
python3 manage.py createsuperuser
```

Follow the prompts on screen to fill in the username, email, and password. 

## Running

To run the django app, follow the below instructions:

```
source venv/bin/activate
python3 manage.py runserver
```

This should launch the virtualenv along with spinning up the django app on ```localhost:8000```. 
Launch your web browser and go to that address, and you should be greeted with the login screen for the app. 

### Accessing Admin Page

If you need to access the django-admin backend, simply go to ```localhost:8000/admin``` and login with your ```superuser``` account information from before. 