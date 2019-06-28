# coding=utf-8
"""This module contains the HostedFeatureServer class 
for editing HostedFeatureServer configuration pre or post publish"""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

from enum import Enum

from .cacheable_core_mixin import CacheableCoreMixin
from .cacheable_ext_mixin import CacheableExtMixin
from .image_dimensions_mixin import ImageDimensionsMixin
from .max_record_count_mixin import MaxRecordCountMixin
from .service_base import ServiceBase
from ..editing.edit_prop import EditorProperty
from ..services.feature_server_extension import FeatureServerExtension

class HostedFeatureServer(
    MaxRecordCountMixin, CacheableExtMixin, CacheableCoreMixin, ServiceBase):
    _feature_server_extension = None

    # Not to be confused with allowGeometryUpdates from the feature server extension
    allow_geometry_updates = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.allowGeometryUpdates" # TODO: Verify
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='allowGeometryUpdates']/Value"
                        }
                    ],
                     "conversions": [
                         {
                            "id": "boolToString"
                        }
                    ]
                }
            }
        }
    )

    # Not to be confused with allowTrueCurvesUpdates from the feature server extension
    allow_true_curves_updates = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.allowTrueCurvesUpdates" # TODO: Verify
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='allowTrueCurvesUpdates']/Value"
                        }
                    ],
                     "conversions": [
                         {
                            "id": "boolToString"
                        }
                    ]
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
                        "path": "$.properties.onlyAllowTrueCurveUpdateByTrueCurveClients" # TODO: Verify
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='onlyAllowTrueCurveUpdatesByTrueCurveClients']/Value"
                        }
                    ],
                     "conversions": [
                         {
                            "id": "boolToString"
                        }
                    ]
                }
            }
        }
    )

    enable_z_defaults = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.enableZDefaults" # TODO: Verify
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='EnableZDefaults']/Value"
                        }
                    ],
                     "conversions": [
                         {
                            "id": "boolToString"
                        }
                    ]
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
                        "path": "$.properties.zDefaultValue" # TODO: Verify
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='zDefaultValue']/Value"
                        }
                    ],
                     "conversions": [
                         {
                            "id": "boolToString"
                        }
                    ]
                }
            }
        }
    )

    allow_update_without_m_values = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.allowUpdateWithoutMValues" # TODO: Verify
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='allowUpdateWithoutMValues']/Value"
                        }
                    ],
                     "conversions": [
                         {
                            "id": "boolToString"
                        }
                    ]
                }
            }
        }
    )

    dataset_inspected = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.datasetInspected" # TODO: Verify
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='datasetInspected']/Value"
                        }
                    ],
                     "conversions": [
                         {
                            "id": "boolToString"
                        }
                    ]
                }
            }
        }
    )

    creator_present = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.creatorPresent" # TODO: Verify
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='creatorPresent']/Value"
                        }
                    ],
                     "conversions": [
                         {
                            "id": "boolToString"
                        }
                    ]
                }
            }
        }
    )

    data_in_gdb = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.dataInGdb" # TODO: Verify
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='dataInGdb']/Value"
                        }
                    ],
                     "conversions": [
                         {
                            "id": "boolToString"
                        }
                    ]
                }
            }
        }
    )
