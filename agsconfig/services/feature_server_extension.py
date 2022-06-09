"""This module contains the feature Server extension class"""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

from .._enum import StrEnum as Enum
from ..editing.edit_prop import EditorProperty
from .extension_base import ExtensionBase


class FeatureServerExtension(ExtensionBase):
    """Feature Server extension properties for ArcGIS services."""
    class Capability(Enum):
        create = "Create"
        delete = "Delete"
        extract = "Extract"
        query = "Query"
        sync = "Sync"
        update = "Update"
        uploads = "Uploads"
        editing = "Editing"

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
                        { #yapf:disable
                            "document": "main",
                            "path":
                                lambda extension_name:
                                    "$.extensions[?(@.typeName = '{}')].properties.allowGeometryUpdates".format(extension_name)
                        } #yapf:enable
                    ]
                },
                "sddraft": {
                    "conversions": [{
                        "id": "boolToString"
                    }],
                    "paths": [
                        { #yapf:disable
                            "path":
                                lambda extension_name:
                                    "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='allowGeometryUpdates']/Value".format(extension_name)
                        } #yapf:enable
                    ]
                }
            }
        }
    )

    allow_others_to_delete = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "conversions": [{
                        "id": "boolToString"
                    }],
                    "paths": [
                        {
                            "document": "main",
                            "path": "$.extensions[?(@.typeName = 'FeatureServer')].properties.allowOthersToDelete"
                        }
                    ]
                },
                "sddraft": {
                    "conversions": [{
                        "id": "boolToString"
                    }],
                    "paths": [
                        {
                            "path": lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='allowOthersToDelete']/Value"
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
                "agsJson": {
                    "conversions": [{
                        "id": "boolToString"
                    }],
                    "paths": [
                        {
                            "document": "main",
                            "path": "$.extensions[?(@.typeName = 'FeatureServer')].properties.allowOthersToQuery"
                        }
                    ]
                },
                "sddraft": {
                    "conversions": [{
                        "id": "boolToString"
                    }],
                    "paths": [
                        {
                            "path": lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='allowOthersToQuery']/Value"
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
                "agsJson": {
                    "conversions": [{
                        "id": "boolToString"
                    }],
                    "paths": [
                        {
                            "document": "main",
                            "path": "$.extensions[?(@.typeName = 'FeatureServer')].properties.allowOthersToUpdate"
                        }
                    ]
                },
                "sddraft": {
                    "conversions": [{
                        "id": "boolToString"
                    }],
                    "paths": [
                        {
                            "path": lambda extension_name:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='allowOthersToUpdate']/Value"
                            .format(extension_name)
                        }
                    ]
                }
            }
        }
    )

    set_defaults_to_null_for_not_null_fields_in_templates = EditorProperty(
        {
            "constraints": {
                "default": False
            },
            "formats": {
                "agsJson": {
                    "conversions": [{
                        "id": "boolToString",
                        "allowNone": False,
                        "noneAsFalse": True
                    }],
                    "paths": [
                        {
                            "document": "main",
                            "path": lambda extension_name:
                            "$.extensions[?(@.typeName = '{}')].properties.setDefaultsToNullForNotNullFieldsInTemplates"
                            .format(extension_name),
                            "parent": {
                                "children": [{
                                    "key": "setDefaultsToNullForNotNullFieldsInTemplates"
                                }]
                            }
                        }
                    ]
                }
            }
        }
    )

    allow_geometry_updates_without_m_values = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "conversions": [{
                        "id": "boolToString"
                    }],
                    "paths": [
                        {
                            "document": "main",
                            "path": "$.extensions[?(@.typeName = 'FeatureServer')].properties.allowUpdateWithoutMValues"
                        }
                    ]
                },
                "sddraft": {
                    "conversions": [{
                        "id": "boolToString"
                    }],
                    "paths": [
                        {#yapf: disable
                            "path": lambda extension_name:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='allowUpdateWithoutMValues']/Value".format(extension_name),
                            "parent": {
                                "children": [
                                    {
                                        "tag": "Value",
                                        "attributes": {
                                            "{http://www.w3.org/2001/XMLSchema-instance}type": "xs:string"
                                        },
                                    }
                                ],
                                "parent": {
                                    "children": [
                                        {
                                            "tag": "PropertySetProperty",
                                            "attributes": {
                                                "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:PropertySetProperty"
                                            },
                                            "children": [
                                                {
                                                    "tag": "Key",
                                                    "value": "allowUpdateWithoutMValues"
                                                }
                                            ]
                                        }
                                    ],
                                    "parent":{
                                        "children": [
                                            {
                                                "tag": "PropertyArray",
                                                "attributes": {
                                                    "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:ArrayOfPropertySetProperty"
                                                }
                                            }
                                        ],
                                        "parent": {
                                            "children": [
                                                {
                                                    "tag": "Props",
                                                    "attributes": {
                                                        "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:PropertySet"
                                                    }
                                                }
                                            ],
                                            "parent": {
                                                "children": [
                                                    {
                                                        "tag": "SVCExtension",
                                                        "attributes": {
                                                            "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:SVCExtension"
                                                        },
                                                        "children": [
                                                            {
                                                                "tag": "TypeName",
                                                                "value": lambda extension_name: "{}".format(extension_name)
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        }
                                    }
                                }
                            }
                        }#yapf: enable
                    ]
                }
            }
        }
    )

    allow_true_curves_updates = EditorProperty(
        {#yapf:disable
            "formats": {
                "agsJson": {
                    "conversions": [{
                        "id": "boolToString"
                    }],
                    "paths": [
                        {
                            "document": "main",
                            "path":
                                lambda extension_name:
                                    "$.extensions[?(@.typeName = '{}')].properties.allowTrueCurvesUpdates".format(extension_name)
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
                                lambda extension_name:
                                    "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='allowTrueCurvesUpdates']/Value".format(extension_name)
                        }
                    ]
                }
            }
        }#yapf:enable
    )

    enable_ownership_based_access_control = EditorProperty(
        {#yapf:disable
            "formats": {
                "agsJson": {
                    "conversions": [{
                        "id": "boolToString"
                    }],
                    "paths": [
                        {
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties.enableOwnershipBasedAccessControl".format(extension_name)
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
                                lambda extension_name:
                                    "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='enableOwnershipBasedAccessControl']/Value".format(extension_name)
                        }
                    ]
                }
            }
        }#yapf:enable
    )

    enable_z_defaults = EditorProperty(
        {#yapf:disable
            "formats": {
                "agsJson": {
                    "conversions": [{
                        "id": "boolToString"
                    }],
                    "paths": [
                        {
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties.enableZDefaults".format(extension_name)
                        }
                    ]
                },
                "sddraft": {
                    "conversions": [{
                        "id": "boolToString"
                    }],
                    "paths": [
                        {
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='enableZDefaults']/Value".format(extension_name)
                        }
                    ]
                }
            }
        }#yapf:enable
    )

    only_allow_true_curve_updates_by_true_curve_clients = EditorProperty(
        {#yapf:disable
            "formats": {
                "agsJson": {
                    "conversions": [{
                        "id": "boolToString"
                    }],
                    "paths": [
                        {
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties.onlyAllowTrueCurveUpdatesByTrueCurveClients".format(extension_name)
                        }
                    ]
                },
                "sddraft": {
                    "conversions": [{
                        "id": "boolToString"
                    }],
                    "paths": [
                        {
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='onlyAllowTrueCurveUpdatesByTrueCurveClients']/Value".format(extension_name)
                        }
                    ]
                }
            }
        }#yapf:enable
    )

    realm = EditorProperty(
        {#yapf:disable
            "formats": {
                "agsJson": {
                    "conversions": [
                        {"id": "noneToEmptyString"}
                    ],
                    "paths": [
                        {
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties.realm".format(extension_name)
                        }
                    ]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='realm']/Value".format(extension_name)
                        }
                    ]
                }
            }
        }#yapf:enable
    )

    z_default_value = EditorProperty(
        {#yapf:disable
            "formats": {
                "agsJson": {
                    "conversions": [
                        {"id": "numberToString"}
                    ],
                    "paths": [
                        {
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties.zDefaultValue".format(extension_name)
                        }
                    ]
                },
                "sddraft": {
                    "conversions": [{
                        "id": "numberToString"
                    }],
                    "paths": [
                        {
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='zDefaultValue']/Value".format(extension_name)
                        }
                    ]
                }
            }
        }#yapf:enable
    )
