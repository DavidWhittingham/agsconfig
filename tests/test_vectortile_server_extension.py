"""Tests for Vector Tile Extension."""
# Python 2/3 compatibility
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()

import os.path
import shutil
import agsconfig
import pytest

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
        ('capabilities', 'Update', None),
        ('web_enabled', True, None)
    ]
)
def test_getters(vectortile_ext, attribute, expectedValue, exception):
    if exception is not None:
        with pytest.raises(exception):
            assert getattr(vectortile_ext, attribute) == expectedValue
    else:
        assert getattr(vectortile_ext, attribute) == expectedValue

