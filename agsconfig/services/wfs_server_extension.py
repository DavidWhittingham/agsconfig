"""This module contains the WFS Server extension class"""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

from enum import Enum
from ..editing.edit_prop import EditorProperty
from .extension_base import ExtensionBase
from .ogc_metadata_extension_mixin import OGCMetadataExtensionMixin
from .custom_get_capabilities_extension_mixin import CustomGetCapabilitiesExtensionMixin


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
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='appSchemaURI']/Value".format(extension_name)
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    app_schema_prefix = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='appSchemaPrefix']/Value".format(extension_name)
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    axis_order_wfs_10 = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='axisOrderWFS10']/Value"
                            .format(extension_name)
                        }
                    ],
                    "conversions": [{
                        "id": "enumToString",
                        "enum": "AxisOrder"
                    }]
                }
            }
        }
    )

    axis_order_wfs_11 = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='axisOrderWFS11']/Value"
                            .format(extension_name)
                        }
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
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='contactInstructions']/Value"
                            .format(extension_name)
                        }
                    ]
                }
            }
        }
    )

    enable_transactions = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='enableTransactions']/Value"
                            .format(extension_name)
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    hours_of_service = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='hoursOfService']/Value"
                            .format(extension_name)
                        }
                    ]
                }
            }
        }
    )

    individual_name = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='individualName']/Value"
                            .format(extension_name)
                        }
                    ]
                }
            }
        }
    )

    position_name = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='positionName']/Value"
                            .format(extension_name)
                        }
                    ]
                }
            }
        }
    )

    provider_site = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='providerSite']/Value"
                            .format(extension_name)
                        }
                    ]
                }
            }
        }
    )

    service_type = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='serviceType']/Value"
                            .format(extension_name)
                        }
                    ]
                }
            }
        }
    )

    service_type_version = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='serviceTypeVersion']/Value"
                            .format(extension_name)
                        }
                    ]
                }
            }
        }
    )
