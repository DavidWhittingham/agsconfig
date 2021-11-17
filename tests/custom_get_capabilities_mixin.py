# coding=utf-8
"""Tests for ogc metadata attributes. """

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

import pytest

@pytest.mark.parametrize(#yapf:disable
    ('attribute', 'expected_value', 'exception'),
    [
        ('custom_get_capabilities', False, None),
        ('path_to_custom_get_capabilities_files', None, None)
    ]
)#yapf:enable
def test_custom_get_capabilities_getters(service_extension, attribute, expected_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            assert getattr(service_extension, attribute) == expected_value
    else:
        assert getattr(service_extension, attribute) == expected_value


@pytest.mark.parametrize(#yapf:disable
    ('attribute', 'new_value', 'expected_value', 'exception'),
    [
        ('custom_get_capabilities', False, False, None),
        ('custom_get_capabilities', True, True, None),
        ('custom_get_capabilities', 'x', None, ValueError),
        ('path_to_custom_get_capabilities_files', 'a:/path', 'a:/path', None)
    ]
)#yapf:enable
def test_custom_get_capabilities_setters(service_extension, attribute, new_value, expected_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(service_extension, attribute, new_value)
    else:
        setattr(service_extension, attribute, new_value)
        assert getattr(service_extension, attribute) == expected_value