# coding=utf-8
"""This module contains the VectorTileServer class for editing Vector Tile service configuration pre or post publish"""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

# Local imports
from .cacheable_core_mixin import CacheableCoreMixin
from .max_record_count_mixin import MaxRecordCountMixin
from .service_base import ServiceBase
from .vector_tile_server_extension import VectorTileServerExtension
from ..editing.edit_prop import EditorProperty
from .._enum import StrEnum as Enum


class VectorTileServer(MaxRecordCountMixin, CacheableCoreMixin, ServiceBase):

    _vector_tile_server_extension = None

    class AntiAliasingMode(Enum):
        none = "None"
        fastest = "Fastest"
        fast = "Fast"
        normal = "Normal"
        best = "Best"

    class Capability(Enum):
        map = "Map"

    class TextAntiAliasingMode(Enum):
        none = "None"
        force = "Force"
        normal = "Normal"

    def __init__(self, editor):
        super().__init__(editor)
        self._vector_tile_server_extension = VectorTileServerExtension(editor)

    @property
    def vector_tile_server(self):
        return self._vector_tile_server_extension

    anti_aliasing_mode = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.antialiasingMode"
                    }],
                    "conversions": [{
                        "id": "enumToString",
                        "enum": "AntiAliasingMode"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path": "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='antialiasingMode']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "enumToString",
                        "enum": "AntiAliasingMode"
                    }]
                }
            }
        }
    )

    keep_existing_data = EditorProperty({"formats": {"sddraft": {"paths": [{"path": "./KeepExistingData"}]}}})

    portal_url = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [{
                        "path": "./StagingSettings/PropertyArray/PropertySetProperty[Key='PortalURL']/Value"
                    }]
                }
            }
        }
    )

    supported_image_return_types = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path": "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='supportedImageReturnTypes']/Value"
                        }
                    ]
                }
            }
        }
    )

    text_anti_aliasing_mode = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {
                            "document": "main",
                            "path": "$.properties.textAntialiasingMode",
                            "parent": {
                                "children": [{
                                    "key": "textAntialiasingMode"
                                }],
                                "parent": {
                                    "children": [{
                                        "key": "properties"
                                    }]
                                }
                            }
                        }
                    ],
                    "conversions": [{
                        "id": "enumToString",
                        "enum": "TextAntiAliasingMode"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path": "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='textAntialiasingMode']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "enumToString",
                        "enum": "TextAntiAliasingMode"
                    }]
                }
            }
        }
    )

    tiling_scheme = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path": "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='tilingScheme']/Value"
                        }
                    ]
                }
            }
        }
    )

    web_enabled = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path": "./Configurations/SVCConfiguration/Definition/Info/PropertyArray/PropertySetProperty[Key='WebEnabled']/Value"
                        }
                    ]
                }
            }
        }
    )
