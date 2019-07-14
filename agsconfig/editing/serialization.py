# coding=utf-8
"""This module contains functions to help with (de-)serialization."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

import datetime
import logging as _logging
import re

from collections import Sequence

#: A regular expression for matching time notation
_TIME_STRING_REGEX = re.compile(r"^([0-9]{2}):([0-9]{2})$")


def deserialize_csv_to_string_list(value, conversion, obj):
    if isinstance(value, list):
        return value

    if value is None or len(value) == 0:
        return []

    return [val for val in value.split(",")]


def deserialize_empty_string_to_none(value, conversion, obj):
    if isinstance(value, Sequence) and not isinstance(value, str):
        if len(value) == 0:
            return value
        return [deserialize_empty_string_to_none(v, conversion, obj) for v in value]

    return None if value == "" else value


def deserialize_formatted_to_string(value, conversion, obj):
    logger = _get_logger()

    # deal with a sequence of formatted strings
    if isinstance(value, Sequence) and not isinstance(value, str):
        if len(value) == 0:
            return value

        return [deserialize_formatted_to_string(v, conversion, obj) for v in value]

    if value is None:
        # no match to find
        return None

    # get format
    frmt = conversion["format"]

    # make sure format use "{}" notation and not "{0}" notation
    frmt = frmt.format("{}")

    # split string around format marker and escape parts
    frmt_parts = frmt.split("{}")
    frmt_parts = [re.escape(p) for p in frmt_parts]
    escaped_frmt = "{}".join(frmt_parts)

    # add capture group where format marker is
    pattern = escaped_frmt.format(r"(\w+)")

    # find matches
    logger.debug("Match pattern: %s", pattern)
    logger.debug("Value: %s", value)
    match = re.match(pattern, value)

    if match is None:
        raise ValueError("Could not find a matching value given the formatted string.")
    
    if len(match.groups()) > 1:
        raise ValueError("Too many matches found.  Value: {}; Format: {}".format(value, frmt))

    return match.groups(1)

def deserialize_string_to_bool(value, conversion, obj):
    if isinstance(value, Sequence) and not isinstance(value, str):
        if len(value) == 0:
            return value

        return [deserialize_string_to_bool(v, conversion, obj) for v in value]

    if value is True or value is False:
        # value has already been desrialized to native type
        return value

    if value is None:
        return None

    true = conversion.get("true", "true")
    false = conversion.get("false", "false")
    ignore_case = conversion.get("ignoreCase", True)
    default_true = conversion.get("defaultTrue", True)

    if ignore_case:
        value = value.upper()
        true = true.upper()
        false = false.upper()

    if default_true:
        return True if value == true else False
    else:
        if value == true:
            return True
        if value == false:
            return False
        raise ValueError("Cannot parse value '{0}' to boolean value.".format(value))


def deserialize_string_to_enum(value, conversion, obj):
    # check if value is a list
    if isinstance(value, Sequence) and not isinstance(value, str):
        if len(value) == 0:
            return value
        return [deserialize_string_to_enum(item, conversion, obj) for item in value]

    if value is None or value == "":
        return None

    enum = obj[conversion["enum"]]

    return enum(value)


def deserialize_string_to_number(value, conversion, obj):
    if isinstance(value, Sequence) and not isinstance(value, str):
        if len(value) == 0:
            return value

        return [deserialize_string_to_number(v, conversion, obj) for v in value]

    # If we already have a number
    if isinstance(value, (float, int)):
        return value

    # Or convert strings
    try:
        return int(value)
    except ValueError:
        pass

    # Or None
    if value is None or value == 'None':
        return None

    return float(value)


def deserialize_string_to_time(value, conversion, obj):
    if isinstance(value, Sequence) and not isinstance(value, str):
        if len(value) == 0:
            return value

        return [deserialize_string_to_time(v, conversion, obj) for v in value]

    if value is None:
        return None

    time_parts = value.split(":")
    return datetime.time(int(time_parts[0]), int(time_parts[1]))


def serialize_bool_to_string(value, conversion, obj):
    if isinstance(value, Sequence) and not isinstance(value, str):
        if len(value) == 0:
            return value

        return [serialize_bool_to_string(v, conversion, obj) for v in value]

    true = conversion["true"] if "true" in conversion else "true"
    false = conversion["false"] if "false" in conversion else "false"

    return true if _value_to_boolean(value) == True else false


def serialize_enum_to_string(value, conversion, obj):
    # check if value is a list
    if isinstance(value, Sequence) and not isinstance(value, str):
        if len(value) == 0:
            return value

        return [serialize_enum_to_string(item, conversion, obj) for item in value]

    enum = obj[conversion["enum"]]

    return _enum_to_str(value, enum, "Could not convert to a known value.")


def serialize_formatted_string(value, conversion, obj):
    # deak with a sequence
    if isinstance(value, Sequence) and not isinstance(value, str):
        if len(value) == 0:
            return value

        return [serialize_formatted_string(v, conversion, obj) for v in value]

    # get the format
    frmt = conversion["format"]

    # return the formatted value
    return frmt.format(value)


def serialize_number_to_string(value, conversion, obj):
    # Check if value is a list
    if isinstance(value, Sequence) and not isinstance(value, str):
        if len(value) == 0:
            return value

        return [serialize_number_to_string(item, conversion, obj) for item in value]

    # Already a string
    elif isinstance(value, str):
        # Check that its a number
        try:
            if float(value):
                return value
        except ValueError:
            raise ValueError

    # Number. Return a string.
    return str(repr(value))


def serialize_none_to_empty_string(value, conversion, obj):
    if isinstance(value, Sequence) and not isinstance(value, str):
        if len(value) == 0:
            return value

        return [serialize_none_to_empty_string(v, conversion, obj) for v in value]

    return "" if value is None else value


def serialize_string_list_to_csv(value, conversion, obj):
    # Already a comma separated string
    try:
        if len(value.split(',')) > 1:
            return value
    except:
        pass

    # Empty string
    if len(value) == 0:
        return ""

    # List of strings
    return ",".join(value)


def serialize_time_to_string(value, conversion, obj):
    if isinstance(value, Sequence) and not isinstance(value, str):
        if len(value) == 0:
            return value

        return [serialize_time_to_string(v, conversion, obj) for v in value]

    if value == None:
        return None

    if isinstance(value, str):
        # make sure string is a valid time
        value = deserialize_string_to_time(value, conversion, obj)

    return "{0:02d}:{1:02d}".format(value.hour, value.minute)


def _enum_to_str(value, enum, exception_message):
    if isinstance(value, (str, int)):
        # Convert string or int to enum to check compatibility
        # Raises ValueError if unknown value.
        value = enum(value)
    elif not isinstance(value, enum):
        # not a known capability, raise exception
        raise TypeError(exception_message)
    return value.value


def _get_logger():
    return _logging.getLogger(__name__)


def _value_to_boolean(value):
    """Converts true-ish and false-ish values to boolean."""
    try:
        value = value.upper()
        if value in ["TRUE", "T"]:
            return True
        elif value in ["FALSE", "F"]:
            return False
    except AttributeError:
        pass

    try:
        value = int(value)
        return True if value == 1 else False
    except (TypeError, ValueError):
        pass

    raise ValueError("Cannot convert value {0} to boolean.".format(value))
