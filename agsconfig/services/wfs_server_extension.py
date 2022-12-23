"""This module contains the WFS Server extension class"""

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


class WFSServerExtension(OGCMetadataExtensionMixin, CustomGetCapabilitiesExtensionMixin, ExtensionBase):
    """ WMS server extension properties for arcGIS services """

    # ArcGIS Server JSON key names
    _AGSJSON_KEY_ADDRESS = "deliveryPoint"

    # Service Definition Draft key names
    _SDDRAFT_KEY_ADDRESS = "deliveryPoint"

    class AxisOrder(Enum):
        lat_long = "LatLong"
        long_lat = "LongLat"

    def __init__(self, editor):
        super().__init__(editor, "WFSServer")

    app_schema_uri = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "conversions": [
                        {"id": "noneToEmptyString"}
                    ],
                    "paths": [
                        {
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties.appSchemaURI".format(extension_name)
                        }
                    ]
                },
                "sddraft": {
                    "conversions": [
                        {"id": "noneToEmptyString"}
                    ],
                    "paths": [
                        { # yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='appSchemaURI']/Value".format(extension_name)
                        } # yapf: enable
                    ]
                }
            }
        }
    )

    app_schema_prefix = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "conversions": [
                        {"id": "noneToEmptyString"}
                    ],
                    "paths": [
                        {
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties.appSchemaPrefix".format(extension_name)
                        }
                    ]
                },
                "sddraft": {
                    "conversions": [
                        {"id": "noneToEmptyString"}
                    ],
                    "paths": [
                        { # yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='appSchemaPrefix']/Value".format(extension_name)
                        } # yapf: enable
                    ]
                }
            }
        }
    )

    axis_order_wfs_10 = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "conversions": [{
                        "id": "enumToString",
                        "enum": "AxisOrder",
                        "case": "lower"
                    }],
                    "paths": [
                        {
                            "document": "main",
                            "path": lambda extension_name:
                            "$.extensions[?(@.typeName = '{}')].properties.axisOrderWFS10".format(extension_name)
                        }
                    ]
                },
                "sddraft": {
                    "conversions": [{
                        "id": "enumToString",
                        "enum": "AxisOrder"
                    }],
                    "paths": [
                        {
                            "path": lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='axisOrderWFS10']/Value"
                            .format(extension_name)
                        }
                    ]
                }
            }
        }
    )

    axis_order_wfs_11 = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "conversions": [{
                        "id": "enumToString",
                        "enum": "AxisOrder",
                        "case": "lower"
                    }],
                    "paths": [
                        { #yapf:disable
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties.axisOrderWFS11".format(extension_name)
                        } #yapf:enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        { #yapf:disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='axisOrderWFS11']/Value".format(extension_name)
                        } #yapf:enable
                    ],
                    "conversions": [{
                        "id": "enumToString",
                        "enum": "AxisOrder"
                    }]
                }
            }
        }
    )

    contact_instructions = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "conversions": [
                        {"id": "noneToEmptyString"}
                    ],
                    "paths": [
                        { #yapf:disable
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties.contactInstructions".format(extension_name)
                        } #yapf:enable
                    ]
                },
                "sddraft": {
                    "conversions": [
                        {"id": "noneToEmptyString"}
                    ],
                    "paths": [
                        { #yapf:disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='contactInstructions']/Value".format(extension_name)
                        } #yapf:enable
                    ]
                }
            }
        }
    )

    enable_transactions = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "conversions": [
                        {
                            "id": "boolToString",
                            "allowNone": False,
                            "noneAsFalse": True
                        }
                    ],
                    "paths": [
                        { #yapf:disable
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties.enableTransactions".format(extension_name)
                        } #yapf:enable
                    ]
                },
                "sddraft": {
                    "conversions": [
                        {
                            "id": "boolToString",
                            "allowNone": False,
                            "noneAsFalse": True
                        }
                    ],
                    "paths": [
                        { #yapf:disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='enableTransactions']/Value".format(extension_name)
                        } #yapf:enable
                    ]
                }
            }
        }
    )

    hours_of_service = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "conversions": [
                        {"id": "noneToEmptyString"}
                    ],
                    "paths": [
                        { #yapf:disable
                             # note: As of ArcGIS Server 10.7.1, the Manager interface writes this into config as 
                             # "hourOrService", but that is incorrect (in that the WFS Capabilities XML produced by 
                             # AGS won't use the value from that key).  The correct key is "hoursOfService".
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties.hoursOfService".format(extension_name),
                            "parent": {
                                "children": [{
                                    "key": "hoursOfService"
                                }]
                            }
                        } #yapf:enable
                    ]
                },
                "sddraft": {
                    "conversions": [
                        {"id": "noneToEmptyString"}
                    ],
                    "paths": [
                        { #yapf:disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='hoursOfService']/Value".format(extension_name)
                        } #yapf:enable
                    ]
                }
            }
        }
    )

    provider_site = EditorProperty(
        {
            "conversions": [
                {"id": "noneToEmptyString"}
            ],
            "formats": {
                "agsJson": {

                    "paths": [
                        { #yapf:disable
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties.providerSite".format(extension_name)
                        } #yapf:enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        { #yapf:disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='providerSite']/Value".format(extension_name)
                        } #yapf:enable
                    ]
                }
            }
        }
    )

    service_type = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "conversions": [
                        {"id": "noneToEmptyString"}
                    ],
                    "paths": [
                        { #yapf:disable
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties.serviceType".format(extension_name)
                        } #yapf:enable
                    ]
                },
                "sddraft": {
                    "conversions": [
                        {"id": "noneToEmptyString"}
                    ],
                    "paths": [
                        { #yapf:disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='serviceType']/Value".format(extension_name)
                        } #yapf:enable
                    ]
                }
            }
        }
    )

    service_type_version = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "conversions": [
                        {"id": "noneToEmptyString"}
                    ],
                    "paths": [
                        { #yapf:disable
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties.serviceTypeVersion".format(extension_name)
                        } #yapf:enable
                    ]
                },
                "sddraft": {
                    "conversions": [
                        {"id": "noneToEmptyString"}
                    ],
                    "paths": [
                        { #yapf:disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='serviceTypeVersion']/Value".format(extension_name)
                        } #yapf:enable
                    ]
                }
            }
        }
    )
