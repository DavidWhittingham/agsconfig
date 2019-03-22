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
from .helpers import vector_tile_service_config as vt_service

@pytest.mark.parametrize(
    ("attribute", "expectedValue", "exception"),
    [
        ("max_record_count", 2000, None),
        ("enable_z_defaults", False, None),
        ("z_default_value", 0, None),
        ("enable_ownership_based_access_control", False, None),
        ("allow_others_to_query", True, None),
        ("allow_others_to_update", False, None),
        ("allow_others_to_delete", False, None),
        ("realm", None, None),
        ("editor_tracking_time_zone_id", "UTC", None),
        ("editor_tracking_respects_daylight_saving_time", False, None),
        ("editor_tracking_time_in_utc", True, None),
        ("allow_geometry_updates", True, None),
        ("allow_true_curves_updates", False, None),
        ("only_allow_true_curve_updates_by_true_curve_clients", "false0", None),
        ("xss_prevention_enabled", True, None),
        ("sync_version_creation_rule", "versionPerDownloadedMap", None),
        ("online_resource", "https://uat-spatial.information.qld.gov.au/arcgis/services/TestVectorTile/VectorTileServer/VectorTileServer", None),
        ("capabilities", [agsconfig.VectorTileServerExtension.ExtensionCapabilities.query,
                        agsconfig.VectorTileServerExtension.ExtensionCapabilities.create,
                        agsconfig.VectorTileServerExtension.ExtensionCapabilities.update,
                        agsconfig.VectorTileServerExtension.ExtensionCapabilities.delete,
                        agsconfig.VectorTileServerExtension.ExtensionCapabilities.uploads,
                        agsconfig.VectorTileServerExtension.ExtensionCapabilities.editing], None),
        ("web_enabled", True, None)
    ]
)
def test_getters(vt_service, attribute, expectedValue, exception):
    if exception is not None:
        with pytest.raises(exception):
            getattr(vt_service.vector_tile_server, attribute)
    else:
        assert getattr(vt_service.vector_tile_server, attribute) == expectedValue

@pytest.mark.parametrize(
    ("attribute", "new_value", "exception"),
    [
        ("max_record_count", 1000, None),
        ("enable_z_defaults", True, None),
        ("z_default_value", 10, None),
        ("enable_ownership_based_access_control", True, None),
        ("allow_others_to_query", False, None),
        ("allow_others_to_update", True, None),
        ("allow_others_to_delete", True, None),
        ("realm", "someRealm", None),
        ("editor_tracking_time_zone_id", "UTC+10", None),
        ("editor_tracking_respects_daylight_saving_time", True, None),
        ("editor_tracking_time_in_utc", False, None),
        ("allow_geometry_updates", False, None),
        ("allow_true_curves_updates", True, None),
        ("only_allow_true_curve_updates_by_true_curve_clients", "false1", None),
        ("xss_prevention_enabled", False, None),
        ("sync_version_creation_rule", "versionPerDownloadedMap2", None),
        ("online_resource", "https://uat-spatial.information.qld.gov.au/arcgis/services/TestVectorTile/VectorTileServer/VectorTileServer/something", None),
        ("capabilities", [agsconfig.VectorTileServerExtension.ExtensionCapabilities.query], None),
        ("web_enabled", False, None)
    ]
)
def test_setters(vt_service, attribute, new_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(vt_service.vector_tile_server, attribute, new_value)
    else:
        setattr(vt_service.vector_tile_server, attribute, new_value)
        assert getattr(vt_service.vector_tile_server, attribute) == new_value