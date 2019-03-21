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
from .image_dimensions_mixin import ImageDimensionsMixin
from .max_record_count_mixin import MaxRecordCountMixin
from .output_dir_mixin import OutputDirMixin
from .service_base import ServiceBase
from ..editing.edit_prop import EditorProperty
from ..services.wfs_server_extension import WFSServerExtension
from ..services.wcs_server_extension import WCSServerExtension
from ..services.wms_server_extension import WMSServerExtension
from ..services.feature_server_extension import FeatureServerExtension
from ..services.jpip_server_extension import JPIPServerExtension
from ..services.kml_server_extension import KmlServerExtension

class MapServer(MaxRecordCountMixin, OutputDirMixin, CacheableMixin, ImageDimensionsMixin, ServiceBase):

    wfs_server_extension = None
    wcs_server_extension = None
    wms_server_extension = None
    feature_server_extension = None
    jpip_server_extension = None
    kml_server_extension = None

    class AntiAliasingMode(Enum):
        none = "None"
        fastest = "Fastest"
        fast = "Fast"
        normal = "Normal"
        best = "Best"

    class Capability(Enum):
        map = "Map"
        query = "Query"
        data = "Data"

    class TextAntiAliasingMode(Enum):
        none = "None"
        force = "Force"
        normal = "Normal"

    def __init__(self, editor):
        super().__init__(editor)
        self.wfs_server_extension = WFSServerExtension(editor)
        self.wcs_server_extension = WCSServerExtension(editor)
        self.wms_server_extension = WMSServerExtension(editor)
        self.feature_server_extension = FeatureServerExtension(editor)
        self.jpip_server_extension = JPIPServerExtension(editor)
        self.kml_server_extension = KmlServerExtension(editor)

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
                            "./Configurations/SVCConfiguration/Definition/Info/PropertyArray/PropertySetProperty[Key='WebCapabilities']/Value"
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