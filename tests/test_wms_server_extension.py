# coding=utf-8
"""Tests for WMS server extensions."""

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
# import fixtures
from .helpers import image_service_config as service_config
from agsconfig.services.wms_server_extension import WMSServerExtension as wms

@pytest.fixture(scope="function")
def service_extension(service_config):
    return service_config.wms_server

@pytest.mark.parametrize(
    ("attribute", "expected_value", "exception"),
    [
        ("britney_spears", "should cause an", AttributeError),  # because she isn't a member
        ("enabled", False, None),
        ("inherit_layer_names", False, None),
        ("path_to_custom_sld_file", "C:\\MyCustomSldeFile.sld", None),
        ("additional_spatial_ref_sys",
         ["102100", "102113", "3857", "20354", "20355", "20356", "28354", "28355", "28356"],
         None),
        ('capabilities',
         [wms.Capability.get_capabilities, wms.Capability.get_map, wms.Capability.get_feature_info, wms.Capability.get_styles, wms.Capability.get_legend_graphic, wms.Capability.get_schema_extension],
         None)
    ]
)
def test_wms_getters(service_config, attribute, expected_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            assert getattr(service_config.wms_server, attribute) == expected_value
    else:
        assert getattr(service_config.wms_server, attribute) == expected_value


@pytest.mark.parametrize(
    ("attribute", "new_value", "expected", "exception"),
    [
        ("britney_spears", "should cause a", None, TypeError),  # because she isn't a member
        ("enabled", True, True, None),
        ("inherit_layer_names", True, True, None),
        ("path_to_custom_sld_file", "a:/path", "a:/path", None),
        ("additional_spatial_ref_sys",
         ["EPSG:102100", "EPSG:102113", "EPSG:3857"],
         ["EPSG:102100", "EPSG:102113", "EPSG:3857"],
         None),
        ("additional_spatial_ref_sys",
         "EPSG:102100,EPSG:102113,EPSG:3857",
         ["EPSG:102100", "EPSG:102113", "EPSG:3857"],
         None),
        ("capabilities",
         ["GetCapabilities", "GetMap", "GetFeatureInfo"],
         [wms.Capability.get_capabilities, wms.Capability.get_map, wms.Capability.get_feature_info],
         None),
        ('postal_code', 4001, 4001, None),
        ('postal_code', '4001', 4001, None),
        ('address_type', 'Sometype', 'Sometype', None)
    ]
)
def test_wms_setters(service_config, attribute, new_value, expected, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(service_config.wms_server, attribute, new_value)
            assert getattr(service_config.wms_server, attribute) == expected
    else:
        setattr(service_config.wms_server, attribute, new_value)
        assert getattr(service_config.wms_server, attribute) == expected
