# coding=utf-8
"""This module contains the GeocodeServer class for editing geocode server configuration pre or post publish"""

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

class GeocodeServer(CacheableMixin, ImageDimensionsMixin, ServiceBase):

    class Capability(Enum):
        geocode = "Geocode"
        reverse_geocode = "ReverseGeocode"

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

    name = EditorProperty(
    {
        "formats": {
            "sddraft": {
                "paths": [
                    {
                        "path":
                        "./ItemInfo/Name"
                    }
                ]
            }
        }
    })

    name = EditorProperty(
    {
        "formats": {
            "sddraft": {
                "paths": [
                    {
                        "path":
                        "./ItemInfo/Title"
                    }
                ]
            }
        }
    })