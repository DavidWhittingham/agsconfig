"""Tests for WPS server extensions."""

# Python 2/3 compatibility
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()

import pytest
from .helpers import geoprocessing_service_config as service_config

from agsconfig.services.wps_server_extension import WPSServerExtension as wps

@pytest.fixture(scope = "function")
def service_extension(service_config):
    return service_config.wps_server

@pytest.mark.parametrize(
    ('attribute', 'expected_value', 'exception'),
    [
        ('britney_spears', 'should cause an', AttributeError),  # because she isn't a member
        ('abstract', None, None),
        ('access_constraints', None, None),
        ('address', None, None),
        ('administrative_area', None, None),
        ('app_schema_prefix', 'Test_TTool2', None),
        ('city', None, None),
        ('contact_instructions', None, None),
        ('country', None, None),
        ('custom_get_capabilities', False, None),
        ('email', None, None),
        ('enabled', False, None),
        ('facsimile', None, None),
        ('fee', None, None),
        ('hours_of_service', None, None),
        ('individual_name', None, None),
        ('keyword', None, None),
        ('keywords_type', None, None),
        ('name', 'WPS', None),
        ('path_to_custom_get_capabilities_files', None, None),
        ('phone', None, None),
        ('position_name', None, None),
        ('postal_code', None, None),
        ('profile', None, None),
        ('provider_site', None, None),
        ('role', None, None),
        ('service_type', None, None),
        ('service_type_version', None, None),
        ('title', None, None)
    ]
)
def test_wfs_getters(service_extension, attribute, expected_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            assert getattr(service_extension, attribute) == expected_value
    else:
        assert getattr(service_extension, attribute) == expected_value


@pytest.mark.parametrize(
    ('attribute', 'new_value', 'expected_value', 'exception'),
    [
        ('britney_spears', 'should cause a', None, TypeError),  # because she isn't a member
        ('abstract', 'abstract', 'abstract', None),
        ('access_constraints', 'ac', 'ac', None),
        ('administrative_area', 'admin', 'admin', None),
        ('app_schema_prefix', 'prefix', 'prefix', None),
        ('city', 'city', 'city', None),
        ('contact_instructions', 'instructions', 'instructions', None),
        ('country', 'country', 'country', None),
        ('custom_get_capabilities', True, True, None),
        ('custom_get_capabilities', 'x', None, ValueError),
        ('email', 'email', 'email', None),
        ('enabled', True, True, None),
        ('enabled', 'x', None, ValueError),
        ('facsimile', 'fax', 'fax', None),
        ('fee', 'fees', 'fees', None),
        ('hours_of_service', 'hours', 'hours', None),
        ('individual_name', 'individual', 'individual', None),
        ('keyword', 'kw', 'kw', None),
        ('keywords_type', 'kt', 'kt', None),
        ('name', 'name', 'name', None),
        ('path_to_custom_get_capabilities_files', 'a:/path', 'a:/path', None),
        ('phone', 'phone', 'phone', None),
        ('position_name', 'pname', 'pname', None),
        ('postal_code', 'postcode', 'postcode', None),
        ('profile', 'pro', 'pro', None),
        ('provider_site', 'site', 'site', None),
        ('role', 'role', 'role', None),
        ('service_type', 'type', 'type', None),
        ('service_type_version', 'version', 'version', None),
        ('title', 'title', 'title', None)
    ]
)
def test_wfs_setters(service_extension, attribute, new_value, expected_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(service_extension, attribute, new_value)
    else:
        setattr(service_extension, attribute, new_value)
        assert getattr(service_extension, attribute) == expected_value