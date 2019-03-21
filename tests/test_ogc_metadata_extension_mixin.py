"""Tests for ogc metadata attributes. """
# Python 2/3 compatibility
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()

import os.path
import shutil
import datetime

import agsconfig

import pytest

SDDRAFT_FILE_PATH = os.path.abspath("{0}/samples/imageservice.sddraft".format(os.path.dirname(__file__)))
SDDRAFT_FILE_PATH2 = os.path.abspath("{0}/samples/mapservice.sddraft".format(os.path.dirname(__file__)))

@pytest.fixture
def imageserver():
    return agsconfig.load_image_sddraft(open(SDDRAFT_FILE_PATH, 'rb+'))

@pytest.mark.parametrize(
    ('attribute', 'expectedValue', 'exception'),
    [
        ('britney_spears', 'should cause an', AttributeError), # because she isn't a member
        ('abstract', 'abstract', None),
        ('access_constraints', 'accessConstraints', None),
        ('city', 'city', None),
        ('country', 'country', None),
        ('keyword', 'keyword', None),
        ('fees', 'fees', None),
        ('name', 'name', None),
        ('title', 'title', None),
    ]
)
def test_getters(imageserver, attribute, expectedValue, exception):
    if exception is not None:
        with pytest.raises(exception):
            assert getattr(imageserver.wms_server_extension, attribute) == expectedValue
    else:
        assert getattr(imageserver.wms_server_extension, attribute) == expectedValue


@pytest.mark.parametrize(
    ('attribute', 'newValue', 'exception'),
    [
        ('britney_spears', 'should cause an', TypeError), # because she isn't a member
        ('abstract', False, None),
        ('access_constraints', False, None),
        ('city', 'Panama', None),
        ('country', 'Panama', None),
        ('keyword', 'keyword', None),
        ('fees', 'nil', None),
        ('name', 'dataset name', None),
        ('title', 'title', None),
    ]
)
def test_setters(imageserver, attribute, newValue, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(imageserver.wms_server_extension, attribute, newValue)
            assert getattr(imageserver.wms_server_extension, attribute) == newValue
    else:
        setattr(imageserver.wms_server_extension, attribute, newValue)
        assert getattr(imageserver.wms_server_extension, attribute) == newValue
