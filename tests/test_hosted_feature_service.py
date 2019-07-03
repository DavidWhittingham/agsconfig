# coding=utf-8
"""This module contains tests for hosted feature services."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

import pytest

import agsconfig
from agsconfig.services.hosted_feature_server import HostedFeatureServer

from .helpers import hosted_feature_config as service_config


def test_load_service_config(service_config):
    # this just tests the fixture setup
    assert True


def test_save(service_config):
    service_config.save()
    assert True


@pytest.mark.parametrize(
    ("capabilities", "expected", "ex"),
    [
        ([agsconfig.MapServer.Capability.map], [agsconfig.MapServer.Capability.map], None),
        ([], [], None),
        (["Query"], [agsconfig.MapServer.Capability.query], None),
        (["Fail"], None, ValueError),
        ([123], None, ValueError)
    ]
)  # yapf: disable
def test_capabilities(service_config, capabilities, expected, ex):
    if ex is not None:
        with pytest.raises(ex):
            service_config.capabilities = capabilities
    else:
        service_config.capabilities = capabilities
        assert set(service_config.capabilities) == set(expected)


@pytest.mark.parametrize(
    ('attribute', 'value', 'exception'), [
        ('allow_geometry_updates', True, None),
        ('allow_true_curves_updates', False, None),
        ('only_allow_true_curve_updates_by_true_curve_clients', False, None),
        ('enable_z_defaults', True, None),
        ('z_default_value', 0, None),
        ('allow_update_without_m_values', True, None),
        ('dataset_inspected', True, None),
        ('creator_present', False, None),
        ('data_in_gdb', True, None)
    ]
)
def test_getters(service_config, attribute, value, exception):
    if exception is not None:
        with pytest.raises(exception):
            getattr(service_config, attribute)
    else:
        assert getattr(service_config, attribute) == value


@pytest.mark.parametrize(
    ('attribute', 'new_value', 'expected_value', 'exception'), [
        ('anti_aliasing_mode', 'comic book guy', None, ValueError),
        ('text_anti_aliasing_mode', 'comic book guy', None, ValueError),
        ('disable_identify_relates', True, True, None),
        ('enable_dynamic_layers', True, True, None),
        ('file_path', 'A:/path', 'A:/path', None),
        ('schema_locking_enabled', False, False, None)
    ]
)
def test_setters(service_config, attribute, new_value, expected_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(service_config, attribute, new_value)
    else:
        setattr(service_config, attribute, new_value)
        assert getattr(service_config, attribute) == expected_value
