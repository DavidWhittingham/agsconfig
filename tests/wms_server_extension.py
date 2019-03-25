# coding=utf-8
"""Tests for WMS server extensions."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

# Third-party imports
import pytest


@pytest.fixture(scope="function")
def service_extension(service_config):
    return service_config.wcs_server


# import tests that should be applied to MapServer
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-position
from .ogc_metadata_extension_mixin import *
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-position


@pytest.mark.parametrize(
    ("attribute", "expected_value", "exception"),
    [
        ("britney_spears", "should cause an", AttributeError),  # because she isn't a member
        ("enabled", False, None),
        ("inherit_layer_names", False, None),
        ("path_to_custom_sld_file", "C:\\MyCustomSldeFile.sld", None)
    ]
)
def test_wms_getters(service_config, attribute, expected_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            assert getattr(service_config.wms_server, attribute) == expected_value
    else:
        assert getattr(service_config.wms_server, attribute) == expected_value


@pytest.mark.parametrize(
    ("attribute", "new_value", "exception"),
    [
        ("britney_spears", "should cause a", TypeError),  # because she isn't a member
        ("enabled", True, None),
        ("inherit_layer_names", True, None),
        ("path_to_custom_sld_file", "a:/path", None)
    ]
)
def test_wms_setters(service_config, attribute, new_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(service_config.wms_server, attribute, new_value)
            assert getattr(service_config.wms_server, attribute) == new_value
    else:
        setattr(service_config.wms_server, attribute, new_value)
        assert getattr(service_config.wms_server, attribute) == new_value
