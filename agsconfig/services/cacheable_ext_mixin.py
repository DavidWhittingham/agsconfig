# coding=utf-8
"""This module contains extended mixins for classic cacheable services (i.e. map, image)."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

from ..editing.edit_prop import EditorProperty


class CacheableExtMixin(object):

    cache_on_demand = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.cacheOnDemand"
                    }],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key = 'cacheOnDemand']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    export_tiles_allowed = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.exportTilesAllowed"
                    }],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key = 'exportTilesAllowed']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    max_export_tiles_count = EditorProperty(
        {
            "constraints": {
                "int": True,
                "min": 0
            },
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.maxExportTilesCount"
                    }],
                    "conversions": [{
                        "id": "numberToString"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key = 'maxExportTilesCount']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "numberToString"
                    }]
                }
            }
        }
    )

    use_local_cache_dir = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.useLocalCacheDir"
                    }],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key = 'useLocalCacheDir']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )
