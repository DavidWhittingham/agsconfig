# coding=utf-8
"""This module contains the HostedFeatureServer class
for editing HostedFeatureServer configuration pre or post publish"""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position,no-name-in-module,import-error
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position,no-name-in-module,import-error

from enum import Enum

from .cacheable_core_mixin import CacheableCoreMixin
from .cacheable_ext_mixin import CacheableExtMixin
from .max_record_count_mixin import MaxRecordCountMixin
from .service_base import ServiceBase
from ..editing.edit_prop import EditorProperty


class HostedFeatureServer(MaxRecordCountMixin, CacheableExtMixin, CacheableCoreMixin, ServiceBase):
    """ Class for editing hosted feature services."""
    class Capability(Enum):
        create = "Create"
        delete = "Delete"
        editing = "Editing"
        extract = "Extract"
        query = "Query"
        sync = "Sync"
        update = "Update"
        uploads = "Uploads"

    def __init__(self, editor):
        super().__init__(editor)

    allow_geometry_updates = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.allowGeometryUpdates"  # TODO: Verify
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path": "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='allowGeometryUpdates']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    allow_true_curves_updates = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.allowTrueCurvesUpdates"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path": "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='allowTrueCurvesUpdates']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    allow_update_without_m_values = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {
                            "document": "main",
                            "path": "$.properties.allowUpdateWithoutMValues",
                            "conversions": [{
                                "id": "boolToString"
                            }]
                        }, {
                            "document": "main",
                            "path": "$.jsonProperties.allowUpdateWithoutMValues"
                        }
                    ]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path": "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='allowUpdateWithoutMValues']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    capabilities = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {
                            "document": "main",
                            "path": "$.capabilities"
                        }, {
                            "document": "main",
                            "path": "$.jsonProperties.capabilities"
                        }
                    ],
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
                            "path": "./Configurations/SVCConfiguration/Definition/Info/PropertyArray/PropertySetProperty[Key='webCapabilities']/Value"
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

    creator_present = EditorProperty(
        {
            "formats": {
                # Not found in json file
                "sddraft": {
                    "paths": [
                        {
                            "path": "./StagingSettings/PropertyArray/PropertySetProperty[Key='creatorPresent']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    data_in_gdb = EditorProperty(
        {
            "formats": {
                # Not found in json file
                "sddraft": {
                    "paths": [{
                        "path": "./StagingSettings/PropertyArray/PropertySetProperty[Key='dataInGdb']/Value"
                    }],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    dataset_inspected = EditorProperty(
        {
            "formats": {
                # Apparently no json implementation
                "sddraft": {
                    "paths": [
                        {
                            "path": "./StagingSettings/PropertyArray/PropertySetProperty[Key='datasetInspected']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    enable_z_defaults = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {
                            "document": "main",
                            "path": "$.properties.enableZDefaults",
                            "conversions": [{
                                "id": "boolToString"
                            }]
                        }, {
                            "document": "main",
                            "path": "$.jsonProperties.enableZDefaults"
                        }
                    ]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path": "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='EnableZDefaults']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    only_allow_true_curve_updates_by_true_curve_clients = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.onlyAllowTrueCurveUpdatesByTrueCurveClients"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path": "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='onlyAllowTrueCurveUpdatesByTrueCurveClients']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    sync_enabled = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.jsonProperties.syncEnabled"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path": "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='syncEnabled']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    z_default_value = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.zDefaultValue"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path": "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='zDefaultValue']/Value"
                        }
                    ]
                }
            }
        }
    )
