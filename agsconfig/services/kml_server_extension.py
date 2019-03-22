"""This module contains the kml Server extension class"""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

from enum import Enum
from ..editing.edit_prop import EditorProperty
from .extension_base import ExtensionBase
from .ogc_metadata_extension_mixin import OGCMetadataExtensionMixin
from .custom_get_capabilities_extension_mixin import CustomGetCapabilitiesExtensionMixin

class KmlServerExtension(OGCMetadataExtensionMixin, CustomGetCapabilitiesExtensionMixin, ExtensionBase):
    """ Kml server extension properties for arcGIS services """

    class Capability(Enum):
        single_image = "SingleImage"
        separate_images = "SeparateImages"
        vectors = "Vectors"

    class CompatibilityMode(Enum):
        google_earth = "GoogleEarth"
        google_maps = "GoogleMaps"
        google_mobile = "GoogleMobile"

    def __init__(self, editor):
        super().__init__(editor, "KmlServer")

    capabilities = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name : "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Info/PropertyArray/PropertySetProperty[Key='WebCapabilities']/Value".format(extension_name)
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

    compatibility_mode = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name : "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='compatibilityMode']/Value".format(extension_name)
                        }
                    ],
                    "conversions": [{
                        "id": "enumToString",
                        "enum": "CompatibilityMode"
                    }, {
                        "id": "stringToCsv"
                    }]
                }
            }
        }
    )
    
    dpi = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name : "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='dpi']/Value".format(extension_name)
                        }
                    ]
                }
            }
        })

    feature_limit = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name : "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='featureLimit']/Value".format(extension_name)
                        }
                    ]
                }
            }
        })

    image_size = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name : "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='imageSize']/Value".format(extension_name)
                        }
                    ]
                }
            }
        })

    link_description = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name : "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='linkDescription']/Value".format(extension_name)
                        }
                    ]
                }
            }
        })

    link_name = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name : "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='linkName']/Value".format(extension_name)
                        }
                    ]
                }
            }
        })

    message = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name : "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='message']/Value".format(extension_name)
                        }
                    ]
                }
            }
        })

    min_refresh_period = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name : "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='minRefreshPeriod']/Value".format(extension_name)
                        }
                    ]
                }
            }
        })

    use_default_snippets = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name : "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='useDefaultSnippets']/Value".format(extension_name)
                        }
                    ]
                }
            }
        })

    use_network_link_control_tag = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name : "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='useNetworkLinkControlTag']/Value".format(extension_name)
                        }
                    ]
                }
            }
        })


