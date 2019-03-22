# coding=utf-8
"""Tests for jpip server extension."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

import os.path

import pytest

import agsconfig
from .helpers import image_service_config

@pytest.mark.parametrize(
    ('attribute', 'expectedValue', 'exception'),
    [
        ('britney_spears', 'should cause an', AttributeError), # because she isn't a member
        ('enabled', False, None)
    ]
)
def test_getters(image_service_config, attribute, expectedValue, exception):
    if exception is not None:
        with pytest.raises(exception):
            assert getattr(image_service_config.jpip_server, attribute) == expectedValue
    else:
        assert getattr(image_service_config.jpip_server, attribute) == expectedValue


@pytest.mark.parametrize(
    ('attribute', 'newValue', 'exception'),
    [
        ('britney_spears', 'should cause a', TypeError), # because she isn't a member
        ('enabled', False, None)
    ]
)
def test_setters(image_service_config, attribute, newValue, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(image_service_config.jpip_server, attribute, newValue)
            assert getattr(image_service_config.jpip_server, attribute) == newValue
    else:
        setattr(image_service_config.jpip_server, attribute, newValue)
        assert getattr(image_service_config.jpip_server, attribute) == newValue