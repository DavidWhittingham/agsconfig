# coding=utf-8
"""Tests for feature server extension."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

# Third-party imports
import pytest

# Local imports
from .helpers import TRUEISH_TEST_PARAMS
from .helpers import map_service_config as service_config

@pytest.mark.parametrize(("allow_geometry_updates", "expected"), TRUEISH_TEST_PARAMS)
def test_allow_geometry_updates(service_config, allow_geometry_updates, expected):
    service_config.feature_server.allow_geometry_updates = allow_geometry_updates
    assert service_config.feature_server.allow_geometry_updates == expected

@pytest.mark.parametrize(("enabled", "expected"), TRUEISH_TEST_PARAMS)
def test_enabled(service_config, enabled, expected):
    service_config.feature_server.enabled = enabled
    assert service_config.feature_server.enabled == expected


@pytest.mark.parametrize(
    ('attribute', 'expected_value', 'exception'),
    [
        ('britney_spears', 'should cause an', AttributeError),  # because she isn't a member
        ('allow_others_to_delete', False, None),
        ('allow_others_to_query', True, None),
        ('allow_others_to_update', False, None),
        ('allow_true_curves_updates', False, None),
        ('enable_ownership_based_access_control', False, None),
        ('enable_z_defaults', False, None),
        ('max_record_count', 1000, None),
        ('realm', None, None),
        ('z_default_value', 0, None)
    ]
)
def test_getters(service_config, attribute, expected_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            assert getattr(service_config.feature_server, attribute) == expected_value
    else:
        assert getattr(service_config.feature_server, attribute) == expected_value


@pytest.mark.parametrize(
    ('attribute', 'new_value', 'exception'),
    [
        ('britney_spears', 'should cause a', TypeError),  # because she isn't a member
        ('allow_others_to_delete', True, None),
        ('allow_others_to_query', False, None),
        ('allow_others_to_update', True, None),
        ('allow_true_curves_updates', True, None),
        ('enable_ownership_based_access_control', True, None),
        ('enable_z_defaults', True, None),
        ('max_record_count', 100, None),
        ('realm', 'realm', None),
        ('z_default_value', 100, None)
    ]
)
def test_setters(service_config, attribute, new_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(service_config.feature_server, attribute, new_value)
            assert getattr(service_config.feature_server, attribute) == new_value
    else:
        setattr(service_config.feature_server, attribute, new_value)
        assert getattr(service_config.feature_server, attribute) == new_value