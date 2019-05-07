# coding=utf-8
"""This module contains the MapServer class for editing MapServer configuration pre or post publish"""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position


import pytest
from .helpers import map_service_config as service_config

@pytest.mark.parametrize(("number", "ex"), [
    (-1, ValueError),
    (0, None),
    (200, None),
    (8000, None)
])
def test_max_record_count(service_config, number, ex):
    if ex is not None:
        with pytest.raises(ex):
            service_config.max_record_count = number
    else:
        service_config.max_record_count = number
        assert service_config.max_record_count == number
