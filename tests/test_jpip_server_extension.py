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

SDDRAFT_FILE_PATH = os.path.abspath("{0}/samples/imageservice.sddraft".format(os.path.dirname(__file__)))

@pytest.fixture
def mapserver():
    return agsconfig.load_map_sddraft(open(SDDRAFT_FILE_PATH, 'rb+'))

@pytest.mark.parametrize(
    ('attribute', 'expectedValue', 'exception'),
    [
        ('britney_spears', 'should cause an', AttributeError), # because she isn't a member
        ('enabled', False, None)
    ]
)
def test_getters(mapserver, attribute, expectedValue, exception):
    if exception is not None:
        with pytest.raises(exception):
            assert getattr(mapserver.jpip_server_extension, attribute) == expectedValue
    else:
        assert getattr(mapserver.jpip_server_extension, attribute) == expectedValue


@pytest.mark.parametrize(
    ('attribute', 'newValue', 'exception'),
    [
        ('britney_spears', 'should cause a', TypeError), # because she isn't a member
        ('enabled', False, None)
    ]
)
def test_setters(mapserver, attribute, newValue, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(mapserver.jpip_server_extension, attribute, newValue)
            assert getattr(mapserver.jpip_server_extension, attribute) == newValue
    else:
        setattr(mapserver.jpip_server_extension, attribute, newValue)
        assert getattr(mapserver.jpip_server_extension, attribute) == newValue