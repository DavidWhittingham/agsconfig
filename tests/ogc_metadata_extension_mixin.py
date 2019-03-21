# coding=utf-8
"""Tests for ogc metadata attributes. """

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

import pytest


@pytest.mark.parametrize(
    ('attribute', 'expectedValue', 'exception'),
    [
        ('britney_spears', 'should cause an', AttributeError),  # because she isn't a member
        ('abstract', 'This is the abstract.', None),
        ('access_constraints', 'There are no access constraints.', None),
        ('city', 'Brisbane', None),
        ('country', 'Australia', None),
        ('keywords', 'These Are Keywords', None),
        ('fees', 'The are no fees.', None),
        ('name', 'Test_Service', None),
        ('title', 'Test Service', None),
    ]
)
def test_ogc_getters(service_config, service_extension, attribute, expectedValue, exception):
    if exception is not None:
        with pytest.raises(exception):
            assert getattr(service_config[service_extension], attribute) == expectedValue
    else:
        assert getattr(service_config[service_extension], attribute) == expectedValue


@pytest.mark.parametrize(
    ('attribute', 'new_value', 'exception'),
    [
        ('britney_spears', 'should cause an', TypeError),  # because she isn't a member
        ('abstract', 'This is the new abstract.', None),
        ('access_constraints', 'Access is not allowed.', None),
        ('city', 'Panama City', None),
        ('country', 'Republic of Panama', None),
        ('keywords', 'These Are Also Keywords', None),
        ('fees', 'nil', None),
        ('name', 'FooBar_Service', None),
        ('title', 'The FooBar Service', None),
    ]
)
def test_ogc_setters(service_config, service_extension, attribute, new_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(service_config[service_extension], attribute, new_value)
            assert getattr(service_config[service_extension], attribute) == new_value
    else:
        setattr(service_config[service_extension], attribute, new_value)
        assert getattr(service_config[service_extension], attribute) == new_value
