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


class MaxRecordCountMixin(object):

    _SDDRAFT_KEY_MAX_RECORD_COUNT = "maxRecordCount"

    max_record_count = EditorProperty(
        {
            "constraints": {
                "min": 0,
                "int": True
            },
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
                            "path": lambda _SDDRAFT_KEY_MAX_RECORD_COUNT:
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key = '{}']/Value"
                            .format(_SDDRAFT_KEY_MAX_RECORD_COUNT)
                        }
                    ]
                }
            }
        }
    )
