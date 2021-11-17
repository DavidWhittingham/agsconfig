"""Tests for WPS server extensions."""

# Python 2/3 compatibility
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()

import pytest
from .helpers import geoprocessing_service_config as service_config

from agsconfig.services.wps_server_extension import WPSServerExtension as wps


@pytest.fixture(scope="function")
def service_extension(service_config):
    return service_config.wps_server


from .extension_base import *
from .custom_get_capabilities_mixin import *
from .ogc_metadata_extension_mixin import *


@pytest.mark.parametrize(
    ('attribute', 'expected_value', 'exception'),
    [
        ('britney_spears', 'should cause an', AttributeError),  # because she isn't a member
        ('app_schema_prefix', 'Test_TTool2', None),
        ('contact_instructions', None, None),
        ('enabled', False, None),
        ('hours_of_service', None, None),
        ('keywords_type', None, None),
        ('name', 'WPS', None),
        ('profile', None, None),
        ('provider_site', None, None),
        ('role', None, None),
        ('service_type', None, None),
        ('service_type_version', None, None)
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
        ('enabled', True, True, None),
        ('enabled', 'x', None, ValueError),
        ('hours_of_service', 'hours', 'hours', None),
        ('keywords_type', 'kt', 'kt', None),
        ('name', 'name', 'name', None),
        ('profile', 'pro', 'pro', None),
        ('provider_site', 'site', 'site', None),
        ('role', 'role', 'role', None),
        ('service_type', 'type', 'type', None),
        ('service_type_version', 'version', 'version', None)
    ]
)
def test_wps_setters(service_extension, attribute, new_value, expected_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(service_extension, attribute, new_value)
    else:
        setattr(service_extension, attribute, new_value)
        assert getattr(service_extension, attribute) == expected_value