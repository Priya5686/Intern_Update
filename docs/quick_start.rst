Quick Start Guide
-----------------

Project Name
------------

This project is named *User Registration Management and schedule Events*

 - *User_API - project name
 - virtual environment names: myenv and

First you’ll need to have Django and django-registration installed;
for details on that, see the :doc:`installation guide`

Setting up URLs
---------------

Each bundled registration workflow in django-registration includes a
Django URLconf which sets up URL patterns for the views in django-registration.
The URLconf for the two-step activation workflow can be found at
django_registration.backends.activation.urls.

For example, to place the registration URLs under the prefix /accounts/,
you could add the following to your project’s root URLconf:

from django.urls import include, path

urlpatterns = [
path('accounts/', include('django_registration.backends.activation.urls')),
path('accounts/', include('django.contrib.auth.urls')),
# More URL patterns ...
]

Users would then be able to register by visiting the URL /accounts/register/,
log in (once activated) at /accounts/login/,etc.
The sample URL configuration above also sets up the built-in auth views included in
Django (login, logout, password reset, etc.) via the django.contrib.auth.urls URLconf

