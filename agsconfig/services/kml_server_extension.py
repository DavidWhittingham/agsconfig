"""This module contains the kml Server extension class"""

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


class KmlServerExtension(ExtensionBase):
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

    compatibility_mode = EditorProperty(
        {#yapf:disable
            "formats": {
                "agsJson": {
                    "conversions": [
                        {
                            "id": "enumToString",
                            "enum": "CompatibilityMode"
                        }
                    ],
                    "paths": [
                        {
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties.compatibilityMode".format(extension_name)
                        }
                    ]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='compatibilityMode']/Value".format(extension_name)
                        }
                    ],
                    "conversions": [
                        {
                            "id": "enumToString",
                            "enum": "CompatibilityMode"
                        }
                    ]
                }
            }
        }#yapf:enable
    )

    dpi = EditorProperty(
        {#yapf:disable
            "constraints": {
                "min": 1,
                "int": True
            },
            "formats": {
                "agsJson": {
                    "conversions": [
                        {
                            "id": "numberToString"
                        }
                    ],
                    "paths": [
                        {
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties.dpi".format(extension_name)
                        }
                    ]
                },
                "sddraft": {
                    "conversions": [
                        {
                            "id": "numberToString"
                        }
                    ],
                    "paths": [
                        {
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='dpi']/Value".format(extension_name)
                        }
                    ]
                }
            }
        }#yapf:enable
    )

    feature_limit = EditorProperty(
        {#yapf:disable
            "constraints": {
                "min": 1,
                "int": True
            },
            "formats": {
                "agsJson": {
                    "conversions": [
                        {
                            "id": "numberToString"
                        }
                    ],
                    "paths": [
                        {
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties.featureLimit".format(extension_name)
                        }
                    ]
                },
                "sddraft": {
                    "conversions": [
                        {
                            "id": "numberToString"
                        }
                    ],
                    "paths": [
                        {
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='featureLimit']/Value".format(extension_name)
                        }
                    ]
                }
            }
        }#yapf:enable
    )

    image_size = EditorProperty(
        {#yapf:disable
            "constraints": {
                "min": 0,
                "int": True
            },
            "formats": {
                "agsJson": {
                    "conversions": [
                        {
                            "id": "numberToString"
                        }
                    ],
                    "paths": [
                        {
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties.imageSize".format(extension_name)
                        }
                    ]
                },
                "sddraft": {
                    "conversions": [
                        {
                            "id": "numberToString"
                        }
                    ],
                    "paths": [
                        {
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='imageSize']/Value".format(extension_name)
                        }
                    ]
                }
            }
        }#yapf:enable
    )

    min_refresh_period = EditorProperty(
        {#yapf:disable
            "constraints": {
                "min": 0,
                "int": True
            },
            "formats": {
                "agsJson": {
                    "conversions": [
                        {
                            "id": "numberToString"
                        }
                    ],
                    "paths": [
                        {
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties.minRefreshPeriod".format(extension_name)
                        }
                    ]
                },
                "sddraft": {
                    "conversions": [
                        {
                            "id": "numberToString"
                        }
                    ],
                    "paths": [
                        {
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='minRefreshPeriod']/Value".format(extension_name)
                        }
                    ]
                }
            }
        }#yapf:enable
    )

    use_default_snippets = EditorProperty(
        {#yapf:disable
            "formats": {
                "agsJson": {
                    "conversions": [
                        {
                            "id": "boolToString"
                        }
                    ],
                    "paths": [
                        {
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties.useDefaultSnippets".format(extension_name)
                        }
                    ]
                },
                "sddraft": {
                    "conversions": [
                        {
                            "id": "boolToString"
                        }
                    ],
                    "paths": [
                        {
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='useDefaultSnippets']/Value".format(extension_name)
                        }
                    ]
                }
            }
        }#yapf:enable
    )