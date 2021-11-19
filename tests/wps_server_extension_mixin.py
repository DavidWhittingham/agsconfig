"""Tests for WPS server extensions."""

# Python 2/3 compatibility
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()

import pytest

from agsconfig.services.wps_server_extension import WPSServerExtension as wps

from .custom_get_capabilities_mixin import *
from .extension_base import *
from .ogc_metadata_extension_mixin import *


# facilitates OGC extension testing
@pytest.fixture(scope="function")
def service_extension(service_config):
    return service_config.wps_server


@pytest.mark.parametrize(
    ('attribute', 'expected_value', 'exception'),
    [
        ('britney_spears', 'should cause an', AttributeError),  # because she isn't a member
        ('app_schema_prefix', 'TestProject_TestService', None),
        ('contact_instructions', None, None),
        ('hours_of_service', None, None),
        ('name', 'WPS', None),
        ('provider_site', None, None),
        ('role', None, None),
        ('service_type_version', None, None),
        ('service_type', None, None)
    ]
)
def test_wps_getters(service_extension, attribute, expected_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            assert getattr(service_extension, attribute) == expected_value
    else:
        assert getattr(service_extension, attribute) == expected_value


@pytest.mark.parametrize(
    ('attribute', 'new_value', 'expected_value', 'exception'),
    [
        ('britney_spears', 'should cause a', None, TypeError),  # because she isn't a member
        ('app_schema_prefix', 'prefix', 'prefix', None),
        ('contact_instructions', 'instructions', 'instructions', None),
        ('hours_of_service', 'hours', 'hours', None),
        ('name', 'name', 'name', None),
        ('provider_site', 'site', 'site', None),
        ('role', 'role', 'role', None),
        ('service_type_version', 'version', 'version', None),
        ('service_type', 'type', 'type', None)
    ]
)
def test_wps_setters(service_extension, attribute, new_value, expected_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(service_extension, attribute, new_value)
    else:
        setattr(service_extension, attribute, new_value)
        assert getattr(service_extension, attribute) == expected_value