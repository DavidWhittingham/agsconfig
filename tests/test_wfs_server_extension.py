# coding=utf-8
"""Tests for WFS server extensions."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

import pytest

from agsconfig.services.wfs_server_extension import WFSServerExtension as wfs

# Import shared fixtures
# pylint: disable=unused-import
from .helpers import map_service_config as service_config
# pylint: enable=unused-import


@pytest.mark.parametrize(
    ('attribute', 'expectedValue', 'exception'),
    [
        ('britney_spears', 'should cause an', AttributeError),  # because she isn't a member
        ('enabled', False, None),
        ('app_schema_uri', 'WFS', None),
        ('app_schema_prefix', 'psl_test', None),
        ('enable_transactions', None, None),
        ('axis_order_wfs10', [wfs.AxisOrder.long_lat], None),
        ('axis_order_wfs11', [wfs.AxisOrder.lat_long], None),
        ('service_type', None, None),
        ('service_type_version', None, None)
    ]
)
def test_getters(service_config, attribute, expectedValue, exception):
    if exception is not None:
        with pytest.raises(exception):
            assert getattr(service_config.wfs_server, attribute) == expectedValue
    else:
        assert getattr(service_config.wfs_server, attribute) == expectedValue


@pytest.mark.parametrize(
    ('attribute', 'newValue', 'exception'),
    [
        ('britney_spears', 'should cause a', TypeError),  # because she isn't a member
        ('enabled', True, None),
        ('app_schema_uri', 'x', None),
        ('app_schema_prefix', 'pfx', None),
        ('enable_transactions', True, None),
        ('axis_order_wfs10', [wfs.AxisOrder.lat_long], None),
        ('axis_order_wfs11', [wfs.AxisOrder.long_lat], None),
        ('service_type', 'Blah', None),
        ('service_type_version', 1.0, None)
    ]
)
def test_setters(service_config, attribute, newValue, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(service_config.wfs_server, attribute, newValue)
            assert getattr(service_config.wfs_server, attribute) == newValue
    else:
        setattr(service_config.wfs_server, attribute, newValue)
        assert getattr(service_config.wfs_server, attribute) == newValue