# coding=utf-8
"""Tests for feature server extension."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

# Third-party imports
import pytest

# Local imports
from .helpers import TRUEISH_TEST_PARAMS

# import additional fixtures
from .extension_base import *


@pytest.mark.parametrize(#yapf:disable
    ('attribute', 'expected_value', 'exception'),
    BASE_GETTER_TEST_CASES +
    [
        ('allow_geometry_updates', True, None),
        ('allow_others_to_delete', False, None),
        ('allow_others_to_query', True, None),
        ('allow_others_to_update', False, None),
        ('set_defaults_to_null_for_not_null_fields_in_templates', False, None),
        ('allow_true_curves_updates', False, None),
        ('enable_ownership_based_access_control', False, None),
        ('enable_z_defaults', False, None),
        ('realm', None, None),
        ('z_default_value', 0, None)
    ]
)#yapf:enable
def test_feature_server_getters(service_config, attribute, expected_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            assert getattr(service_config.feature_server, attribute) == expected_value
    else:
        assert getattr(service_config.feature_server, attribute) == expected_value


@pytest.mark.parametrize(#yapf:disable
    ('attribute', 'new_value', 'expected_value', 'exception'),
    BASE_SETTER_TEST_CASES +
    [
        ('realm', 'testRealm', 'testRealm', None),
        ('z_default_value', 100, 100, None),
        ('z_default_value', '200', 200, None),
        ('z_default_value', 'xyz', None, ValueError),
        ('z_default_value', 128.234569871, 128.234569871, None)
    ] + [
        ("allow_geometry_updates", trueish_value, trueish_expected, None)
        for (trueish_value, trueish_expected) in TRUEISH_TEST_PARAMS
    ] + [
        ("allow_others_to_delete", trueish_value, trueish_expected, None)
        for (trueish_value, trueish_expected) in TRUEISH_TEST_PARAMS
    ] + [
        ("allow_others_to_query", trueish_value, trueish_expected, None)
        for (trueish_value, trueish_expected) in TRUEISH_TEST_PARAMS
    ] + [
        ("allow_others_to_update", trueish_value, trueish_expected, None)
        for (trueish_value, trueish_expected) in TRUEISH_TEST_PARAMS
    ] + [
        ("set_defaults_to_null_for_not_null_fields_in_templates", trueish_value, trueish_expected, None)
        for (trueish_value, trueish_expected) in TRUEISH_TEST_PARAMS
    ] + [
        ("allow_true_curves_updates", trueish_value, trueish_expected, None)
        for (trueish_value, trueish_expected) in TRUEISH_TEST_PARAMS
    ] + [
         ("enable_ownership_based_access_control", trueish_value, trueish_expected, None)
         for (trueish_value, trueish_expected) in TRUEISH_TEST_PARAMS
     ] + [
         ("enable_z_defaults", trueish_value, trueish_expected, None)
         for (trueish_value, trueish_expected) in TRUEISH_TEST_PARAMS
     ]
)#yapf:enable
def test_feature_server_setters(service_config, attribute, new_value, expected_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(service_config.feature_server, attribute, new_value)
    else:
        setattr(service_config.feature_server, attribute, new_value)
        assert getattr(service_config.feature_server, attribute) == expected_value
