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

import datetime as _datetime
import logging as _logging

from abc import ABCMeta as _ABCMeta

from ..model_base import ModelBase as _ModelBase
from ..editing.edit_prop import EditorProperty as _EditorProperty
from .._enum import StrEnum as _Enum

MIDNIGHT = _datetime.time(0, 0)


def max_instances_constraint(self, value):
    if value < self.min_instances:
        # Max instances can't be smaller than min instances, so bring min instances down to the same size if smaller
        self.min_instances = value

    return value


def min_instances_constraint(self, value):
    if value == 0 or self.max_instances == 0:
        # min or max instances constraint disabled, don't check min scale
        return value

    if value > self.max_instances:
        # Min instances can't be bigger than max instances, so make the same size
        self.max_instances = value

    return value


class ServiceBase(_ModelBase):
    """Contains base settings/configuration that are common across ArcGIS Service types."""

    __metaclass__ = _ABCMeta

    _custom_extensions = []
    _editor = None
    _logger = _logging.getLogger(__name__)

    class Capability(_Enum):
        """Must be overridden by sub-classes if any capabilities are supported."""
        pass

    @classmethod
    def add_custom_extension(cls, name, extension_class):
        """Add a custom extension class to this service type.

        Args:
            name (str): _description_
            extension_class (_type_): _description_
        """
        cls._custom_extensions.append((name, extension_class))

    def __init__(self, editor):
        """Initilises the class.

        Args:
            editor: An editor object that will receive metadata about each property
        """

        self._editor = editor

        for (name, extension_class) in self._custom_extensions:
            # close over extension class
            def make_prop():
                return property(lambda self: extension_class(editor))

            setattr(type(self), name, make_prop())

    def export(self):
        """Exports the configuration into an in-memory object."""
        return self._editor.export()

    def save(self):
        """Overwrite this file."""
        self._editor.save()

    def save_a_copy(self, *paths):
        """Save this service to one or more new files (one file per input to the service type)."""
        self._editor.save_a_copy(*paths)

    access_information = _EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "conversions": [{
                        "id": "htmlToText"
                    }],
                    "paths": [
                        {
                            "document": "itemInfo",
                            "path": "$.licenseInfo",
                            "parent": {
                                "children": [{
                                    "key": "licenseInfo"
                                }]
                            }
                        }
                    ]
                },
                "sddraft": {
                    "conversions": [{
                        "id": "htmlToText"
                    }],
                    "paths": [
                        {
                            "path": "./ItemInfo/AccessInformation",
                            "parent": {
                                "children": [{
                                    "tag": "AccessInformation"
                                }]
                            }
                        }
                    ]
                }
            }
        }
    )

    cluster = _EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {
                            "document": "main",
                            "path": "$.clusterName",
                            "parent": {
                                "children": [{
                                    "key": "clusterName"
                                }]
                            }
                        }
                    ]
                },
                "sddraft": {
                    "paths": [{
                        "path": "./Configurations/SVCConfiguration/Definition/Cluster"
                    }]
                }
            }
        }
    )

    credits = _EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {
                            "document": "itemInfo",
                            "path": "$.accessInformation",
                            "parent": {
                                "children": [{
                                    "key": "accessInformation"
                                }]
                            }
                        }
                    ]
                },
                "sddraft": {
                    "paths": [{
                        "path": "./ItemInfo/Credits"
                    }]
                }
            }
        }
    )

    description = _EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {
                            "document": "main",
                            "path": "$.description",
                            "parent": {
                                "children": [{
                                    "key": "description"
                                }]
                            }
                        }, {
                            "document": "main",
                            "path": "$.serviceDescription",
                            "parent": {
                                "children": [{
                                    "key": "serviceDescription"
                                }]
                            }
                        }, {
                            "document": "itemInfo",
                            "path": "$.description",
                            "parent": {
                                "children": [{
                                    "key": "description"
                                }]
                            },
                            "conversions": [{
                                "id": "htmlToText"
                            }]
                        }
                    ]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path": "./Configurations/SVCConfiguration/Definition/Description"
                        }, {
                            "path": "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key = 'description']/Value",
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
                                            "children": [{
                                                "tag": "Key",
                                                "value": "description"
                                            }]
                                        }
                                    ]
                                }
                            }
                        }, {
                            "path": "./ItemInfo/Description",
                            "conversions": [{
                                "id": "htmlToText"
                            }]
                        }
                    ]
                }
            }
        }
    )

    folder = _EditorProperty(
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

    high_isolation = _EditorProperty(
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
                            "path": "./Configurations/SVCConfiguration/Definition/Props/PropertyArray/PropertySetProperty[Key = 'Isolation']/Value"
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

    idle_timeout = _EditorProperty(
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
                            "path": "./Configurations/SVCConfiguration/Definition/Props/PropertyArray/PropertySetProperty[Key = 'IdleTimeout']/Value"
                        }
                    ]
                }
            }
        }
    )

    instances_per_container = _EditorProperty(
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
                            "path": "./Configurations/SVCConfiguration/Definition/Props/PropertyArray/PropertySetProperty[Key = 'InstancesPerContainer']/Value"
                        }
                    ]
                }
            }
        }
    )

    max_instances = _EditorProperty(
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
                            "path": "./Configurations/SVCConfiguration/Definition/Props/PropertyArray/PropertySetProperty[Key = 'MaxInstances']/Value"
                        }
                    ]
                }
            }
        }
    )

    metadata_xml = _EditorProperty({"formats": {"sddraft": {"paths": [{"path": "./Metadata/XmlDoc"}]}}})

    min_instances = _EditorProperty(
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
                            "path": "./Configurations/SVCConfiguration/Definition/Props/PropertyArray/PropertySetProperty[Key = 'MinInstances']/Value"
                        }
                    ]
                }
            }
        }
    )

    name = _EditorProperty(
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
                    "paths": [
                        {
                            "path": "./Name"
                        }, {
                            "path": "./Configurations/SVCConfiguration/Name"
                        }, {
                            "path": "./ItemInfo/Name"
                        }
                    ]
                }
            }
        }
    )

    recycle_interval = _EditorProperty(
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
                            "path": "./Configurations/SVCConfiguration/Definition/Props/PropertyArray/PropertySetProperty[Key = 'recycleInterval']/Value"
                        }
                    ]
                }
            }
        }
    )

    recycle_start_time = _EditorProperty(
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
                            "path": "./Configurations/SVCConfiguration/Definition/Props/PropertyArray/PropertySetProperty[Key = 'recycleStartTime']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "timeToString"
                    }]
                }
            }
        }
    )

    replace_existing = _EditorProperty(
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

    summary = _EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {
                            "document": "itemInfo",
                            "path": "$.snippet",
                            "parent": {
                                "children": [{
                                    "key": "snippet"
                                }]
                            }
                        }, {
                            "document": "itemInfo",
                            "path": "$.summary",
                            "parent": {
                                "children": [{
                                    "key": "summary"
                                }]
                            }
                        }
                    ]
                },
                "sddraft": {
                    "paths": [{
                        "path": "./ItemInfo/Snippet",
                        "parent": {
                            "children": [{
                                "tag": "Snippet"
                            }]
                        }
                    }]
                }
            }
        }
    )

    tags = _EditorProperty(
        {
            "constraints": {
                "list": True
            },
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "itemInfo",
                        "path": "$.tags",
                        "parent": {
                            "children": [{
                                "key": "tags"
                            }]
                        }
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
                            "parent": {
                                "children": [
                                    {
                                        "tag": "Tags",
                                        "attributes": {
                                            "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:ArrayOfString"
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        }
    )

    title = _EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "itemInfo",
                        "path": "$.title",
                        "parent": {
                            "children": [{
                                "key": "title"
                            }]
                        }
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path": "./ItemInfo/Title"
                        }, {
                            "path": "./StagingSettings/PropertyArray/PropertySetProperty[Key='ServiceTitle']/Value",
                            "optional": True
                        }
                    ]
                }
            }
        }
    )

    usage_timeout = _EditorProperty(
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
                            "path": "./Configurations/SVCConfiguration/Definition/Props/PropertyArray/PropertySetProperty[Key = 'UsageTimeout']/Value"
                        }
                    ]
                }
            }
        }
    )

    wait_timeout = _EditorProperty(
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
                            "path": "./Configurations/SVCConfiguration/Definition/Props/PropertyArray/PropertySetProperty[Key = 'WaitTimeout']/Value"
                        }
                    ]
                }
            }
        }
    )
