# coding=utf-8
"""Tests for serialization.py."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

# standard lib imports
import datetime

# third-party imports
import pytest

# local imports
from agsconfig import MapServer
from agsconfig.editing import serialization


#yapf: disable
@pytest.mark.parametrize(
    ("value", "expected", "exception"),
    [
        (("","",""), [None, None, None], None),
        ([], [], None)
    ]
)#yapf:enable
def test_deserialize_empty_string_to_none(value, expected, exception):
    if exception is not None:
        with pytest.raises(exception):
            assert serialization.deserialize_empty_string_to_none(value, None, None) == expected
    else:
        assert serialization.deserialize_empty_string_to_none(value, None, None) == expected


#yapf: disable
@pytest.mark.parametrize(
    ("value", "conversion", "expected", "exception"),
    [
        ("true", {"id" : "boolToString"}, True, None),
        ("false", {"id" : "boolToString"}, False, None),
        (("false", "true"), {"id" : "boolToString"}, [False, True], None),
        ("123", {"id" : "boolToString", "defaultTrue" : False}, None, ValueError),
        ([], {"id" : "boolToString"}, [], None),
        ("TRUE", {"id" : "boolToString", "defaultTrue" : False}, True, None),
        ("FALSE", {"id" : "boolToString", "defaultTrue" : False}, False, None)
    ]
)#yapf:enable
def test_deserialize_string_to_bool(value, conversion, expected, exception):
    if exception is not None:
        with pytest.raises(exception):
            serialization.deserialize_string_to_bool(value, conversion, None)
    else:
        assert serialization.deserialize_string_to_bool(value, conversion, None) == expected


#yapf: disable
@pytest.mark.parametrize(
    ("value", "conversion", "expected", "exception"),
    [
        ("", {"enum" : "Capabilities", "id" : "enumToString"}, None, None)
    ]
)#yapf:enable
def test_deserialize_string_to_enum(value, conversion, expected, exception):
    if exception is not None:
        with pytest.raises(exception):
            serialization.deserialize_string_to_enum(value, conversion, None)
    else:
        assert serialization.deserialize_string_to_enum(value, conversion, None) == expected


#yapf: disable
@pytest.mark.parametrize(
    ("value", "conversion", "expected", "exception"),
    [
        ([], {"enum" : "Capabilities", "id" : "enumToString"}, [], None),
        (["12:00", "14:00"], {"enum" : "Capabilities", "id" : "enumToString"}, [datetime.time(12, 0), datetime.time(14, 0)], None)
    ]
)#yapf:enable
def test_deserialize_string_to_time(value, conversion, expected, exception):
    if exception is not None:
        with pytest.raises(exception):
            serialization.deserialize_string_to_time(value, conversion, None)
    else:
        assert serialization.deserialize_string_to_time(value, conversion, None) == expected


#yapf: disable
@pytest.mark.parametrize(
    ("value", "conversion", "expected", "exception"),
    [
        ([], {"enum" : "Capabilities", "id" : "enumToString"}, [], None),
        (["1", "2"], {"enum" : "Capabilities", "id" : "enumToString"}, [1, 2], None)
    ]
)#yapf:enable
def test_deserialize_string_to_number(value, conversion, expected, exception):
    if exception is not None:
        with pytest.raises(exception):
            serialization.deserialize_string_to_number(value, conversion, None)
    else:
        assert serialization.deserialize_string_to_number(value, conversion, None) == expected


#yapf: disable
@pytest.mark.parametrize(
    ("value", "conversion", "expected", "exception"),
    [
        (True, {"enum" : "Capabilities", "id" : "enumToString"}, "true", None),
        ([True, False], {"enum" : "Capabilities", "id" : "enumToString"}, ["true", "false"], None),
        ([], {"enum" : "Capabilities", "id" : "enumToString"}, [], None),
    ]
)#yapf:enable
def test_serialize_bool_to_string(value, conversion, expected, exception):
    if exception is not None:
        with pytest.raises(exception):
            serialization.serialize_bool_to_string(value, conversion, None)
    else:
        assert serialization.serialize_bool_to_string(value, conversion, None) == expected


#yapf: disable
@pytest.mark.parametrize(
    ("value", "conversion", "expected", "exception"),
    [
        (1, {"enum" : "Capabilities", "id" : "enumToString"}, "1", None),
        ([1, 2], {"enum" : "Capabilities", "id" : "enumToString"}, ["1", "2"], None),
        ([], {"enum" : "Capabilities", "id" : "enumToString"}, [], None)
    ]
)#yapf:enable
def test_serialize_number_to_string(value, conversion, expected, exception):
    if exception is not None:
        with pytest.raises(exception):
            serialization.serialize_number_to_string(value, conversion, None)
    else:
        assert serialization.serialize_number_to_string(value, conversion, None) == expected


#yapf: disable
@pytest.mark.parametrize(
    ("value", "conversion", "expected", "exception"),
    [
        (None, {"enum" : "Capabilities", "id" : "enumToString"}, "", None),
        ([None, None], {"enum" : "Capabilities", "id" : "enumToString"}, ["", ""], None),
        ([], {"enum" : "Capabilities", "id" : "enumToString"}, [], None)
    ]
)#yapf:enable
def test_serialize_none_to_empty_string(value, conversion, expected, exception):
    if exception is not None:
        with pytest.raises(exception):
            serialization.serialize_none_to_empty_string(value, conversion, None)
    else:
        assert serialization.serialize_none_to_empty_string(value, conversion, None) == expected


#yapf: disable
@pytest.mark.parametrize(
    ("value", "conversion", "expected", "exception"),
    [
        (None, {"enum" : "Capabilities", "id" : "enumToString"}, None, None),
        ([None, None], {"enum" : "Capabilities", "id" : "enumToString"}, [None, None], None),
        ([], {"enum" : "Capabilities", "id" : "enumToString"}, [], None)
    ]
)#yapf:enable
def test_serialize_time_to_string(value, conversion, expected, exception):
    if exception is not None:
        with pytest.raises(exception):
            serialization.serialize_time_to_string(value, conversion, None)
    else:
        assert serialization.serialize_time_to_string(value, conversion, None) == expected
