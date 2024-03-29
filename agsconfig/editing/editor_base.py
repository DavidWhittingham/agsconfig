# coding=utf-8
"""This module contains the EditorBase base class for implementing ArcGIS service configuration editors."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

# Python lib imports
import inspect
import copy

from abc import ABCMeta, abstractmethod
from . import serialization


class EditorBase(object):
    """ Base class for implementing ArcGIS service configuration editors."""
    __metaclass__ = ABCMeta
    _format_id = None
    _deserialization_func_map = None
    _serialization_func_map = None

    def __init__(self, format_id, deserialization_func_map=None, serialization_func_map=None):
        self._format_id = format_id

        self._deserialization_func_map = {
            "boolToString": serialization.deserialize_string_to_bool,
            "enumToString": serialization.deserialize_string_to_enum,
            "formatString": serialization.deserialize_formatted_to_string,
            "htmlToText": lambda value, conversion, obj: value,
            "noneToEmptyString": serialization.deserialize_empty_string_to_none,
            "numberToString": serialization.deserialize_string_to_number,
            "olsonTimeZoneToWindowsTimeZone": serialization.deserialize_windows_tz_to_olson_tz,
            "stringToCsv": serialization.deserialize_csv_to_string_list,
            "timeToString": serialization.deserialize_string_to_time,
            "xmlToEscapedString": serialization.unescape_xml
        }

        if deserialization_func_map is not None:
            self._deserialization_func_map.update(deserialization_func_map)

        self._serialization_func_map = {
            "boolToString": serialization.serialize_bool_to_string,
            "enumToString": serialization.serialize_enum_to_string,
            "formatString": serialization.serialize_formatted_string,
            "htmlToText": serialization.html_to_text,
            "noneToEmptyString": serialization.serialize_none_to_empty_string,
            "numberToString": serialization.serialize_number_to_string,
            "olsonTimeZoneToWindowsTimeZone": serialization.serialize_olson_tz_to_windows_tz,
            "stringToCsv": serialization.serialize_string_list_to_csv,
            "timeToString": serialization.serialize_time_to_string,
            "xmlToEscapedString": serialization.escape_xml
        }

        if serialization_func_map is not None:
            self._serialization_func_map.update(serialization_func_map)

    def get_value(self, property_name, meta, obj):
        format_info = self._get_format_info_and_check_support(property_name, meta)

        # even if the result is in multiple locations, return only the first
        # resolve the "paths" variable itself in case that's a lambda
        path_info = self._resolve_lambda(self.resolve_lambda_value(format_info["paths"], obj)[0], obj, "path")

        value = self._get_value(path_info)

        conversions = None
        if "conversions" in format_info:
            # global conversions exist, use these
            conversions = format_info["conversions"]
        if "conversions" in path_info:
            # pre-path conversions exist, use these instead
            conversions = path_info["conversions"]

        if conversions:
            return self._deserialize(value, conversions, obj)
        return value

    @abstractmethod
    def save(self):
        """Save the current state of the edited config back to the input file object.

        Completely abstract function that is editor implementation specific.
        """
    def set_value(self, property_name, value, meta, obj):
        format_info = self._get_format_info_and_check_support(property_name, meta, True)

        # set the value in all locations listed
        # resolve the "paths" variable itself in case that's a lambda
        for path_info in self.resolve_lambda_value(format_info["paths"], obj):

            # try and get path-specific conversions, fall back to global conversions
            conversions = path_info.get("conversions", format_info.get("conversions"))

            if conversions:
                # serialize value, don't record the result against value, in case there is more than one path_info
                self._set_value(
                    self._serialize(value, conversions, obj), self._resolve_lambda(path_info, obj, "path"), obj
                )
            else:
                self._set_value(value, self._resolve_lambda(path_info, obj, "path"), obj)

    @classmethod
    def _resolve_lambda(cls, path_info, obj, key):
        # if the path is a lambda, get the arg names and assume they're in obj
        if callable(path_info[key]):
            # don't modify the original path_info object, it may need to be evaluated multiple times with different
            # arguments being passed, so return a shallow copy of the object with just the "path" key resolved
            path_info = copy.copy(path_info)

            path_info[key] = cls.resolve_lambda_value(path_info[key], obj)

        return path_info

    @staticmethod
    def resolve_lambda_value(path_or_lambda, obj):
        if callable(path_or_lambda):
            # python 2/3 code split here, inspect module has changed
            if hasattr(inspect, "signature"):
                # running on Py 3
                args = [param for param in inspect.signature(path_or_lambda).parameters]
            else:
                # running on Py 2
                args = [arg for arg in inspect.getargspec(path_or_lambda).args]

            kwargs = {}
            for arg in args:
                kwargs[arg] = getattr(obj, arg)
            path_or_lambda = path_or_lambda(**kwargs)

        return path_or_lambda

    @abstractmethod
    def _get_value(self, path_info):
        """Get the value at the provided path.

        Completely abstract function that is editor implementation specific.
        """
        pass

    @abstractmethod
    def _set_value(self, value, path_info, obj):
        """Set the value at the provided path.

        Completely abstract function that is editor implementation specific.
        """
        pass

    def _deserialize(self, value, conversions, obj):
        # a sequence of conversions has been specified for serializing, reverse the order to process
        for conversion in reversed(conversions):
            value = self._deserialization_func_map.get(conversion["id"])(value, conversion, obj)
        return value

    def _get_format_info_and_check_support(self, property_name, meta, check_constraints=False):
        # check if metadata exists for our format, throw exception if it does not
        if not self._format_id in meta["formats"]:
            raise NotImplementedError(
                "Support for the '{}' property has not been implemented on the '{}' configuration format.".format(
                    property_name, self._format_id
                )
            )

        format_info = meta["formats"][self._format_id]

        if check_constraints is True and "constraints" in format_info:
            constraints = format_info["constraints"]
            if constraints.get("readOnly", False):
                raise NotImplementedError(
                    "Setting the '{}' property on the '{}' configuration format is not permitted (property is read-only)."
                    .format(property_name, self._format_id)
                )

        return format_info

    def _serialize(self, value, conversions, obj):
        # a sequence of conversions has been specified for serializing, reverse the order to process
        for conversion in conversions:
            value = self._serialization_func_map.get(conversion["id"])(value, conversion, obj)
        return value
