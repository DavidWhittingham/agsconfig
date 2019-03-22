# coding=utf-8
"""This module contains shared tests for all models that use image dimensions."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

import pytest

@pytest.mark.parametrize(("height", "ex"), [
    (1000, None),
    (None, ValueError),
    (0, ValueError),
    (-1, ValueError)
])
def test_max_image_height(service_config, height, ex):
    if (ex != None):
        with pytest.raises(ex):
            service_config.max_image_height = height
    else:
        service_config.max_image_height = height
        assert service_config.max_image_height == height

@pytest.mark.parametrize(("width", "ex"), [
    (1000, None),
    (None, ValueError),
    (0, ValueError),
    (-1, ValueError)
])
def test_max_image_width(service_config, width, ex):
    if (ex != None):
        with pytest.raises(ex):
            service_config.max_image_width = width
    else:
        service_config.max_image_width = width
        assert service_config.max_image_width == width