# coding=utf-8
"""This module contains tests for map services."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

import pytest

from agsconfig.services.map_server import MapServer

from .helpers import map_service_config as service_config
from .cacheable_core_mixin import *
from .cacheable_ext_mixin import *
from .feature_server_extension_mixin import *
from .image_dimensions_mixin import *
from .kml_server_extension_mixin import *
from .max_record_count_mixin import *
from .na_server_extension_mixin import *
from .output_dir_mixin import *
from .parcel_fabric_server_extension_mixin import *
from .scale_range_mixin import *
from .service_base_mixin import *
from .validation_server_extension_mixin import *
from .version_management_server_extension_mixin import *
from .wcs_server_extension_mixin import *
from .wfs_server_extension_mixin import *
from .wms_server_extension_mixin import *


def test_load_map_service_config(service_config):
    # this just tests the fixture setup
    assert True


def test_map_save(service_config):
    service_config.save()
    assert True


@pytest.mark.parametrize(
    ("capabilities", "expected", "ex"),
    [
        ([MapServer.Capability.map], [MapServer.Capability.map], None),
        ([], [], None),
        (["Query"], [MapServer.Capability.query], None),
        (["Fail"], None, ValueError),
        ([123], None, ValueError)
    ]
)  # yapf: disable
def test_map_capabilities(service_config, capabilities, expected, ex):
    if ex is not None:
        with pytest.raises(ex):
            service_config.capabilities = capabilities
    else:
        service_config.capabilities = capabilities
        assert set(service_config.capabilities) == set(expected)


@pytest.mark.parametrize(
    ("attribute", "value", "exception"), [
        ("comic_book_guy", None, AttributeError), ("anti_aliasing_mode", MapServer.AntiAliasingMode.fastest, None),
        ("text_anti_aliasing_mode", MapServer.TextAntiAliasingMode.force, None),
        ("disable_identify_relates", False, None), ("enable_dynamic_layers", False, None), ("file_path", None, None),
        ("schema_locking_enabled", True, None)
    ]
)
def test_map_getters(service_config, attribute, value, exception):
    if exception is not None:
        with pytest.raises(exception):
            getattr(service_config, attribute)
    else:
        assert getattr(service_config, attribute) == value


@pytest.mark.parametrize(
    ("attribute", "new_value", "expected_value", "exception"),
    [
        ("anti_aliasing_mode", "comic book guy", None, ValueError),
        ("anti_aliasing_mode", "Best", MapServer.AntiAliasingMode.best, None),
        ("text_anti_aliasing_mode", "comic book guy", None, ValueError),
        ("text_anti_aliasing_mode", "Normal", MapServer.TextAntiAliasingMode.normal, None),
        ("disable_identify_relates", True, True, None),
        ("enable_dynamic_layers", True, True, None),
        ("file_path", "A:/path", "A:/path", None),
        ("schema_locking_enabled", False, False, None),
        ("date_fields_respect_daylight_saving_time", True, True, None),
        ("date_fields_respect_daylight_saving_time", False, False, None),
        ("date_fields_timezone_id", "Australia/Brisbane", "Australia/Brisbane", None),

        # this happens/is expected because the time zones are equivalent
        ("date_fields_timezone_id", "Australia/Canberra", "Australia/Sydney", None),

        # this should happen because input should allow the Windows Timezone IDs
        ("date_fields_timezone_id", "E. Australia Standard Time", "Australia/Brisbane", None)
    ]
)
def test_map_setters(service_config, attribute, new_value, expected_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(service_config, attribute, new_value)
    else:
        setattr(service_config, attribute, new_value)
        assert getattr(service_config, attribute) == expected_value
