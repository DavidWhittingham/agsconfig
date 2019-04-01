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

# Python lib imports
import datetime

# Third-party imports
import pytest

# Local imports
from agsconfig.services.image_server import ImageServer

# import fixtures
from .helpers import image_service_config as service_config


def test_load_service_config(service_config):
    # this just tests the fixture setup
    assert True


@pytest.mark.parametrize(
    ("attribute", "expected_value", "exception"),
    [
        ("britney_spears", "should cause an", AttributeError),  # because she isn't a member
        (
            "capabilities", [
                ImageServer.Capability.image, ImageServer.Capability.metadata, ImageServer.Capability.catalog,
                ImageServer.Capability.mensuration
            ], None
        ),
        ("client_caching_allowed", True, None),
        ("cluster", "default", None),
        ("access_information", None, None),
        (
            "allowed_mosaic_methods", [
                ImageServer.MosaicMethod.north_west, ImageServer.MosaicMethod.center,
                ImageServer.MosaicMethod.lock_raster, ImageServer.MosaicMethod.by_attribute,
                ImageServer.MosaicMethod.nadir, ImageServer.MosaicMethod.viewpoint, ImageServer.MosaicMethod.seamline,
                ImageServer.MosaicMethod.none
            ], None
        ),
        ("cache_dir", "cacheDir", None),
        ("client_caching_allowed", True, None),
        ("credits", None, None),
        ("description", "This is a description", None),
        ("folder", None, None),
        ("high_isolation", True, None),
        ("idle_timeout", 1800, None),
        ("instances_per_container", 1, None),
        ("keep_cache", False, None),
        ("max_image_height", 4100, None),
        ("max_image_width", 15000, None),
        ("max_instances", 2, None),
        ("min_instances", 1, None),
        ("min_instances", 1, None),
        ("name", "ExampleImageService", None),
        ("recycle_interval", 24, None),
        ("recycle_start_time", datetime.time(0, 0), None),
        ("summary", None, None),
        ("tags", [], None),
        ("title", "Example Image Service", None),
        ("usage_timeout", 600, None),
        ("wait_timeout", 60, None),
        ("has_valid_sr", True, None)
    ]
)
def test_getters(service_config, attribute, expected_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            assert getattr(service_config, attribute) == expected_value
    else:
        assert getattr(service_config, attribute) == expected_value


@pytest.mark.parametrize(
    ("attribute", "new_value", "exception"),
    [
        ("britney_spears", "should cause a", TypeError),  # because she isn't a member
        ("capabilities", [ImageServer.Capability.image], None),
        ("capabilities", "Something", ValueError),
        ("client_caching_allowed", False, None),
        ("cluster", "default", None),
        ("access_information", "Access information", None),
        ("allowed_mosaic_methods", [ImageServer.MosaicMethod.north_west], None),
        ("cache_dir", "a:/cache/dir", None),
        ("client_caching_allowed", False, None),
        ("credits", "Credits", None),
        ("description", "Description", None),
        ("folder", "a:/folder", None),
        ("high_isolation", False, None),
        ("idle_timeout", 1200, None),
        ("instances_per_container", 2, None),
        ("keep_cache", True, None),
        ("max_image_height", 410, None),
        ("max_image_width", 1500, None),
        ("max_instances", 2, None),
        ("max_scale", 1000, None),
        ("min_instances", 2, None),
        ("min_scale", 10, None),
        ("name", "Example", None),
        ("recycle_interval", 1, None),
        ("recycle_start_time", datetime.time(16, 0), None),
        ("summary", "summary", None),
        ("tags", ["blah"], None),
        ("title", "SomeTitle", None),
        ("usage_timeout", 6000, None),
        ("wait_timeout", 160, None),
        ("has_valid_sr", False, None)
    ]
)
def test_setters(service_config, attribute, new_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(service_config, attribute, new_value)
            assert getattr(service_config, attribute) == new_value
    else:
        setattr(service_config, attribute, new_value)
        assert getattr(service_config, attribute) == new_value