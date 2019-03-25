# coding=utf-8
"""Tests for Vector Tile services."""

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
from .helpers import vector_tile_service_config as vectortile


def test_load_service_config(vectortile):
    # this just tests the fixture setup
    assert True


@pytest.mark.parametrize(
    ("attribute", "expectedValue", "exception"),
    [
        ("britney_spears", "should cause an", AttributeError),  # because she isn"t a member of vectortile
        ("portal_url", "https://uat-spatial.information.qld.gov.au/arcgis/", None),
        ("title", "TestVectorTile", None),
        ("keep_existing_data", False, None),
        ("keep_cache", False, None),
        ("cluster", "default", None),
        ("name", "TestVectorTile", None),
        ("type_name", "VectorTileServer", None),
        ("service_folder", "Test2", None),
        ("supported_image_return_types", "MIME", None),
        ("max_record_count", 2000, None),
        ("export_tiles_allowed", False, None),
        ("max_export_tiles_count", 100000, None),
        ("cache_dir", None, None),
        ("cache_on_demand", False, None),
        ("client_caching_allowed", True, None),
        ("antialiasing_mode", [agsconfig.VectorTileServer.AntiAliasingMode.fast], None),
        ("text_antialiasing_mode", "Force", None),
        ("is_cached", True, None),
        ("tiling_scheme", 0, None),
        ("ignore_cache", False, None),
        ("web_enabled", True, None)
    ]
)
def test_getters(vectortile, attribute, expectedValue, exception):
    if exception is not None:
        with pytest.raises(exception):
            assert getattr(vectortile, attribute) == expectedValue
    else:
        assert getattr(vectortile, attribute) == expectedValue


@pytest.mark.parametrize(
    ("attribute", "newValue", "exception"),
    [
        ("britney_spears", "should cause a", TypeError),  # model_base prevents assignment of unknown members
        ("portal_url", "https://uat-spatial.information.qld.gov.au/arcgis/s", None),
        ("title", "TestVectorTiles", None),
        ("keep_existing_data", True, None),
        ("keep_cache", True, None),
        ("cluster", "defaultx", None),
        ("name", "TestVectorTilex", None),
        ("type_name", "VectorTileServerx", None),
        ("service_folder", "Test1", None),
        ("supported_image_return_types", "xMIME", None),
        ("max_record_count", 4000, None),
        ("export_tiles_allowed", False, None),
        ("max_export_tiles_count", 10000, None),
        ("cache_dir", True, None),
        ("cache_on_demand", True, None),
        ("client_caching_allowed", False, None),
        ("antialiasing_mode", "somevalue not in the enum", ValueError),
        ("antialiasing_mode", [agsconfig.VectorTileServer.AntiAliasingMode.best], None),
        ("text_antialiasing_mode", "Unknown", None),
        ("is_cached", False, None),
        ("tiling_scheme", 1, None),
        ("ignore_cache", True, None),
        ("web_enabled", False, None)
    ]
)
def test_setters(vectortile, attribute, newValue, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(vectortile, attribute, newValue)
            assert getattr(vectortile, attribute) == newValue
    else:
        setattr(vectortile, attribute, newValue)
        assert getattr(vectortile, attribute) == newValue
