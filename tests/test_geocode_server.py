"""Tests for Image services."""
# Python 2/3 compatibility
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()

import os.path
import agsconfig
from agsconfig.services.geocode_server import GeocodeServer

import pytest

SDDRAFT_FILE_PATH = os.path.abspath("{0}/samples/geocodeservice.sddraft".format(os.path.dirname(__file__)))

@pytest.fixture
def geocodeserver():
    return agsconfig.load_geocode_sddraft(open(SDDRAFT_FILE_PATH, 'rb+'))

def test_load_imagesddraft():
    """Load a vector tile into a map sddraft object."""
    sddraft = agsconfig.load_geocode_sddraft(open(SDDRAFT_FILE_PATH, 'rb+'))

    assert type(sddraft) == agsconfig.services.geocode_server.GeocodeServer


@pytest.mark.parametrize(
    ('attribute', 'expected_value', 'exception'),
    [
        ('britney_spears', 'should cause an', AttributeError), # because she isn't a member
        ('capabilities', [GeocodeServer.Capability.geocode,
                          GeocodeServer.Capability.reverse_geocode], None),
        ('name', 'NameOfGeocodeService', None),
        ('title', 'NameOfGeocodeService', None)
    ]
)
def test_getters(geocodeserver, attribute, expected_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            assert getattr(geocodeserver, attribute) == expected_value
    else:
        assert getattr(geocodeserver, attribute) == expected_value


@pytest.mark.parametrize(
    ('attribute', 'new_value', 'exception'),
    [
        ('britney_spears', 'should cause a', TypeError), # because she isn't a member
        ('capabilities', [GeocodeServer.Capability.geocode], None),
        ('name', 'AnotherName', None),
        ('title', 'AnotherTitle', None)
    ]
)
def test_setters(geocodeserver, attribute, new_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(geocodeserver, attribute, new_value)
            assert getattr(geocodeserver, attribute) == new_value
    else:
        setattr(geocodeserver, attribute, new_value)
        assert getattr(geocodeserver, attribute) == new_value
