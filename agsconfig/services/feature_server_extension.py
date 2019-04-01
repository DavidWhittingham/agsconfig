"""This module contains the feature Server extension class"""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

from enum import Enum
from ..editing.edit_prop import EditorProperty
from .extension_base import ExtensionBase
from .ogc_metadata_extension_mixin import OGCMetadataExtensionMixin
from .custom_get_capabilities_extension_mixin import CustomGetCapabilitiesExtensionMixin


class FeatureServerExtension(OGCMetadataExtensionMixin, CustomGetCapabilitiesExtensionMixin, ExtensionBase):
    """ WCS server extension properties for arcGIS services """

    class Capability(Enum):
        create = "Create"
        delete = "Delete"
        extract = "Extract"
        query = "Query"
        sync = "Sync"
        update = "Update"

    def __init__(self, editor):
        super().__init__(editor, "FeatureServer")

    allow_geometry_updates = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "conversions": [{
                        "id": "boolToString"
                    }],
                    "paths": [
                        {
                            "document": "main",
                            "path": "$.extensions[?(@.typeName = 'FeatureServer')].properties.allowGeometryUpdates"
                        }
                    ]
                },
                "sddraft": {
                    "conversions": [{
                        "id": "boolToString"
                    }],
                    "paths": [
                        {
                            "path":
                            lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='allowGeometryUpdates']/Value".format(extension_name)
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
                            lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='allowOthersToDelete']/Value".format(extension_name)
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
                            lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='allowOthersToQuery']/Value".format(extension_name)
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
                            lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='allowOthersToUpdate']/Value".format(extension_name)
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
                            lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='allowTrueCurvesUpdates']/Value".format(extension_name)
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
                            lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='enableOwnershipBasedAccessControl']/Value".format(extension_name)
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
                            lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='enableZDefaults']/Value".format(extension_name)
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
                            lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='maxRecordCount']/Value".format(extension_name)
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
                            lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='realm']/Value".format(extension_name)
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
                            lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='zDefaultValue']/Value".format(extension_name)
                        }
                    ]
                }
            }
        })
