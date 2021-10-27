# coding=utf-8
"""This module contains core mixins for services that are cacheable."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

from ..editing.edit_prop import EditorProperty


class CacheableCoreMixin(object):

    _SDDRAFT_IS_CACHED_PATHS = [
        {#yapf: disable
            "path": "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key = 'isCached']/Value"
        }#yapf: enable
    ]

    cache_dir = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.cacheDir"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path": "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key = 'cacheDir']/Value"
                        }
                    ]
                }
            }
        }
    )

    client_caching_allowed = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.clientCachingAllowed"
                    }],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path": "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key = 'clientCachingAllowed']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    ignore_cache = EditorProperty(
        {
            "constraints": {
                "default": False
            },
            "formats": {
                "agsJson": {
                    "paths": [
                        {
                            "document": "main",
                            "path": "$.properties.ignoreCache",
                            "parent": {
                                "children": [{
                                    "key": "ignoreCache"
                                }]
                            }
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString",
                        "allowNone": False,
                        "noneAsFalse": True
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path": "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key = 'ignoreCache']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString",
                        "allowNone": False,
                        "noneAsFalse": True
                    }]
                }
            }
        }
    )

    is_cached = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.isCached"
                    }],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                },
                "sddraft": {
                    "paths": lambda _SDDRAFT_IS_CACHED_PATHS: _SDDRAFT_IS_CACHED_PATHS,
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

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
                            "path": "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key = 'cacheOnDemand']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    keep_cache = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [{
                        "path": "./KeepExistingMapCache"
                    }],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    virtual_cache_dir = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.virtualCacheDir"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path": "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key = 'virtualCacheDir']/Value",
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
                                                "value": "virtualCacheDir"
                                            }]
                                        }
                                    ]
                                }
                            }
                        }
                    ]
                }
            }
        }
    )
