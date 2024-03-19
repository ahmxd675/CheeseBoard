import os
import re
import inspect
import tempfile
from CheeseBoardSite import models, forms
from populate_cheese import populate
from django.db import models
from django.test import TestCase
from django.conf import settings
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.forms import fields as django_fields

# Create your tests here.

# creating a user for testing
user = User.objects.create(username = "user", first_name = "first", last_name = "last", email = "abc@123.com")
user.set_password("PleaseDontFlagPasswordValidation123")
user.save()

# u might want to create a superuser not sure
