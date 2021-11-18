# coding=utf-8
"""This module contains functions to help deal with strings."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

from aenum import IntEnum, StrEnum as _StrEnum

from ._strutils import caseless_equal as _caseless_equal


class StrEnum(_StrEnum):
    """String-based enum that can be found from a string whilst ignoring case."""
    @classmethod
    def _missing_value_(cls, value):
        """Handle the scenario where the input value is lowercase, which can happen from ArcGIS Server JSON for Axis Order."""

        if not isinstance(value, str):
            # can't ignore case on a non-string value
            return None

        for member in cls:
            if _caseless_equal(member.value, value):
                return member

        return None
