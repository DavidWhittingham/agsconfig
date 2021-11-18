# coding=utf-8
"""This module contains test fixtures for services that support min/max scale ranges."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

import pytest

_SCALES = [(1.1, 1.1), ("1.1", 1.1), (None, 0)]


@pytest.mark.parametrize(("scale", "exp_scale"), _SCALES)
def test_max_scale(service_config, scale, exp_scale):
    service_config.max_scale = scale
    assert service_config.max_scale == exp_scale


@pytest.mark.parametrize(("scale", "exp_scale"), _SCALES)
def test_min_scale(service_config, scale, exp_scale):
    service_config.min_scale = scale
    assert service_config.min_scale == exp_scale


@pytest.mark.parametrize(
    ("min_scale", "max_scale", "expected_min", "expected_max"),
    [(0, 0, 0, 0), (1000, 0, 1000, 0), (0, 1000, 0, 1000), (1000, 2000, 2000, 2000)]
)
def test_min_max_scale(service_config, min_scale, max_scale, expected_min, expected_max):
    service_config.min_scale = min_scale
    service_config.max_scale = max_scale
    assert service_config.min_scale == expected_min
    assert service_config.max_scale == expected_max