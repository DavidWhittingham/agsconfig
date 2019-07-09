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

import pytest

from .helpers import TRUEISH_TEST_PARAMS

@pytest.mark.parametrize(("enabled", "expected"), TRUEISH_TEST_PARAMS)
def test_enabled(service_extension, enabled, expected):
    service_extension.enabled = enabled
    assert service_extension.enabled == expected