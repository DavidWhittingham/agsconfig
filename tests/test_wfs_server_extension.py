"""Tests for WFS server extensions."""
# Python 2/3 compatibility
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()

import os.path
import shutil
import datetime

import agsconfig
from agsconfig.services.wfs_server_extension import WFSServerExtension as wfs
import pytest

SDDRAFT_FILE_PATH = os.path.abspath("{0}/samples/example.sddraft".format(os.path.dirname(__file__)))

@pytest.fixture
def mapserver():
    return agsconfig.load_map_sddraft(open(SDDRAFT_FILE_PATH, 'rb+'))

@pytest.mark.parametrize(
    ('attribute', 'expectedValue', 'exception'),
    [
        ('britney_spears', 'should cause an', AttributeError), # because she isn't a member
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
def test_getters(mapserver, attribute, expectedValue, exception):
    if exception is not None:
        with pytest.raises(exception):
            assert getattr(mapserver.wfs_server_extension, attribute) == expectedValue
    else:
        assert getattr(mapserver.wfs_server_extension, attribute) == expectedValue


@pytest.mark.parametrize(
    ('attribute', 'newValue', 'exception'),
    [
        ('britney_spears', 'should cause a', TypeError), # because she isn't a member
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
def test_setters(mapserver, attribute, newValue, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(mapserver.wfs_server_extension, attribute, newValue)
            assert getattr(mapserver.wfs_server_extension, attribute) == newValue
    else:
        setattr(mapserver.wfs_server_extension, attribute, newValue)
        assert getattr(mapserver.wfs_server_extension, attribute) == newValue