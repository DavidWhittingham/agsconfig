# coding=utf-8
"""Tests for Image services."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

import datetime
import os.path

import pytest

import agsconfig
from agsconfig.services.image_server import ImageServer

SDDRAFT_FILE_PATH = os.path.abspath("{0}/samples/imageservice.sddraft".format(os.path.dirname(__file__)))
SDDRAFT_FILE_PATH2 = os.path.abspath("{0}/samples/mapservice.sddraft".format(os.path.dirname(__file__)))


@pytest.fixture
def imageserver():
    return agsconfig.load_image_sddraft(open(SDDRAFT_FILE_PATH, 'rb+'))


def test_load_imagesddraft():
    """Load a vector tile into a map sddraft object."""
    sddraft = agsconfig.load_image_sddraft(open(SDDRAFT_FILE_PATH, 'rb+'))

    assert isinstance(sddraft, agsconfig.services.image_server.ImageServer)


@pytest.mark.parametrize(
    ('attribute', 'expectedValue', 'exception'),
    [
        ('britney_spears', 'should cause an', AttributeError),  # because she isn't a member
        (
            'capabilities', [
                ImageServer.Capability.image, ImageServer.Capability.metadata, ImageServer.Capability.catalog,
                ImageServer.Capability.mensuration
            ], None
        ),
        ('client_caching_allowed', True, None),
        ('cluster', 'default', None),
        ('access_information', None, None),
        (
            'allowed_mosaic_methods', [
                ImageServer.MosaicMethod.north_west, ImageServer.MosaicMethod.center,
                ImageServer.MosaicMethod.lock_raster, ImageServer.MosaicMethod.by_attribute,
                ImageServer.MosaicMethod.nadir, ImageServer.MosaicMethod.viewpoint, ImageServer.MosaicMethod.seamline,
                ImageServer.MosaicMethod.none
            ], None
        ),
        ('cache_dir', 'cacheDir', None),
        ('cache_on_demand', False, None),
        ('client_caching_allowed', True, None),
        ('credits', None, None),
        ('description', None, None),
        ('export_tiles_allowed', False, None),
        ('folder', None, None),
        ('high_isolation', True, None),
        ('idle_timeout', 1800, None),
        ('instances_per_container', 1, None),
        ('keep_cache', False, None),
        ('max_export_tiles_count', 100000, None),
        ('max_image_height', 4100, None),
        ('max_image_width', 15000, None),
        ('max_instances', 2, None),
        ('max_scale', -1, None),
        ('min_instances', 1, None),
        ('min_scale', -1, None),
        ('min_instances', 1, None),
        ('min_scale', -1, None),
        ('name', 'ExampleImageService', None),
        ('recycle_interval', None, None),
        ('recycle_start_time', None, None),
        ('summary', None, None),
        ('tags', [], None),
        ('title', 'IMG.QldOrthoSecure_Gda94', None),
        ('usage_timeout', 600, None),
        ('use_local_cache_dir', True, None),
        ('wait_timeout', 60, None)
    ]
)
def test_getters(imageserver, attribute, expectedValue, exception):
    if exception is not None:
        with pytest.raises(exception):
            assert getattr(imageserver, attribute) == expectedValue
    else:
        assert getattr(imageserver, attribute) == expectedValue


@pytest.mark.parametrize(
    ('attribute', 'newValue', 'exception'),
    [
        ('britney_spears', 'should cause a', TypeError),  # because she isn't a member
        ('capabilities', [ImageServer.Capability.image], None),
        ('capabilities', 'Something', ValueError),
        ('client_caching_allowed', False, None),
        ('cluster', 'default', None),
        ('access_information', "Access information", None),
        ('allowed_mosaic_methods', [ImageServer.MosaicMethod.north_west], None),
        ('cache_dir', 'a:/cache/dir', None),
        ('cache_on_demand', True, None),
        ('client_caching_allowed', False, None),
        ('credits', 'Credits', None),
        ('description', "Description", None),
        ('export_tiles_allowed', True, None),
        ('folder', "a:/folder", None),
        ('high_isolation', False, None),
        ('idle_timeout', 1200, None),
        ('instances_per_container', 2, None),
        ('keep_cache', True, None),
        ('max_export_tiles_count', 10000, None),
        ('max_image_height', 410, None),
        ('max_image_width', 1500, None),
        ('max_instances', 2, None),
        ('max_scale', 1000, None),
        ('min_instances', 2, None),
        ('min_scale', 10, None),
        ('name', 'Example', None),
        ('recycle_interval', 1, None),
        ('recycle_start_time', datetime.time(16, 0), None),
        ('summary', 'summary', None),
        ('tags', ['blah'], None),
        ('title', 'SomeTitle', None),
        ('usage_timeout', 6000, None),
        ('use_local_cache_dir', False, None),
        ('wait_timeout', 160, None)
    ]
)
def test_setters(imageserver, attribute, newValue, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(imageserver, attribute, newValue)
            assert getattr(imageserver, attribute) == newValue
    else:
        setattr(imageserver, attribute, newValue)
        assert getattr(imageserver, attribute) == newValue