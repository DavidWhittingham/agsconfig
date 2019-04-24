# coding=utf-8
"""This module contains tests related to the CacheableCoreMixin class."""

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
from .helpers import map_service_config as service_config

@pytest.mark.parametrize(
    ("cache_dir", "expected"),
    [("D:\\Test\\File\\Path", "D:\\Test\\File\\Path"), ("\\\\Test\\Unc\\Path", "\\\\Test\\Unc\\Path"), (None, None)]
)
def test_cache_dir(service_config, cache_dir, expected):
    service_config.cache_dir = cache_dir
    assert service_config.cache_dir == expected


@pytest.mark.parametrize(("keep_cache", "expected"), TRUEISH_TEST_PARAMS)
def test_keep_cache(service_config, keep_cache, expected):
    service_config.keep_cache = keep_cache
    assert service_config.keep_cache == expected
