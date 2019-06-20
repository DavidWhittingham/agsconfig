# coding=utf-8
"""This module contains the ExtensionBase abstract base class for implementing ArcGIS Server service extensions."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
from future.utils import raise_
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

# Python lib imports
import logging as _logging
import sys as _sys

from abc import ABCMeta

# Third-party package imports
from enum import Enum

# Local package imports
from ..editing.edit_prop import EditorProperty
from ..model_base import ModelBase


class ExtensionBase(ModelBase):
    """Contains base settings/configuration that are common across ArcGIS Service extensions."""

    __metaclass__ = ABCMeta

    _editor = None
    _extension_name = None
    _logger = _logging.getLogger(__name__)
    _web_capabilities_key = "WebCapabilities"

    class Capability(Enum):
        """Must be overridden by sub-classes if any capabilities are supported."""
        pass

    def __init__(self, editor, extension_name):
        """Initilises the class.

        Args:
            editor: An editor object that will receive metadata about each property
            extension_name: Used to find xpaths in sddrafts where there is more than one extension
        """

        self._editor = editor
        self._extension_name = extension_name

    @property
    def extension_name(self):
        return self._extension_name

    def _set_props_from_dict(self, prop_dict, ignore_not_implemented=False):
        """Method for setting properties from a dictionary where keys match property names."""
        for key, value in prop_dict.items():
            if hasattr(self, key):
                try:
                    setattr(self, key, value)
                except AttributeError:
                    getattr(self, key)._set_props_from_dict(value, ignore_not_implemented)
                except NotImplementedError:
                    t, v, tb = _sys.exc_info()
                    if ignore_not_implemented:
                        self._logger.warning(
                            "Tried to set the '{}' property to '{}', but this is not supported on the supplied configuration format."
                            .format(key, value)
                        )
                    else:
                        raise_(t, v, tb)

    capabilities = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name, _web_capabilities_key: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Info/PropertyArray/PropertySetProperty[Key='{1}']/Value".format(extension_name, _web_capabilities_key)
                        }
                    ],
                    "conversions": [{
                        "id": "enumToString",
                        "enum": "Capability"
                    }, {
                        "id": "stringToCsv"
                    }]
                }
            }
        }
    )

    enabled = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "conversions": [{
                        "id": "boolToString",
                        "true": "true",
                        "false": "false"
                    }],
                    "paths": [
                        {
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{0}')].enabled".format(extension_name)
                        }
                    ]
                },
                "sddraft": {
                    "conversions": [{
                        "id": "boolToString"
                    }],
                    "paths": [
                        {
                            "path":
                            lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Enabled".format(extension_name)
                        }
                    ]
                }
            }
        })
