"""This module contains the WMS Server extension class"""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

from .extension_base import ExtensionBase
from .ogc_metadata_extension_mixin import OGCMetadataExtensionMixin
from .custom_get_capabilities_extension_mixin import CustomGetCapabilitiesExtensionMixin
from ..editing.edit_prop import EditorProperty
from .._enum import StrEnum as Enum


class WMSServerExtension(OGCMetadataExtensionMixin, CustomGetCapabilitiesExtensionMixin, ExtensionBase):
    """ WMS server extension properties for arcGIS services """

    # ArcGIS Server JSON key names
    _AGSJSON_KEY_ADMINISTRATIVE_AREA = "stateOrProvince"
    _AGSJSON_KEY_EMAIL = "contactElectronicMailAddress"
    _AGSJSON_KEY_FACSIMILE = "contactFacsimileTelephone"
    _AGSJSON_KEY_INDIVIDUAL_NAME = "contactPerson"
    _AGSJSON_KEY_PHONE = "contactVoiceTelephone"
    _AGSJSON_KEY_POSITION_NAME = "contactPosition"
    _AGSJSON_KEY_POSTAL_CODE = "postCode"
    _AGSJSON_KEY_PROVIDER_NAME = "contactOrganization"

    # Service Definition Draft key names
    _SDDRAFT_KEY_ADMINISTRATIVE_AREA = "stateOrProvince"
    _SDDRAFT_KEY_EMAIL = "contactElectronicMailAddress"
    _SDDRAFT_KEY_FACSIMILE = "contactFacsimileTelephone"
    _SDDRAFT_KEY_INDIVIDUAL_NAME = "contactPerson"
    _SDDRAFT_KEY_PHONE = "contactVoiceTelephone"
    _SDDRAFT_KEY_POSITION_NAME = "contactPosition"
    _SDDRAFT_KEY_POSTAL_CODE = "postCode"
    _SDDRAFT_KEY_PROVIDER_NAME = "contactOrganization"

    class Capability(Enum):
        get_capabilities = "GetCapabilities"
        get_map = "GetMap"
        get_feature_info = "GetFeatureInfo"
        get_styles = "GetStyles"
        get_legend_graphic = "GetLegendGraphic"
        get_schema_extension = "GetSchemaExtension"

    def __init__(self, editor):
        super().__init__(editor, "WMSServer")

    additional_spatial_ref_sys = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{0}')].properties.listSupportedCRS".format(extension_name),
                            "parent": {
                                "children": [{
                                    "key": "listSupportedCRS"
                                }],
                                "parent": lambda _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE: _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE
                            }
                        }
                    ],
                    "conversions": [{
                        "id": "stringToCsv"
                    }],
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='ListSupportedCRS']/Value".format(extension_name),
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
                                                    "value": "ListSupportedCRS"
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
                        }# yapf: enable
                    ],
                    "conversions": [{
                        "id": "stringToCsv"
                    }]
                }
            }
        }
    )

    address_type = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{0}')].properties.addressType".format(extension_name),
                            "parent": {
                                "children": [{
                                    "key": "addressType"
                                }],
                                "parent": lambda _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE: _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE
                            }
                        }
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='addressType']/Value".format(extension_name),
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
                                                    "value": "addressType"
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
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    inherit_layer_names = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {# yapf: disable
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{0}')].properties.inheritLayerNames".format(extension_name),
                            "parent": {
                                "children": [{
                                    "key": "inheritLayerNames"
                                }],
                                "parent": lambda _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE: _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE
                            }
                        }# yapf: enable
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }],
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='inheritLayerNames']/Value".format(extension_name),
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
                                                    "value": "inheritLayerNames"
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
                        }# yapf: enable
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    name = EditorProperty(
        {
            "constraints": {
                "notEmpty": True
            },
            "formats": {
                "agsJson": {
                    "paths": [
                        {# yapf: disable
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{0}')].properties.name".format(extension_name),
                            "parent": {
                                "children": [{
                                    "key": "name"
                                }],
                                "parent": lambda _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE: _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE
                            }
                        }# yapf: enable
                    ],
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='name']/Value".format(extension_name),
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
                                                    "value": "name"
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
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    path_to_custom_sld_file = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {# yapf: disable
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{0}')].properties.pathToCustomSLDFile".format(extension_name),
                            "parent": {
                                "children": [{
                                    "key": "pathToCustomSLDFile"
                                }],
                                "parent": lambda _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE: _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE
                            }
                        }# yapf: enable
                    ],
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='pathToCustomSLDFile']/Value".format(extension_name),
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
                                                    "value": "pathToCustomSLDFile"
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
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    reaspect = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {# yapf: disable
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{0}')].properties.reaspect".format(extension_name),
                            "parent": {
                                "children": [{
                                    "key": "reaspect"
                                }],
                                "parent": lambda _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE: _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE
                            }
                        }# yapf: enable
                    ],
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='Reaspect']/Value".format(extension_name),
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
                                                    "value": "Reaspect"
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
                        }# yapf: enable
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )