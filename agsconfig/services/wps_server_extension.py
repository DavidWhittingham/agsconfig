"""This module contains the WPS Server extension class"""

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


class WPSServerExtension(OGCMetadataExtensionMixin, CustomGetCapabilitiesExtensionMixin, ExtensionBase):
    """ WPS server extension properties for ArcGIS services """

    # ArcGIS Server JSON key names
    _AGSJSON_KEY_ADDRESS = "deliveryPoint"
    _AGSJSON_KEY_FEES = "fee"

    # Service Definition Draft key names
    _SDDRAFT_KEY_ADDRESS = "deliveryPoint"
    _SDDRAFT_KEY_FEES = "fee"

    class Capability(Enum):
        get_capabilities = "GetCapabilities"
        get_map = "GetMap"
        get_feature_info = "GetFeatureInfo"
        get_styles = "GetStyles"
        get_legend_graphic = "GetLegendGraphic"
        get_schema_extension = "GetSchemaExtension"

    def __init__(self, editor):
        super().__init__(editor, "WPSServer")

    app_schema_prefix = EditorProperty(
        {
            "conversions": [
                {"id": "noneToEmptyString"}
            ],
            "formats": {
                "agsJson": {
                    "paths": [
                        { #yapf:disable
                            "document": "main",
                            "path":
                                lambda extension_name:
                                    "$.extensions[?(@.typeName = '{}')].properties.appSchemaPrefix".format(extension_name)
                        } #yapf:enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        { # yapf: disable
                            "path":
                                lambda extension_name:
                                    "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='appSchemaPrefix']/Value".format(extension_name)
                        } # yapf: enable
                    ]
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
                            "path":
                                lambda extension_name:
                                    "$.extensions[?(@.typeName = '{}')].properties.contactInstructions".format(extension_name)
                        } #yapf:enable
                    ]
                },
                "sddraft": {
                    "conversions": [
                        {"id": "noneToEmptyString"}
                    ],
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='contactInstructions']/Value".format(extension_name)
                        }# yapf: enable
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
                            "document": "main",
                            "path":
                                lambda extension_name:
                                    "$.extensions[?(@.typeName = '{}')].properties.hoursOfService".format(extension_name)
                        } #yapf:enable
                    ]
                },
                "sddraft": {
                    "conversions": [
                        {"id": "noneToEmptyString"}
                    ],
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='hoursOfService']/Value".format(extension_name)
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    provider_site = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "conversions": [
                        {"id": "noneToEmptyString"}
                    ],
                    "paths": [
                        { #yapf:disable
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties.providerSite".format(extension_name)
                        } #yapf:enable
                    ]
                },
                "sddraft": {
                    "conversions": [
                        {"id": "noneToEmptyString"}
                    ],
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='providerSite']/Value".format(extension_name)
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    role = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "conversions": [
                        {"id": "noneToEmptyString"}
                    ],
                    "paths": [
                        { #yapf:disable
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties.role".format(extension_name)
                        } #yapf:enable
                    ]
                },
                "sddraft": {
                    "conversions": [
                        {"id": "noneToEmptyString"}
                    ],
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='role']/Value".format(extension_name)
                        }# yapf: enable
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
