import os
import shutil
from unittest.mock import Mock, patch
import datetime

from django.core.exceptions import ValidationError
from django.conf import settings
from django.test import TestCase
from django.contrib.auth import get_user_model

from employees.forms import UserForm


class UserFormTests(TestCase):
  fixtures = ['tock/fixtures/dev_user.json']

  def test_user_update(self):
    form_data = {'email': 'testuser@gsa.gov', 'first_name': 'Test'}
    form = UserForm(form_data)
    self.assertTrue(form.is_valid())
    self.assertEqual(form.cleaned_data['email'], "testuser@gsa.gov")
    self.assertEqual(form.cleaned_data['first_name'], "Test")

  def test_date_validation(self):
  	form_data = {'email': 'testuser@gsa.gov', 'end_date': '2015-01-01'}
  	form = UserForm(form_data)
  	self.assertFalse(form.is_valid())

  	form_data = {'email': 'testuser@gsa.gov', 'start_date': '2015-02-01', 'end_date': '2015-01-01'}
  	form = UserForm(form_data)
  	self.assertFalse(form.is_valid())

  	form_data = {'email': 'testuser@gsa.gov', 'start_date': '2015-01-01', 'end_date': '2015-05-05'}
  	form = UserForm(form_data)
  	self.assertTrue(form.is_valid())