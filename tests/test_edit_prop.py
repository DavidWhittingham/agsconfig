# coding=utf-8
"""Tests for EditorProperty."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

import pytest

from agsconfig.editing.edit_prop import EditorProperty

class TestObj(object):

    t = EditorProperty({
        "constraints": {
            "min": 0,
            "max": 10
        }
    })

@pytest.fixture
def test_obj():
    return TestObj()

def test_no_delete(test_obj):
    with pytest.raises(AttributeError):
        del test_obj.t


@pytest.mark.parametrize(
    ('value'),
    [-20, 20]
)
def test_value_assignment_extremes(test_obj, value):
    """Tests that values set at extremes cause value errors."""
    with pytest.raises(ValueError):
            test_obj.t = value