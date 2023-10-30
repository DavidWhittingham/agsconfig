# coding=utf-8
"""This module contains a mixin class for service types that support SOIs."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

from ..editing.edit_prop import EditorProperty


class InterceptorMixin(object):
    """A mixin for service types that support Server Object Interceptors"""

    interceptor_order_list = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "conversions": [{
                        "id": "stringToCsv"
                    }],
                    "paths": [
                        {
                            "document": "main",
                            "path": "$.frameworkProperties.interceptorOrderList",
                            "parent": {
                                "children": [{
                                    "key": "interceptorOrderList"
                                }]
                            }
                        }
                    ]
                }
            }
        }
    )