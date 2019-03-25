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

from .cacheable_core_mixin import CacheableCoreMixin
from .cacheable_ext_mixin import CacheableExtMixin
from .image_dimensions_mixin import ImageDimensionsMixin
from .max_record_count_mixin import MaxRecordCountMixin
from .output_dir_mixin import OutputDirMixin
from .service_base import ServiceBase
from ..editing.edit_prop import EditorProperty
from ..services.wfs_server_extension import WFSServerExtension
from ..services.wcs_server_extension import WCSServerExtension
from ..services.wms_server_extension import WMSServerExtension
from ..services.feature_server_extension import FeatureServerExtension
from ..services.kml_server_extension import KmlServerExtension


class MapServer(
    MaxRecordCountMixin, OutputDirMixin, CacheableExtMixin, CacheableCoreMixin, ImageDimensionsMixin, ServiceBase
):

    _wfs_server_extension = None
    _wcs_server_extension = None
    _wms_server_extension = None
    _feature_server_extension = None
    _kml_server_extension = None

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
        self._feature_server_extension = FeatureServerExtension(editor)
        self._kml_server_extension = KmlServerExtension(editor)
        self._wfs_server_extension = WFSServerExtension(editor)
        self._wcs_server_extension = WCSServerExtension(editor)
        self._wms_server_extension = WMSServerExtension(editor)

    @property
    def feature_server(self):
        """Gets the properties for the Feature Server (Feature Access in Web UI) extension."""
        return self._feature_server_extension

    @property
    def kml_server(self):
        """Gets the properties for the KML Server extension."""
        return self._kml_server_extension

    @property
    def mobile_server(self):
        """Gets the properties for the Mobile (Mobile Data Access in the UI) server extension."""
        return self._mobile_server_extension

    @property
    def na_server(self):
        """Gets the properties for the Network Analysis server extension"""
        return self._na_server_extension

    @property
    def wcs_server(self):
        """Gets the properties for the WCS Server extension."""
        return self._wcs_server_extension

    @property
    def wfs_server(self):
        """Gets the properties for the WFS Server extension."""
        return self._wfs_server_extension

    @property
    def wms_server(self):
        """Gets the properties for the WMS Server extension."""
        return self._wms_server_extension

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
