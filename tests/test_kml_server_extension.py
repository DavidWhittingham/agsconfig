# coding=utf-8
"""Tests for KML server extension."""

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
from .helpers import map_service_config
# Local imports
from agsconfig.services.kml_server_extension import KmlServerExtension as kml


@pytest.mark.parametrize(
    ('attribute', 'expectedValue', 'exception'),
    [
        ('britney_spears', 'should cause an', AttributeError),  # because she isn't a member
        ('enabled', True, None),
        ('capabilities', [kml.Capability.single_image, kml.Capability.separate_images, kml.Capability.vectors], None),
        ('compatibility_mode', [kml.CompatibilityMode.google_earth], None),
        ('dpi', 96, None),
        ('feature_limit', 1000000, None),
        ('image_size', 1024, None),
        ('link_description', None, None),
        ('link_name', None, None),
        ('message', None, None),
        ('min_refresh_period', 30, None),
        ('use_default_snippets', 0, None),
        ('use_network_link_control_tag', 0, None)
    ]
)
def test_kml_getters(map_service_config, attribute, expectedValue, exception):
    if exception is not None:
        with pytest.raises(exception):
            assert getattr(map_service_config.kml_server, attribute) == expectedValue
    else:
        assert getattr(map_service_config.kml_server, attribute) == expectedValue


@pytest.mark.parametrize(
    ('attribute', 'new_value', 'exception'),
    [
        ('britney_spears', 'should cause a', TypeError),  # because she isn't a member
        ('enabled', False, None),
        ('capabilities', [kml.Capability.single_image], None),
        ('compatibility_mode', [kml.CompatibilityMode.google_maps], None),
        ('dpi', 1024, None),
        ('feature_limit', 1000, None),
        ('image_size', 96, None),
        ('link_description', 'description', None),
        ('link_name', 'link_name', None),
        ('message', 'message', None),
        ('min_refresh_period', 20, None),
        ('use_default_snippets', 10, None),
        ('use_network_link_control_tag', 10, None)
    ]
)
def test_kml_setters(map_service_config, attribute, new_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(map_service_config.kml_server, attribute, new_value)
            assert getattr(map_service_config.kml_server, attribute) == new_value
    else:
        setattr(map_service_config.kml_server, attribute, new_value)
        assert getattr(map_service_config.kml_server, attribute) == new_value