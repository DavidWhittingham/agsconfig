# coding=utf-8
"""This module contains the ServiceBase abstract base class for implementing ArcGIS Server service configuration models."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

import datetime
import re

from abc import ABCMeta

from enum import Enum

from ..model_base import ModelBase
from ..editing.edit_prop import EditorProperty

MIDNIGHT = datetime.time(0, 0)


def max_instances_constraint(self, value):
    if value < self.min_instances:
        # Max instances can't be smaller than min instances, so bring min instances down to the same size if smaller
        self.min_instances = value

    return value


def min_instances_constraint(self, value):
    if value > self.max_instances:
        # Min instances can't be bigger than max instances, so make the same size
        self.max_instances = value

    return value


class ServiceBase(ModelBase):
    """Contains base settings/configuration that are common across ArcGIS Service types."""

    __metaclass__ = ABCMeta

    _editor = None

    class Capability(Enum):
        """Must be overridden by sub-classes if any capabilities are supported."""
        pass

    def __init__(self, editor):
        """Initilises the class.

        Args:
            editor: An editor object that will receive metadata about each property
        """

        self._editor = editor

    def export(self):
        """Exports the configuration into an in-memory object."""
        return self._editor.export()

    def save(self):
        """Overwrite this file."""
        self._editor.save()

    def save_a_copy(self, *paths):
        """Save this service to one or more new files (one file per input to the service type)."""
        self._editor.save_a_copy(*paths)

    def _set_props_from_dict(self, prop_dict):
        """Method for setting properties from a dictionary where keys match property names.
        Can be overridden by sub-classes.
        """
        for key, value in prop_dict.items():
            if hasattr(self, key):
                try:
                    setattr(self, key, value)
                except AttributeError:
                    getattr(self, key)._set_props_from_dict(value)

    access_information = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "itemInfo",
                        "path": "$.licenseInfo",
                        "parentPath": "$",
                        "key": "licenseInfo"
                    }]
                },
                "sddraft": {
                    "paths": [{
                        "path": "./ItemInfo/AccessInformation"
                    }]
                }
            }
        }
    )

    cluster = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.clusterName",
                        "parentPath": "$",
                        "key": "clusterName"
                    }]
                },
                "sddraft": {
                    "paths": [{
                        "path": "./Configurations/SVCConfiguration/Definition/Cluster"
                    }]
                }
            }
        }
    )

    credits = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "itemInfo",
                        "path": "$.accessInformation",
                        "parentPath": "$",
                        "key": "accessInformation"
                    }]
                },
                "sddraft": {
                    "paths": [{
                        "path": "./ItemInfo/Credits"
                    }]
                }
            }
        }
    )

    description = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths":
                    [{
                        "document": "main",
                        "path": "$.description",
                        "parentPath": "$",
                        "key": "description"
                    }, {
                        "document": "itemInfo",
                        "path": "$.description",
                        "parentPath": "$",
                        "key": "description"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path": "./Configurations/SVCConfiguration/Definition/Description"
                        }, {
                            "path": "./ItemInfo/Description"
                        }
                    ]
                }
            }
        }
    )

    folder = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [{
                        "path": "./Configurations/SVCConfiguration/ServiceFolder"
                    }],
                    "conversions": [{
                        "id": "noneToEmptyString"
                    }]
                }
            }
        }
    )

    high_isolation = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.isolationLevel"
                    }],
                    "conversions": [{
                        "id": "boolToString",
                        "true": "HIGH",
                        "false": "LOW"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Props/PropertyArray/PropertySetProperty[Key = 'Isolation']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString",
                        "true": "HIGH",
                        "false": "LOW"
                    }]
                }
            }
        }
    )

    idle_timeout = EditorProperty(
        {
            "constraints": {
                "min": 0,
                "int": True
            },
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.maxIdleTime"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Props/PropertyArray/PropertySetProperty[Key = 'IdleTimeout']/Value"
                        }
                    ]
                }
            }
        }
    )

    instances_per_container = EditorProperty(
        {
            "constraints": {
                "min": 1,
                "int": True
            },
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.instancesPerContainer"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Props/PropertyArray/PropertySetProperty[Key = 'InstancesPerContainer']/Value"
                        }
                    ]
                }
            }
        }
    )

    max_instances = EditorProperty(
        {
            "constraints": {
                "int": True,
                "min": 1,
                "func": max_instances_constraint
            },
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.maxInstancesPerNode"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Props/PropertyArray/PropertySetProperty[Key = 'MaxInstances']/Value"
                        }
                    ]
                }
            }
        }
    )

    max_scale = EditorProperty(
        {
            "constraints": {
                "min": 1,
                "float": True
            },
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.maxScale"
                    }],
                    "conversions": [{
                        "id": "numberToString"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key = 'maxScale']/Value"
                        }
                    ]
                }
            }
        }
    )

    min_instances = EditorProperty(
        {
            "constraints": {
                "int": True,
                "min": 0,
                "func": min_instances_constraint
            },
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.minInstancesPerNode"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Props/PropertyArray/PropertySetProperty[Key = 'MinInstances']/Value"
                        }
                    ]
                }
            }
        }
    )

    min_scale = EditorProperty(
        {
            "constraints": {
                "float": True
            },
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.minScale"
                    }],
                    "conversions": [{
                        "id": "numberToString"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key = 'minScale']/Value"
                        }
                    ]
                }
            }
        }
    )

    name = EditorProperty(
        {
            "constraints": {
                "notEmpty": True
            },
            "formats": {
                "agsJson": {
                    "constraints": {
                        "readOnly": True
                    },
                    "paths": [{
                        "document": "main",
                        "path": "$.serviceName"
                    }]
                },
                "sddraft": {
                    "paths": [{
                        "path": "./Name"
                    }, {
                        "path": "./Configurations/SVCConfiguration/Name"
                    }]
                }
            }
        }
    )

    recycle_interval = EditorProperty(
        {
            "constraints": {
                "default": 24,
                "min": 1,
                "int": True
            },
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.recycleInterval"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Props/PropertyArray/PropertySetProperty[Key = 'recycleInterval']/Value"
                        }
                    ]
                }
            }
        }
    )

    recycle_start_time = EditorProperty(
        {
            "constraints": {
                "default": MIDNIGHT
            },
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.recycleStartTime"
                    }],
                    "conversions": [{
                        "id": "timeToString"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Props/PropertyArray/PropertySetProperty[Key = 'recycleStartTime']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "timeToString"
                    }]
                }
            }
        }
    )

    replace_existing = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [{
                        "path": "./Type"
                    }],
                    "conversions": [
                        {
                            "id": "boolToString",
                            "true": "esriServiceDefinitionType_Replacement",
                            "false": "esriServiceDefinitionType_New"
                        }
                    ]
                }
            }
        }
    )

    summary = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "itemInfo",
                        "path": "$.snippet",
                        "parentPath": "$",
                        "key": "snippet"
                    }]
                },
                "sddraft": {
                    "paths": [{
                        "path": "./ItemInfo/Snippet"
                    }]
                }
            }
        }
    )

    tags = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "itemInfo",
                        "path": "$.tags",
                        "parentPath": "$",
                        "key": "tags"
                    }]
                },
                "sddraft": {
                    "conversions": [{
                        "id": "listToElements",
                        "tag": "String"
                    }],
                    "paths": [
                        {
                            "path": "./ItemInfo/Tags",
                            "parentPath": "./ItemInfo",
                            "tag": "Tags",
                            "attributes": {
                                "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:ArrayOfString"
                            }
                        }
                    ]
                }
            }
        }
    )

    title = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "itemInfo",
                        "path": "$.title",
                        "parentPath": "$",
                        "key": "title"
                    }]
                },
                "sddraft": {
                    "paths": [{
                        "path": "./ItemInfo/Title"
                    }]
                }
            }
        }
    )

    usage_timeout = EditorProperty(
        {
            "constraints": {
                "min": 0,
                "int": True
            },
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.maxUsageTime"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Props/PropertyArray/PropertySetProperty[Key = 'UsageTimeout']/Value"
                        }
                    ]
                }
            }
        }
    )

    wait_timeout = EditorProperty(
        {
            "constraints": {
                "min": 0,
                "int": True
            },
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.maxWaitTime"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Props/PropertyArray/PropertySetProperty[Key = 'WaitTimeout']/Value"
                        }
                    ]
                }
            }
        }
    )
