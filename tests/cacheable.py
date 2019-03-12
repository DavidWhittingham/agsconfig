# coding=utf-8
"""This module contains the MapServer class for editing MapServer configuration pre or post publish"""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

import pytest

from .helpers import *

@pytest.mark.parametrize(("cache_dir", "expected"), [
    ("D:\\Test\\File\\Path", "D:\\Test\\File\\Path"),
    ("\\\\Test\\Unc\\Path", "\\\\Test\\Unc\\Path"),
    (None, None)
])
def test_cache_dir(service_config, cache_dir, expected):
    service_config.cache_dir = cache_dir
    assert service_config.cache_dir == expected


@pytest.mark.parametrize(("cache_on_demand", "expected"), TRUEISH_TEST_PARAMS)
def test_cache_on_demand(service_config, cache_on_demand, expected):
    service_config.cache_on_demand = cache_on_demand
    assert service_config.cache_on_demand == expected

@pytest.mark.parametrize(("keep_cache", "expected"), TRUEISH_TEST_PARAMS)
def test_keep_cache(service_config, keep_cache, expected):
    service_config.keep_cache = keep_cache
    assert service_config.keep_cache == expected
    
@pytest.mark.parametrize(("export_tiles_allowed", "expected"), TRUEISH_TEST_PARAMS)
def test_export_tiles_allowed(service_config, export_tiles_allowed, expected):
    service_config.export_tiles_allowed = export_tiles_allowed
    assert service_config.export_tiles_allowed == expected

@pytest.mark.parametrize(("max_export_tiles_count", "ex"), [
    (0, None),
    (100, None),
    (99999, None),
    (-10, ValueError)
])
def test_max_export_tiles_count(service_config, max_export_tiles_count, ex):
    if ex != None:
        with pytest.raises(ex):
            service_config.max_export_tiles_count = max_export_tiles_count
    else:
        service_config.max_export_tiles_count = max_export_tiles_count
        assert service_config.max_export_tiles_count == max_export_tiles_count

@pytest.mark.parametrize(("use_local_cache_dir", "expected"), TRUEISH_TEST_PARAMS)
def test_use_local_cache_dir(service_config, use_local_cache_dir, expected):
    service_config.use_local_cache_dir = use_local_cache_dir
    assert service_config.use_local_cache_dir == expected