# coding=utf-8
"""Tests for Vector Tile services."""

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
import agsconfig

# Fixture imports
from .helpers import vector_tile_service_config as service_config


def test_load_service_config(service_config):
    # this just tests the fixture setup
    assert True


@pytest.mark.parametrize(
    ("attribute", "expected_value", "exception"),
    [
        ("britney_spears", "should cause an", AttributeError),  # because she isn"t a member of vectortile
        ("portal_url", "https://uat-spatial.information.qld.gov.au/arcgis/", None),
        ("title", "TestVectorTile", None),
        ("keep_existing_data", False, None),
        ("keep_cache", False, None),
        ("cluster", "default", None),
        ("name", "TestVectorTile", None),
        ("folder", "Test2", None),
        ("supported_image_return_types", "MIME", None),
        ("max_record_count", 2000, None),
        ("cache_dir", "\\\\server\\fileshare\\arcgis\\directories\\arcgiscache", None),
        ("client_caching_allowed", True, None),
        ("anti_aliasing_mode", agsconfig.VectorTileServer.AntiAliasingMode.fast, None),
        ("text_anti_aliasing_mode", agsconfig.VectorTileServer.TextAntiAliasingMode.force, None),
        ("is_cached", True, None),
        ("tiling_scheme", 0, None),
        ("ignore_cache", False, None),
        ("web_enabled", True, None),
        ("tags", ["tag"], None)
    ]
)
def test_getters(service_config, attribute, expected_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            assert getattr(service_config, attribute) == expected_value
    else:
        assert getattr(service_config, attribute) == expected_value


@pytest.mark.parametrize(
    ("attribute", "new_value", "expected", "exception"),
    [
        ("britney_spears", "should cause a", None, TypeError),  # model_base prevents assignment of unknown members
        (
            "portal_url", "https://uat-spatial.information.qld.gov.au/arcgis/s",
            "https://uat-spatial.information.qld.gov.au/arcgis/s", None
        ),
        ("title", "TestVectorTiles", "TestVectorTiles", None),
        ("keep_existing_data", True, True, None),
        ("keep_cache", True, True, None),
        ("cluster", "defaultx", "defaultx", None),
        ("name", "TestVectorTilex", "TestVectorTilex", None),
        ("folder", "Test1", "Test1", None),
        ("supported_image_return_types", "xMIME", "xMIME", None),
        ("max_record_count", 4000, 4000, None),
        ("cache_dir", True, True, None),
        ("client_caching_allowed", False, False, None),
        ("anti_aliasing_mode", "somevalue not in the enum", None, ValueError),
        (
            "anti_aliasing_mode", agsconfig.VectorTileServer.AntiAliasingMode.best,
            agsconfig.VectorTileServer.AntiAliasingMode.best, None
        ),
        ("anti_aliasing_mode", "Fastest", agsconfig.VectorTileServer.AntiAliasingMode.fastest, None),
        ("text_anti_aliasing_mode", "Unknown", None, ValueError),
        (
            "text_anti_aliasing_mode", agsconfig.VectorTileServer.TextAntiAliasingMode.normal,
            agsconfig.VectorTileServer.TextAntiAliasingMode.normal, None
        ),
        ("text_anti_aliasing_mode", "Force", agsconfig.VectorTileServer.TextAntiAliasingMode.force, None),
        ("is_cached", False, False, None),
        ("tiling_scheme", 1, 1, None),
        ("ignore_cache", True, True, None),
        ("web_enabled", False, False, None),
        ("tags", "tags,more tags", ['tags', 'more tags'], None)
    ]
)
def test_setters(service_config, attribute, new_value, expected, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(service_config, attribute, new_value)
            assert getattr(service_config, attribute) == expected
    else:
        setattr(service_config, attribute, new_value)
        assert getattr(service_config, attribute) == expected
