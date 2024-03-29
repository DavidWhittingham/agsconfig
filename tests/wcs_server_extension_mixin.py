# coding=utf-8
"""Tests for WCS server extension."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

import pytest

from .custom_get_capabilities_mixin import *
from .extension_base import *
from .ogc_metadata_extension_mixin import *

@pytest.mark.parametrize(#yapf:disable
    ('attribute', 'expected_value', 'exception'),
    BASE_GETTER_TEST_CASES +
    OGC_GETTER_TEST_CASES +
    CUSTOM_GET_CAPABILITIES_GETTER_TEST_CASES
)#yapf:enable
def test_wcs_getters(service_config, attribute, expected_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            assert getattr(service_config.wcs_server, attribute) == expected_value
    else:
        assert getattr(service_config.wcs_server, attribute) == expected_value


@pytest.mark.parametrize(#yapf:disable
    ('attribute', 'new_value', 'expected_value', 'exception'),
    BASE_SETTER_TEST_CASES +
    OGC_SETTER_TEST_CASES +
    CUSTOM_GET_CAPABILITIES_SETTER_TEST_CASES
)#yapf:enable
def test_wcs_setters(service_config, attribute, new_value, expected_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(service_config.wcs_server, attribute, new_value)
    else:
        setattr(service_config.wcs_server, attribute, new_value)
        assert getattr(service_config.wcs_server, attribute) == expected_value
