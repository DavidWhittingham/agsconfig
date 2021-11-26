"""Tests for Geocode services."""
# Python 2/3 compatibility
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()

import os.path
import agsconfig
from agsconfig.services.geocode_server import GeocodeServer

import pytest

from .helpers import geocode_service_config as service_config
from .service_base_mixin import *


def test_load_geocode_service(service_config):
    # this just tests the fixture setup
    assert True


@pytest.mark.parametrize(
    ('attribute', 'expected_value', 'exception'), [
        ('capabilities', [GeocodeServer.Capability.geocode, GeocodeServer.Capability.reverse_geocode], None),
        ('name', 'NameOfGeocodeService', None), ('title', 'NameOfGeocodeService', None)
    ]
)
def test_geocode_getters(service_config, attribute, expected_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            assert getattr(service_config, attribute) == expected_value
    else:
        assert getattr(service_config, attribute) == expected_value


@pytest.mark.parametrize(
    ('attribute', 'new_value', 'exception'), [
        ('capabilities', [GeocodeServer.Capability.geocode], None), ('name', 'AnotherName', None),
        ('title', 'AnotherTitle', None)
    ]
)
def test_geocode_setters(service_config, attribute, new_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(service_config, attribute, new_value)
            assert getattr(service_config, attribute) == new_value
    else:
        setattr(service_config, attribute, new_value)
        assert getattr(service_config, attribute) == new_value
