# coding=utf-8
"""Tests for Image services."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
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
from .cacheable_core_mixin import *
from .cacheable_ext_mixin import *
from .image_dimensions_mixin import *
from .jpip_server_extension_mixin import *
from .max_record_count_mixin import *
from .output_dir_mixin import *
from .scale_range_mixin import *
from .service_base_mixin import *
from .wcs_server_extension_mixin import *
from .wms_server_extension_mixin import *


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
        ("max_record_count", 1000, None),
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
    ("attribute", "new_value", "expected_value", "exception"),
    [
        ("britney_spears", "should cause a", None, TypeError),  # because she isn't a member
        ("capabilities", [ImageServer.Capability.image], [ImageServer.Capability.image], None),
        ("capabilities", "Something", "Something", ValueError),
        ("client_caching_allowed", False, False, None),
        ("cluster", "default", "default", None),
        ("access_information", "Access information", "Access information", None),
        ("allowed_mosaic_methods", [ImageServer.MosaicMethod.north_west], [ImageServer.MosaicMethod.north_west], None),
        ("cache_dir", "a:/cache/dir", "a:/cache/dir", None),
        ("client_caching_allowed", False, False, None),
        ("credits", "Credits", "Credits", None),
        ("description", "Description", "Description", None),
        ("folder", "a:/folder", "a:/folder", None),
        ("high_isolation", False, False, None),
        ("idle_timeout", 1200, 1200, None),
        ("instances_per_container", 2, 2, None),
        ("keep_cache", True, True, None),
        ("max_image_height", 410, 410, None),
        ("max_image_width", 1500, 1500, None),
        ("max_instances", 2, 2, None),
        ("max_scale", 1000, 1000, None),
        ("max_record_count", 2000, 2000, None),
        ("min_instances", 2, 2, None),
        ("min_scale", 10, 10, None),
        ("name", "Example", "Example", None),
        ("raster_functions", ["None", "Path/To/RasterFunction.xml"], ["None", "Path/To/RasterFunction.xml"], None),
        ("recycle_interval", 1, 1, None),
        ("recycle_start_time", datetime.time(16, 0), datetime.time(16, 0), None),
        ("summary", "summary", "summary", None),
        ("tags", ["blah"], ["blah"], None),
        ("title", "SomeTitle", "SomeTitle", None),
        ("usage_timeout", 6000, 6000, None),
        ("wait_timeout", 160, 160, None),
        ("has_valid_sr", False, False, None),
        ("default_resampling_method", ImageServer.ResamplingMethod.cubic, ImageServer.ResamplingMethod.cubic, None),
        ("available_fields", "ONE,TWO,THREE", ["ONE", "TWO", "THREE"], None),
        ("available_fields", ["ONE", "TWO"], ["ONE", "TWO"], None),
        ("return_jpgpng_as_jpg", True, True, None),
        ("max_mosaic_image_count", 10, 10, None),
        ("max_download_size_limit", 10, 10, None),
        ("max_download_size_limit", -1, None, ValueError),
        ("max_download_size_limit", None, None, None),
        ("max_download_image_count", 20, 20, None),
        ("max_download_image_count", -1, None, ValueError),
        ("max_download_image_count", None, None, None),
        ("has_valid_sr", True, True, None)
    ]
)
def test_setters(service_config, attribute, new_value, expected_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(service_config, attribute, new_value)
    else:
        setattr(service_config, attribute, new_value)
        assert getattr(service_config, attribute) == expected_value


def test_setter(service_config):
    setattr(service_config, "max_download_size_limit", 10)
