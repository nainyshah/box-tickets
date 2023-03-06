""" Test for the city API"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import City

from city.serializers import CitySerializer

def create_city(user, **params):
    """Create and return a sample city."""
    defaults = {
        'name': 'Riyadh'
    }
    defaults.update(params)

    city = City.objects.create(user=user, **defaults)
    return city


def 