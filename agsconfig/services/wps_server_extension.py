"""Edit WPS server extension properties for ArcGIS geoprocessing services."""
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()

from enum import Enum
from ..editing.edit_prop import EditorProperty
from .extension_base import ExtensionBase
from .ogc_metadata_extension_mixin import OGCMetadataExtensionMixin
from .custom_get_capabilities_extension_mixin import CustomGetCapabilitiesExtensionMixin


class WPSServerExtension(OGCMetadataExtensionMixin, CustomGetCapabilitiesExtensionMixin, ExtensionBase):
    """ WMS server extension properties for arcGIS services """

    _agsjson_key_address = "deliveryPoint"
    _sddraft_key_address = "deliveryPoint"

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

    contact_instructions = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='contactInstructions']/Value".format(extension_name)
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    facsimile = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='facsimile']/Value".format(extension_name)
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    hours_of_service = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='hoursOfService']/Value".format(extension_name)
                        }# yapf: enable
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
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='individualName']/Value".format(extension_name)
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    organisation = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='organisation']/Value".format(extension_name)
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    phone = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='phone']/Value".format(extension_name)
                        }# yapf: enable
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
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='positionName']/Value".format(extension_name)
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    postal_code = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='postalCode']/Value".format(extension_name)
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    keywords_type = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='keywordsType']/Value".format(extension_name)
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    profile = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='profile']/Value".format(extension_name)
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    provider_name = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='providerName']/Value".format(extension_name)
                        }# yapf: enable
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
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='role']/Value".format(extension_name)
                        }# yapf: enable
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
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='serviceTypeVersion']/Value".format(extension_name)
                        }# yapf: enable
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
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='serviceType']/Value".format(extension_name)
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    fee = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='fee']/Value".format(extension_name)
                        }# yapf: enable
                    ]
                }
            }
        }
    )
