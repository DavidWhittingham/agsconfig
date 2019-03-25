# coding=utf-8
"""This module contains the VectorTileServer extension class"""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

# Third party imports
from enum import Enum

# Local imports
from .extension_base import ExtensionBase
from ..editing.edit_prop import EditorProperty

class VectorTileServerExtension(ExtensionBase):
    class ExtensionCapabilities(Enum):
        query = "Query"
        create = "Create"
        update = "Update"
        delete = "Delete"
        uploads = "Uploads"
        editing = "Editing"

    def __init__(self, editor):
        super().__init__(editor, "VectorTileServer")

    web_enabled = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension/Info/PropertyArray/PropertySetProperty[Key='webEnabled']/Value"
                        }
                    ]
                }
            }
        })

    enable_z_defaults = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension/Props/PropertyArray/PropertySetProperty[Key='enableZDefaults']/Value"
                        }
                    ]
                }
            }
        })
    
    z_default_value = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension/Props/PropertyArray/PropertySetProperty[Key='zDefaultValue']/Value"
                        }
                    ]
                }
            }
        })

    enable_ownership_based_access_control = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension/Props/PropertyArray/PropertySetProperty[Key='enableOwnershipBasedAccessControl']/Value"
                        }
                    ]
                }
            }
        })

    allow_others_to_query = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension/Props/PropertyArray/PropertySetProperty[Key='allowOthersToQuery']/Value"
                        }
                    ]
                }
            }
        })

    allow_others_to_update = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension/Props/PropertyArray/PropertySetProperty[Key='allowOthersToUpdate']/Value"
                        }
                    ]
                }
            }
        })

    allow_others_to_delete = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension/Props/PropertyArray/PropertySetProperty[Key='allowOthersToDelete']/Value"
                        }
                    ]
                }
            }
        })

    realm = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension/Props/PropertyArray/PropertySetProperty[Key='realm']/Value"
                        }
                    ]
                }
            }
        })

    allow_true_curves_updates = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension/Props/PropertyArray/PropertySetProperty[Key='allowTrueCurvesUpdates']/Value"
                        }
                    ]
                }
            }
        })

    only_allow_true_curve_updates_by_true_curve_clients = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension/Props/PropertyArray/PropertySetProperty[Key='onlyAllowTrueCurveUpdatesByTrueCurveClients']/Value"
                        }
                    ]
                }
            }
        })

    xss_prevention_enabled = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension/Props/PropertyArray/PropertySetProperty[Key='xssPreventionEnabled']/Value"
                        }
                    ]
                }
            }
        })

    sync_version_creation_rule = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension/Props/PropertyArray/PropertySetProperty[Key='syncVersionCreationRule']/Value"
                        }
                    ]
                }
            }
        })

    editor_tracking_respects_daylight_saving_time = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension/Props/PropertyArray/PropertySetProperty[Key='editorTrackingRespectsDayLightSavingTime']/Value"
                        }
                    ]
                }
            }
        })

    allow_geometry_updates = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension/Props/PropertyArray/PropertySetProperty[Key='allowGeometryUpdates']/Value"
                        }
                    ]
                }
            }
        })

    editor_tracking_time_zone_id = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension/Props/PropertyArray/PropertySetProperty[Key='editorTrackingTimeZoneID']/Value"
                        }
                    ]
                }
            }
        })

    max_record_count = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension/Props/PropertyArray/PropertySetProperty[Key='maxRecordCount']/Value"
                        }
                    ]
                }
            }
        })

    online_resource = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension/Props/PropertyArray/PropertySetProperty[Key='onlineResource']/Value"
                        }
                    ]
                }
            }
        })

    capabilities = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension/Info/PropertyArray/PropertySetProperty[Key='webCapabilities']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "enumToString",
                        "enum": "ExtensionCapabilities"
                    }, {
                        "id": "stringToCsv"
                    }]
                }
            }
        }
    )

    editor_tracking_time_in_utc = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension/Props/PropertyArray/PropertySetProperty[Key='editorTrackingTimeInUTC']/Value"
                        }
                    ]
                }
            }
        })