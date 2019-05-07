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

from ..editing.edit_prop import EditorProperty


class ImageDimensionsMixin(object):
    """A mixin for server config models that support image dimensions"""

    max_image_height = EditorProperty(
        {
            "constraints": {
                "min": 0,
                "notEmpty": True,
                "int": True
            },
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.maxImageHeight"
                    }],
                    "conversions": [{
                        "id": "numberToString"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key = 'MaxImageHeight']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "numberToString"
                    }]
                }
            }
        }
    )

    max_image_width = EditorProperty(
        {
            "constraints": {
                "min": 0,
                "notEmpty": True,
                "int": True
            },
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.maxImageWidth"
                    }],
                    "conversions": [{
                        "id": "numberToString"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key = 'MaxImageWidth']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "numberToString"
                    }]
                }
            }
        }
    )
