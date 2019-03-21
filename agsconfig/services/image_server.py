# coding=utf-8
"""This module contains the MapServer class for editing MapServer configuration pre or post publish"""

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
from ..editing.edit_prop import EditorProperty
from .image_dimensions_mixin import ImageDimensionsMixin
from .service_base import ServiceBase
from .wms_server_extension import WMSServerExtension
from .jpip_server_extension import JPIPServerExtension
from .wcs_server_extension import WCSServerExtension

class ImageServer(CacheableMixin, ImageDimensionsMixin, ServiceBase):

    wms_server_extension = None
    wcs_server_extension = None
    jpip_server_extension = None

    class Capability(Enum):
        catalog = "Catalog"
        edit = "Edit"
        mensuration = "Mensuration"
        pixels = "Pixels"
        download = "Download"
        image = "Image"
        metadata = "Metadata"
        uploads = "Uploads"

    class CompressionMethod(Enum):
        none = "None"
        jpeg = "JPEG"
        lz77 = "LZ77"
        lerc = "LERC"

    class MosaicMethod(Enum):
        north_west = "NorthWest"
        center = "Center"
        lock_raster = "LockRaster"
        by_attribute = "ByAttribute"
        nadir = "Nadir"
        viewpoint = "Viewpoint"
        seamline = "Seamline"
        none = "None"

    class ResamplingMethod(Enum):
        nearest_neighbor = 0
        bilinear = 1
        cubic = 2
        majority = 3

    def __init__(self, editor):
        super().__init__(editor)
        self.jpip_server_extension = JPIPServerExtension(editor)
        self.wcs_server_extension = WCSServerExtension(editor)
        self.wms_server_extension = WMSServerExtension(editor)

    allowed_mosaic_methods = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.capabilities"
                    }],
                    "conversions": [{
                        "id": "enumToString",
                        "enum": "MosaicMethod"
                    }, {
                        "id": "stringToCsv"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='AllowedMosaicMethods']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "enumToString",
                        "enum": "MosaicMethod"
                    }, {
                        "id": "stringToCsv"
                    }]
                }
            }
        }
    )

    capabilities = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.capabilities"
                    }],
                    "conversions": [{
                        "id": "enumToString",
                        "enum": "Capability"
                    }, {
                        "id": "stringToCsv"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Info/PropertyArray/PropertySetProperty[Key='webCapabilities']/Value"
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