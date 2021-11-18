# coding=utf-8
"""This module contains the VectorTileServer extension class"""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

# Local imports
from .extension_base import ExtensionBase
from ..editing.edit_prop import EditorProperty
from .._enum import StrEnum as Enum


class VectorTileServerExtension(ExtensionBase):

    _web_capabilities_key = "webCapabilities"

    class Capability(Enum):
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
                            "path": lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Info/PropertyArray/PropertySetProperty[Key='webEnabled']/Value"
                            .format(extension_name)
                        }
                    ]
                }
            }
        }
    )

    enable_z_defaults = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path": lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='enableZDefaults']/Value"
                            .format(extension_name)
                        }
                    ]
                }
            }
        }
    )

    z_default_value = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path": lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='zDefaultValue']/Value"
                            .format(extension_name)
                        }
                    ]
                }
            }
        }
    )

    enable_ownership_based_access_control = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path": lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='enableOwnershipBasedAccessControl']/Value"
                            .format(extension_name)
                        }
                    ]
                }
            }
        }
    )

    allow_others_to_query = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path": lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='allowOthersToQuery']/Value"
                            .format(extension_name)
                        }
                    ]
                }
            }
        }
    )

    allow_others_to_update = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path": lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='allowOthersToUpdate']/Value"
                            .format(extension_name)
                        }
                    ]
                }
            }
        }
    )

    allow_others_to_delete = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path": lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='allowOthersToDelete']/Value"
                            .format(extension_name)
                        }
                    ]
                }
            }
        }
    )

    realm = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path": lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='realm']/Value"
                            .format(extension_name)
                        }
                    ]
                }
            }
        }
    )

    allow_true_curves_updates = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path": lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='allowTrueCurvesUpdates']/Value"
                            .format(extension_name)
                        }
                    ]
                }
            }
        }
    )

    only_allow_true_curve_updates_by_true_curve_clients = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path": lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='onlyAllowTrueCurveUpdatesByTrueCurveClients']/Value"
                            .format(extension_name)
                        }
                    ]
                }
            }
        }
    )

    xss_prevention_enabled = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path": lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='xssPreventionEnabled']/Value"
                            .format(extension_name)
                        }
                    ]
                }
            }
        }
    )

    sync_version_creation_rule = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path": lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='syncVersionCreationRule']/Value"
                            .format(extension_name)
                        }
                    ]
                }
            }
        }
    )

    editor_tracking_respects_daylight_saving_time = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path": lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='editorTrackingRespectsDayLightSavingTime']/Value"
                            .format(extension_name)
                        }
                    ]
                }
            }
        }
    )

    allow_geometry_updates = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path": lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='allowGeometryUpdates']/Value"
                            .format(extension_name)
                        }
                    ]
                }
            }
        }
    )

    editor_tracking_time_zone_id = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path": lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='editorTrackingTimeZoneID']/Value"
                            .format(extension_name)
                        }
                    ]
                }
            }
        }
    )

    max_record_count = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path": lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='maxRecordCount']/Value"
                            .format(extension_name)
                        }
                    ]
                }
            }
        }
    )

    online_resource = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path": lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='onlineResource']/Value"
                            .format(extension_name)
                        }
                    ]
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
                            "path": lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='editorTrackingTimeInUTC']/Value"
                            .format(extension_name)
                        }
                    ]
                }
            }
        }
    )
