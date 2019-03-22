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

import os.path

import pytest

import agsconfig
from .helpers import map_service_config as mapserver


@pytest.mark.parametrize(
    ('attribute', 'expectedValue', 'exception'),
    [
        ('britney_spears', 'should cause an', AttributeError),  # because she isn't a member
        ('enabled', False, None),
        ('allow_geometry_updates', True, None),
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
def test_getters(mapserver, attribute, expectedValue, exception):
    if exception is not None:
        with pytest.raises(exception):
            assert getattr(mapserver.feature_server, attribute) == expectedValue
    else:
        assert getattr(mapserver.feature_server, attribute) == expectedValue


@pytest.mark.parametrize(
    ('attribute', 'newValue', 'exception'),
    [
        ('britney_spears', 'should cause a', TypeError),  # because she isn't a member
        ('enabled', False, None),
        ('allow_geometry_updates', False, None),
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
def test_setters(mapserver, attribute, newValue, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(mapserver.feature_server, attribute, newValue)
            assert getattr(mapserver.feature_server, attribute) == newValue
    else:
        setattr(mapserver.feature_server, attribute, newValue)
        assert getattr(mapserver.feature_server, attribute) == newValue