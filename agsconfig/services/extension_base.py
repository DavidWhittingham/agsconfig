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

# Python lib imports
import logging as _logging

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

    _AGSJSON_EXTENSION_STRUCTURE = {"children": [{"value": lambda extension_name: {"typeName": extension_name}}]}

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

    capabilities = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {# yapf: disable
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{0}')].capabilities".format(extension_name),
                            "parent": {
                                "children": [
                                    {
                                        "key": "capabilities"
                                    }
                                ],
                                "parent": _AGSJSON_EXTENSION_STRUCTURE
                            }
                        }# yapf: enable
                    ],
                    "conversions": [{
                        "id": "enumToString",
                        "enum": "Capability"
                    }, {
                        "id": "stringToCsv"
                    }],
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _web_capabilities_key: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Info/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _web_capabilities_key),
                            "parent": {
                                "children": [
                                    {
                                        "tag": "Value",
                                        "attributes": {
                                            "{http://www.w3.org/2001/XMLSchema-instance}type": "xs:string"
                                        },
                                    }
                                ],
                                "parent": {
                                    "children": [
                                        {
                                            "tag": "PropertySetProperty",
                                            "attributes": {
                                                "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:PropertySetProperty"
                                            },
                                            "children": [
                                                {
                                                    "tag": "Key",
                                                    "value": lambda _web_capabilities_key: "{}".format(_web_capabilities_key)
                                                }
                                            ]
                                        }
                                    ],
                                    "parent":{
                                        "children": [
                                            {
                                                "tag": "PropertyArray",
                                                "attributes": {
                                                    "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:ArrayOfPropertySetProperty"
                                                }
                                            }
                                        ],
                                        "parent": {
                                            "children": [
                                                {
                                                    "tag": "Info",
                                                    "attributes": {
                                                        "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:PropertySet"
                                                    }
                                                }
                                            ],
                                            "parent": {
                                                "children": [
                                                    {
                                                        "tag": "SVCExtension",
                                                        "attributes": {
                                                            "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:SVCExtension"
                                                        },
                                                        "children": [
                                                            {
                                                                "tag": "TypeName",
                                                                "value": lambda extension_name: "{}".format(extension_name)
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        }
                                    }
                                }
                            }
                        }# yapf: enable
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
                        "id": "boolToString"
                    }],
                    "paths": [
                        {# yapf: disable
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{0}')].enabled".format(extension_name),
                            "parent": {
                                "children": [
                                    {
                                        "key": "enabled"
                                    }
                                ],
                                "parent": _AGSJSON_EXTENSION_STRUCTURE
                            }
                        }
                    ]
                },
                "sddraft": {
                    "conversions": [{
                        "id": "boolToString"
                    }],
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Enabled".format(extension_name),
                            "parent": {
                                "children": [
                                    {
                                        "tag": "Enabled"
                                    }
                                ],
                                "parent": {
                                    "children": [
                                        {
                                            "tag": "SVCExtension",
                                            "attributes": {
                                                "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:SVCExtension"
                                            },
                                            "children": [
                                                {
                                                    "tag": "TypeName",
                                                    "value": lambda extension_name: "{}".format(extension_name)
                                                }
                                            ]
                                        }
                                    ]
                                }
                            }
                        }# yapf: enable
                    ]
                }
            }
        }
    )
