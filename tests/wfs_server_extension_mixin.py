# coding=utf-8
"""Tests for WFS server extensions."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

# Third-party lib imports
import pytest

# agsconfig imports to help create test values
from agsconfig.services.wfs_server_extension import WFSServerExtension as wfs

# Addition test fixtures to mix in
from .custom_get_capabilities_mixin import *
from .extension_base import *
from .ogc_metadata_extension_mixin import *


@pytest.mark.parametrize(#yapf:disable
    ('attribute', 'expected_value', 'exception'),
    BASE_GETTER_TEST_CASES +
    OGC_GETTER_TEST_CASES +
    CUSTOM_GET_CAPABILITIES_GETTER_TEST_CASES +
    [
        ('app_schema_uri', 'WFS', None),
        ('app_schema_prefix', 'FooBarSchemaPrefix', None),
        ('enable_transactions', False, None),
        ('axis_order_wfs_10', wfs.AxisOrder.long_lat, None),
        ('axis_order_wfs_11', wfs.AxisOrder.lat_long, None),
        ('hours_of_service', 'Test hours', None),
        ('service_type', None, None),
        ('service_type_version', None, None)
    ]
)#yapf:enable
def test_wfs_getters(service_config, attribute, expected_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            assert getattr(service_config.wfs_server, attribute) == expected_value
    else:
        assert getattr(service_config.wfs_server, attribute) == expected_value


@pytest.mark.parametrize(#yapf:disable
    ('attribute', 'new_value', 'expected_value', 'exception'),
    BASE_SETTER_TEST_CASES +
    OGC_SETTER_TEST_CASES +
    CUSTOM_GET_CAPABILITIES_SETTER_TEST_CASES +
    [
        ('app_schema_uri', 'x', 'x', None), ('app_schema_prefix', 'pfx', 'pfx', None),
        ('enable_transactions', True, True, None), ('enable_transactions', 'nuts', None, ValueError),
        ('axis_order_wfs_10', wfs.AxisOrder.lat_long, wfs.AxisOrder.lat_long, None),
        ('axis_order_wfs_10', 'LatLong', wfs.AxisOrder.lat_long, None), ('axis_order_wfs_10', 'err', None, ValueError),
        ('axis_order_wfs_11', wfs.AxisOrder.long_lat, wfs.AxisOrder.long_lat, None),
        ('axis_order_wfs_11', 'err', None, ValueError), ('axis_order_wfs_11', 'LongLat', wfs.AxisOrder.long_lat, None),
        ('hours_of_service', '24/7', '24/7'),
        ('service_type', 'Blah', 'Blah', None), ('service_type_version', 1.0, 1.0, None)
    ]
)#yapf:enable
def test_wfs_setters(service_config, attribute, new_value, expected_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(service_config.wfs_server, attribute, new_value)
    else:
        setattr(service_config.wfs_server, attribute, new_value)
        assert getattr(service_config.wfs_server, attribute) == expected_value
