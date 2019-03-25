# coding=utf-8
"""This module contains tests the mobile service extension."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

# Third-party imports
import pytest

# Fixture imports
from .helpers import TRUEISH_TEST_PARAMS


def test_na_capabilities(service_config):
    assert len(service_config.na_server.capabilities) == 0 
    with pytest.raises(ValueError):
        service_config.na_server.capabilities = "Blah"

@pytest.mark.parametrize(("enabled", "expected"), TRUEISH_TEST_PARAMS)
def test_na_enabled(service_config, enabled, expected):
    service_config.na_server.enabled = enabled
    assert service_config.na_server.enabled == expected