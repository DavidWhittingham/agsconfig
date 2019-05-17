# coding=utf-8
"""This module contains the GeodataServer class for editing geodata server configuration pre or post publish"""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

# Third-party imports
from enum import Enum

# Local imports
from .service_base import ServiceBase
from ..editing.edit_prop import EditorProperty


class GeodataServer(ServiceBase):
    class Capability(Enum):
        extraction = "Extraction"
        query = "Query"
        replication = "Replication"
        uploads = "Uploads"

    def __init__(self, editor):
        super().__init__(editor)

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

    name = EditorProperty(
        {
            "constraints": {
                "notEmpty": True
            },
            "formats": {
                "agsJson": {
                    "constraints": {
                        "readOnly": True
                    },
                    "paths": [{
                        "document": "main",
                        "path": "$.serviceName"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path": "./Name"
                        }, {
                            "path": "./Configurations/SVCConfiguration/Name"
                        }, {
                            "path": "./ItemInfo/Name"
                        }
                    ]
                }
            }
        }
    )
