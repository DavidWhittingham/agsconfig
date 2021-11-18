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

import unicodedata as _unicodedata


def caseless_equal(left, right):
    return normalize_caseless(left) == normalize_caseless(right)


def normalize_caseless(text):
    if hasattr(text, "casefold"):
        # use casefold on Py3 to normalize correctly
        return _unicodedata.normalize("NFKD", text.casefold())

    # Python 2 or other weird non-casefoldable string, just use upper/lower as fallback
    return text.upper().lower()