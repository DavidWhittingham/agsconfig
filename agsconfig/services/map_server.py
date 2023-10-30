# coding=utf-8
"""This module contains the MapServer class for editing MapServer configuration pre or post publish"""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

from .._enum import StrEnum as Enum
from ..editing.edit_prop import EditorProperty
from ..services.feature_server_extension import FeatureServerExtension
from ..services.kml_server_extension import KmlServerExtension
from ..services.na_server_extension import NAServerExtension
from ..services.parcel_fabric_server_extension import ParcelFabricServerExtension
from ..services.validation_server_extension import ValidationServerExtension
from ..services.version_management_server_extension import VersionManagementServerExtension
from ..services.wcs_server_extension import WCSServerExtension
from ..services.wfs_server_extension import WFSServerExtension
from ..services.wms_server_extension import WMSServerExtension
from .cacheable_core_mixin import CacheableCoreMixin
from .cacheable_ext_mixin import CacheableExtMixin
from .image_dimensions_mixin import ImageDimensionsMixin
from .interceptor_mixin import InterceptorMixin
from .max_record_count_mixin import MaxRecordCountMixin
from .output_dir_mixin import OutputDirMixin
from .scale_range_mixin import ScaleRangeMixin
from .service_base import ServiceBase


class MapServer(
    InterceptorMixin, ScaleRangeMixin, MaxRecordCountMixin, OutputDirMixin, CacheableExtMixin, CacheableCoreMixin,
    ImageDimensionsMixin, ServiceBase
):
    _feature_server_extension = None
    _kml_server_extension = None
    _na_server_extension = None
    _parcel_fabric_server_extension = None
    _validation_server_extension = None
    _version_management_server_extension = None
    _wcs_server_extension = None
    _wfs_server_extension = None
    _wms_server_extension = None

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
        self._na_server_extension = NAServerExtension(editor)
        self._parcel_fabric_server_extension = ParcelFabricServerExtension(editor)
        self._validation_server_extension = ValidationServerExtension(editor)
        self._version_management_server_extension = VersionManagementServerExtension(editor)
        self._wcs_server_extension = WCSServerExtension(editor)
        self._wfs_server_extension = WFSServerExtension(editor)
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
    def na_server(self):
        """Gets the properties for the Network Analysis Server extension."""
        return self._na_server_extension

    @property
    def parcel_fabric_server(self):
        """Gets the properties for the Parcel Fabric Server extension."""
        return self._parcel_fabric_server_extension

    @property
    def validation_server(self):
        """Gets the properties for the Validation Server extension."""
        return self._validation_server_extension

    @property
    def version_management_server(self):
        """Gets the properties for the Version Management Server extension."""
        return self._version_management_server_extension

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

    anti_aliasing_mode = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {
                            "document": "main",
                            "path": "$.properties.antialiasingMode",
                            "parent": {
                                "children": [{
                                    "key": "antialiasingMode"
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
                            "path": "./Configurations/SVCConfiguration/Definition/Info/PropertyArray/PropertySetProperty[Key='WebCapabilities']/Value"
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

    date_fields_respect_daylight_saving_time = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {
                            "document": "main",
                            "path": "$.properties.dateFieldsRespectsDayLightSavingTime",
                            "parent": {
                                "children": [{
                                    "key": "dateFieldsRespectsDayLightSavingTime"
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
                        "id": "boolToString"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path": "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='dateFieldsRespectsDayLightSavingTime']/Value",
                            "parent": {
                                "children": [
                                    {
                                        "tag": "Value",
                                        "attributes": {
                                            "{http://www.w3.org/2001/XMLSchema-instance}type": "xs:string"
                                        }
                                    }
                                ],
                                "parent": {
                                    "children": [
                                        {
                                            "tag": "PropertySetProperty",
                                            "attributes": {
                                                "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:PropertySetProperty"
                                            },
                                            "children": [
                                                {
                                                    "tag": "Key",
                                                    "value": "dateFieldsRespectsDayLightSavingTime"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            }
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    date_fields_timezone_id = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {
                            "document": "main",
                            "path": "$.properties.dateFieldsTimezoneID",
                            "parent": {
                                "children": [{
                                    "key": "dateFieldsTimezoneID"
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
                        "id": "olsonTimeZoneToWindowsTimeZone"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path": "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='dateFieldsTimezoneID']/Value",
                            "parent": {
                                "children": [
                                    {
                                        "tag": "Value",
                                        "attributes": {
                                            "{http://www.w3.org/2001/XMLSchema-instance}type": "xs:string"
                                        }
                                    }
                                ],
                                "parent": {
                                    "children": [
                                        {
                                            "tag": "PropertySetProperty",
                                            "attributes": {
                                                "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:PropertySetProperty"
                                            },
                                            "children": [{
                                                "tag": "Key",
                                                "value": "dateFieldsTimezoneID"
                                            }]
                                        }
                                    ]
                                }
                            }
                        }
                    ],
                    "conversions": [{
                        "id": "olsonTimeZoneToWindowsTimeZone"
                    }]
                }
            }
        }
    )

    disable_identify_relates = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path": "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='disableIdentifyRelates']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    enable_dynamic_layers = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {
                            "document": "main",
                            "path": "$.properties.enableDynamicLayers",
                            "parent": {
                                "children": [{
                                    "key": "enableDynamicLayers"
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
                        "id": "boolToString"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path": "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='enableDynamicLayers']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    file_path = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path": "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='FilePath']/Value"
                        }
                    ]
                }
            }
        }
    )

    schema_locking_enabled = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {
                            "document": "main",
                            "path": "$.properties.schemaLockingEnabled",
                            "parent": {
                                "children": [{
                                    "key": "schemaLockingEnabled"
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
                        "id": "boolToString"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path": "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='schemaLockingEnabled']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }]
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