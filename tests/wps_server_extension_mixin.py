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


@pytest.mark.parametrize( #yapf:disable
    ('attribute', 'expected_value', 'exception'),
    BASE_GETTER_TEST_CASES +
    OGC_GETTER_TEST_CASES +
    CUSTOM_GET_CAPABILITIES_GETTER_TEST_CASES +
    [
        ('app_schema_prefix', 'TestProject_TestService', None),
        ('contact_instructions', None, None),
        ('hours_of_service', None, None),
        ('name', 'WPS', None),
        ('provider_site', None, None),
        ('role', None, None),
        ('service_type_version', None, None),
        ('service_type', None, None)
    ]
) #yapf:enable
def test_wps_getters(service_config, attribute, expected_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            assert getattr(service_config.wps_server, attribute) == expected_value
    else:
        assert getattr(service_config.wps_server, attribute) == expected_value


@pytest.mark.parametrize( #yapf:disable
    ('attribute', 'new_value', 'expected_value', 'exception'),
    BASE_SETTER_TEST_CASES +
    OGC_SETTER_TEST_CASES +
    CUSTOM_GET_CAPABILITIES_SETTER_TEST_CASES +
    [
        ('app_schema_prefix', 'prefix', 'prefix', None),
        ('contact_instructions', 'instructions', 'instructions', None),
        ('hours_of_service', 'hours', 'hours', None),
        ('name', 'name', 'name', None),
        ('provider_site', 'site', 'site', None),
        ('role', 'role', 'role', None),
        ('service_type_version', 'version', 'version', None),
        ('service_type', 'type', 'type', None)
    ]
) #yapf:enable
def test_wps_setters(service_config, attribute, new_value, expected_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(service_config.wps_server, attribute, new_value)
    else:
        setattr(service_config.wps_server, attribute, new_value)
        assert getattr(service_config.wps_server, attribute) == expected_value