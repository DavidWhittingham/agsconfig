# coding=utf-8
"""Tests for Vector Tile Extension."""

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

SDDRAFT_FILE_PATH = os.path.abspath("{0}/samples/TestVectorTile.sddraft".format(os.path.dirname(__file__)))
SDDRAFT_FILE_PATH2 = os.path.abspath("{0}/samples/mapservice.sddraft".format(os.path.dirname(__file__)))

@pytest.fixture
def vectortile_ext():
    vectortile_service = agsconfig.load_vectortile_sddraft(open(SDDRAFT_FILE_PATH, 'rb+'))
    return vectortile_service.vectortile_server_extension

def test_load_vectortilesddraft():
    """Load a vector tile into a map sddraft object."""
    sddraft = agsconfig.load_vectortile_sddraft(open(SDDRAFT_FILE_PATH, 'rb+'))
    
    assert type(sddraft) == agsconfig.services.vectortile_server.VectorTileServer

@pytest.mark.parametrize(
    ('attribute', 'expectedValue', 'exception'),
    [
        ('max_record_count', 2000, None),
        ('enable_z_defaults', False, None),
        ('z_default_value', 0, None),
        ('enable_ownership_based_access_control', False, None),
        ('allow_others_to_query', True, None),
        ('allow_others_to_update', False, None),
        ('allow_others_to_delete', False, None),
        ('realm', None, None),
        ('editor_tracking_time_zone_id', 'UTC', None),
        ('editor_tracking_respects_daylight_saving_time', False, None),
        ('editor_tracking_time_in_utc', True, None),
        ('allow_geometry_updates', True, None),
        ('allow_true_curves_updates', False, None),
        ('only_allow_true_curve_updates_by_true_curve_clients', 'false0', None),
        ('xss_prevention_enabled', True, None),
        ('sync_version_creation_rule', 'versionPerDownloadedMap', None),
        ('online_resource', 'https://uat-spatial.information.qld.gov.au/arcgis/services/TestVectorTile/VectorTileServer/VectorTileServer', None),
        ('capabilities', [agsconfig.VectorTileServerExtension.ExtensionCapabilities.query,
                        agsconfig.VectorTileServerExtension.ExtensionCapabilities.create,
                        agsconfig.VectorTileServerExtension.ExtensionCapabilities.update,
                        agsconfig.VectorTileServerExtension.ExtensionCapabilities.delete,
                        agsconfig.VectorTileServerExtension.ExtensionCapabilities.uploads,
                        agsconfig.VectorTileServerExtension.ExtensionCapabilities.editing], None),
        ('web_enabled', True, None)
    ]
)
def test_getters(vectortile_ext, attribute, expectedValue, exception):
    if exception is not None:
        with pytest.raises(exception):
            getattr(vectortile_ext, attribute)
    else:
        assert getattr(vectortile_ext, attribute) == expectedValue
        pass

@pytest.mark.parametrize(
    ('attribute', 'newValue', 'exception'),
    [
        ('max_record_count', 1000, None),
        ('enable_z_defaults', True, None),
        ('z_default_value', 10, None),
        ('enable_ownership_based_access_control', True, None),
        ('allow_others_to_query', False, None),
        ('allow_others_to_update', True, None),
        ('allow_others_to_delete', True, None),
        ('realm', 'someRealm', None),
        ('editor_tracking_time_zone_id', 'UTC+10', None),
        ('editor_tracking_respects_daylight_saving_time', True, None),
        ('editor_tracking_time_in_utc', False, None),
        ('allow_geometry_updates', False, None),
        ('allow_true_curves_updates', True, None),
        ('only_allow_true_curve_updates_by_true_curve_clients', 'false1', None),
        ('xss_prevention_enabled', False, None),
        ('sync_version_creation_rule', 'versionPerDownloadedMap2', None),
        ('online_resource', 'https://uat-spatial.information.qld.gov.au/arcgis/services/TestVectorTile/VectorTileServer/VectorTileServer/something', None),
        ('capabilities', [agsconfig.VectorTileServerExtension.ExtensionCapabilities.query], None),
        ('web_enabled', False, None)
    ]
)
def test_setters(vectortile_ext, attribute, newValue, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(vectortile_ext, attribute, newValue)
    else:
        setattr(vectortile_ext, attribute, newValue)
        assert getattr(vectortile_ext, attribute) == newValue
        pass