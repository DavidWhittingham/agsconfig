""" Class for modifying ArcGIS geoprocessing service settings."""
# Python 2/3 compatibility
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()

from enum import Enum

from .output_dir_mixin import OutputDirMixin
from .service_base import ServiceBase
from .wps_server_extension import WPSServerExtension
from ..editing.edit_prop import EditorProperty

class GeoprocessingServer(OutputDirMixin, ServiceBase):

    _wps_server_extension = None

    class Capability(Enum):
        uploads = "Uploads"

    class ExecutionType(Enum):
        synchronous = "Synchronous"
        asynchronous = "Asynchronous"

    class MessageLevel(Enum):
        none = "None"
        error = "Error"
        warning = "Warning"
        info = "Info"
        debug = "Debug"

    def __init__(self, editor):
        super().__init__(editor)
        self._wps_server_extension = WPSServerExtension(editor)

    @property
    def wps_server(self):
        """Gets the properties for the WPS server extension."""
        return self._wps_server_extension

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

    execution_type = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.executionType"
                    }],
                    "conversions": [{
                        "id": "enumToString",
                        "enum": "ExecutionType"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='executionType']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "enumToString",
                        "enum": "ExecutionType"
                    }]
                }
            }
        }
    )

    result_map_server = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='resultMapServer']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    show_messages = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='showMessages']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "enumToString",
                        "enum": "MessageLevel"
                    }]
                }
            }
        }
    )

    maximum_records = EditorProperty(
        {
            "constraints": {
                "int": True
            },
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='maximumRecords']/Value"
                        }
                    ]
                }
            }
        }
    )
