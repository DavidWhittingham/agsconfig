"""This module contains the WCS Server extension class"""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

from ..editing.edit_prop import EditorProperty
from .extension_base import ExtensionBase
from .ogc_metadata_extension_mixin import OGCMetadataExtensionMixin
from .custom_get_capabilities_extension_mixin import CustomGetCapabilitiesExtensionMixin


class WCSServerExtension(OGCMetadataExtensionMixin, CustomGetCapabilitiesExtensionMixin, ExtensionBase):
    """ WCS server extension properties for arcGIS services """

    # ArcGIS Server JSON key names
    _AGSJSON_KEY_ADMINISTRATIVE_AREA = "province"
    _AGSJSON_KEY_EMAIL = "email"
    _AGSJSON_KEY_FACSIMILE = "fax"
    _AGSJSON_KEY_INDIVIDUAL_NAME = "responsiblePerson"
    _AGSJSON_KEY_KEYWORDS = "keywords"
    _AGSJSON_KEY_POSITION_NAME = "responsiblePosition"
    _AGSJSON_KEY_POSTAL_CODE = "zipcode"

    # Service Definition Draft key names
    _SDDRAFT_KEY_ADMINISTRATIVE_AREA = "province"
    _SDDRAFT_KEY_EMAIL = "email"
    _SDDRAFT_KEY_FACSIMILE = "fax"
    _SDDRAFT_KEY_INDIVIDUAL_NAME = "responsiblePerson"
    _SDDRAFT_KEY_KEYWORDS = "keywords"
    _SDDRAFT_KEY_POSITION_NAME = "responsiblePosition"
    _SDDRAFT_KEY_POSTAL_CODE = "zipcode"

    def __init__(self, editor):
        super().__init__(editor, "WCSServer")

    provider_site = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {#yapf: disable
                            "path": lambda extension_name:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='providerWebsite']/Value".format(extension_name),
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
                                                    "value": "providerWebsite"
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
                                                    "tag": "Props",
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
                        }#yapf: enable
                    ]
                }
            }
        }
    )