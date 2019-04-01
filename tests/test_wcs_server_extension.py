# coding=utf-8
"""Tests for WCS server extension."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

import pytest
# import fixtures
from .helpers import image_service_config as service_config

@pytest.fixture(scope = "function")
def service_extension(service_config):
    return service_config.wcs_server


@pytest.mark.parametrize(
    ('attribute', 'expectedValue', 'exception'),
    [
        ('britney_spears', 'should cause an', AttributeError),  # because she isn't a member
        ('enabled', False, None)
    ]
)
def test_wcs_getters(service_config, attribute, expectedValue, exception):
    if exception is not None:
        with pytest.raises(exception):
            assert getattr(service_config.wcs_server, attribute) == expectedValue
    else:
        assert getattr(service_config.wcs_server, attribute) == expectedValue


@pytest.mark.parametrize(
    ('attribute', 'newValue', 'exception'),
    [
        ('britney_spears', 'should cause a', TypeError),  # because she isn't a member
        ('enabled', True, None)
    ]
)
def test_wcs_setters(service_config, attribute, newValue, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(service_config.wcs_server, attribute, newValue)
            assert getattr(service_config.wcs_server, attribute) == newValue
    else:
        setattr(service_config.wcs_server, attribute, newValue)
        assert getattr(service_config.wcs_server, attribute) == newValue