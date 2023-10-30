# coding=utf-8
"""This module contains the ExtensionBase abstract base class for implementing ArcGIS Server service extensions."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

from abc import ABCMeta

# Local package imports
from .extension_base import ExtensionBase


class SoiExtensionBase(ExtensionBase):
    """Contains base settings/configuration that are common across ArcGIS Server Object Interceptor extensions."""

    __metaclass__ = ABCMeta

    _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE = {
        "children": [
            {
                "key": "properties",
                "value": {
                    "supportsREST": "false",
                    "supportsSOAP": "false",
                    "supportsInterceptor": "true"
                }
            }
        ],
        "parent": lambda _AGSJSON_EXTENSION_STRUCTURE: _AGSJSON_EXTENSION_STRUCTURE
    }