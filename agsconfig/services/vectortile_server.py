# coding=utf-8
"""This module contains the VectorTileServer class for editing Vector Tile service configuration pre or post publish"""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

from enum import Enum

from .cacheable_mixin import CacheableMixin
from .image_dimensions_mixin import ImageDimensionsMixin
from .service_base import ServiceBase
from ..editing.edit_prop import EditorProperty
from .vectortile_server_extension import VectorTileServerExtension

class VectorTileServer(ServiceBase, CacheableMixin):

    _vectortile_server_extension = None

    class Capability(Enum):
        map = "Map"

    class AntiAliasingMode(Enum):
        none = "None"
        fastest = "Fastest"
        fast = "Fast"
        normal = "Normal"
        best = "Best"

    @property
    def vectortile_server_extension(self):
        return self._vectortile_server_extension

    def __init__(self, editor):
        super(VectorTileServer, self).__init__(editor)
        self._vectortile_server_extension = VectorTileServerExtension(editor)

    portal_url = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.portalUrl" # TODO: unknown
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./StagingSettings/PropertyArray/PropertySetProperty[Key='PortalURL']/Value"
                        }
                    ]
                }
            }
        }
    )

    type_name = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.type"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/TypeName"
                        }
                    ]
                }
            }
        }
    )

    cluster = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.clusterName"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Cluster"
                        }
                    ]
                }
            }
        }
    )

    keep_existing_data = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.keepExistingData"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./KeepExistingData"
                        }
                    ]
                }
            }
        }
    )

    supported_image_return_types = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.configuration.supportedImageReturnTypes" #TODO: fix
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='supportedImageReturnTypes']/Value"
                        }
                    ]
                }
            }
        }
    )

    is_cached = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.isCached"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='isCached']/Value"
                        }
                    ]
                }
            }
        }
    )

    service_folder = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.serviceFolder" #TODO: unknown
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/ServiceFolder"
                        }
                    ]
                }
            }
        }
    )

    tiling_scheme = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.tilingScheme" #TODO: unknown
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='tilingScheme']/Value"
                        }
                    ]
                }
            }
        }
    )

    ignore_cache = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.ignoreCache" #TODO: unknown
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='ignoreCache']/Value"
                        }
                    ]
                }
            }
        }
    )

    web_enabled = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.webEnabled" #TODO: unknown
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Info/PropertyArray/PropertySetProperty[Key='WebEnabled']/Value"
                        }
                    ]
                }
            }
        }
    )

    max_record_count = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.maxRecordCount"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='maxRecordCount']/Value"
                        }
                    ]
                }
            }
        }
    )

    antialiasing_mode = EditorProperty(
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
                    }, {
                        "id": "stringToCsv"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='antialiasingMode']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "enumToString",
                        "enum": "AntiAliasingMode"
                    }, {
                        "id": "stringToCsv"
                    }]
                }
            }
        }
    )

    text_antialiasing_mode = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.textAntialiasingMode"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='textAntialiasingMode']/Value"
                        }
                    ]
                }
            }
        }
    )

    keep_existing_data = EditorProperty(
    {
        "formats": {
            "agsJson": {
                "paths": [{
                    "document": "main",
                    "path": "$.keepExistingData" #TODO: unknown
                    }]
                },
            "sddraft": {
                "paths": [
                        {
                            "path":
                            "./KeepExistingData"
                        }
                    ]
                }
            }
        }
    )

