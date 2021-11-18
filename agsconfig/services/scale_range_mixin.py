# coding=utf-8
"""This module contains a mixin class for scale range properties."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

from ..editing.edit_prop import EditorProperty as _EditorProperty


def _max_scale_constraint(self, value):
    if value == 0 or self.min_scale == 0:
        # min or max scale constraint disabled, don't check min scale
        return value

    if value > self.min_scale:
        # max scale cannot be smaller than the min scale
        self.min_scale = value

    return value


def _min_scale_constraint(self, value):
    if value < self.max_scale:
        # min scale cannot be larger than the max scale
        self.max_scale = value

    return value


class ScaleRangeMixin(object):
    """A mixin for server config models that support a min/max scale range."""

    max_scale = _EditorProperty(
        {
            "constraints": {
                "default": 0,
                "float": True,
                "func": _max_scale_constraint
            },
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.maxScale"
                    }],
                    "conversions": [{
                        "id": "numberToString"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path": "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key = 'maxScale']/Value"
                        }
                    ]
                }
            }
        }
    )

    min_scale = _EditorProperty(
        {
            "constraints": {
                "default": 0,
                "float": True,
                "func": _min_scale_constraint
            },
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.minScale"
                    }],
                    "conversions": [{
                        "id": "numberToString"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path": "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key = 'minScale']/Value"
                        }
                    ]
                }
            }
        }
    )