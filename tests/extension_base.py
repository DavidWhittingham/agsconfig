# coding=utf-8
"""Tests for base functionality of service extensions."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

from .helpers import TRUEISH_TEST_PARAMS

BASE_GETTER_TEST_CASES = [
    ('non_existent_attribute', 'should cause an', AttributeError),  # because she isn't a member
    ('enabled', False, None)
]

BASE_SETTER_TEST_CASES = [
    ('non_existent_attribute', 'should cause an', None, AttributeError),  # because she isn't a member
] + [("enabled", trueish_value, trueish_expected, None) for (trueish_value, trueish_expected) in TRUEISH_TEST_PARAMS]
