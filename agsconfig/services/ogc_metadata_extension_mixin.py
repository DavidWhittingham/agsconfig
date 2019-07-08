"""This module contains the WMS Server extension class"""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

from ..editing.edit_prop import EditorProperty


class OGCMetadataExtensionMixin(object):

    _agsjson_key_address = "address"
    _sddraft_key_administrative_area = "administrativeArea"
    _sddraft_key_address = "address"
    _sddraft_key_email = "electronicMailAddress"
    _sddraft_key_keyword = "keyword"

    abstract = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {# yapf: disable
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{0}')].properties.abstract".format(extension_name),
                            "parentPath": lambda extension_name: "$.extensions[?(@.typeName = '{0}')].properties".format(extension_name),
                            "key": "abstract"
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='abstract']/Value".format(extension_name)
                        }# yapf: enable
                    ]
                }
            }
        })

    access_constraints = EditorProperty(
        {
            "formats": {
                 "agsJson": {
                    "paths": [
                        {
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{0}')].properties.accessConstraints".format(extension_name),
                            "parentPath": lambda extension_name: "$.extensions[?(@.typeName = '{0}')].properties".format(extension_name),
                            "key": "accessConstraints"
                        }
                    ]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='accessConstraints']/Value".format(extension_name)
                        }
                    ]
                }
            }
        }
    )

    address = EditorProperty(
        {
            "formats": {
                 "agsJson": {
                    "paths": [
                        {# yapf: disable
                            "document": "main",
                            "path": lambda extension_name, _agsjson_key_address: "$.extensions[?(@.typeName = '{}')].{}".format(extension_name, _agsjson_key_address),
                            "parentPath": lambda extension_name: "$.extensions[?(@.typeName = '{}')]".format(extension_name),
                            "key": "address"
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _sddraft_key_address: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _sddraft_key_address)
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    administrative_area = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name, _sddraft_key_administrative_area: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _sddraft_key_administrative_area)
                        }
                    ]
                }
            }
        }
    )

    city = EditorProperty(
        {
            "formats": {
                 "agsJson": {
                    "paths": [
                        {
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{0}')].properties.city".format(extension_name),
                            "parentPath": lambda extension_name: "$.extensions[?(@.typeName = '{0}')].properties".format(extension_name),
                            "key": "city"
                        }
                    ]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='city']/Value".format(extension_name)
                        }
                    ]
                }
            }
        })

    country = EditorProperty(
        {
            "formats": {
                 "agsJson": {
                    "paths": [
                        {
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{0}')].properties.country".format(extension_name),
                            "parentPath": lambda extension_name: "$.extensions[?(@.typeName = '{0}')].properties".format(extension_name),
                            "key": "country"
                        }
                    ]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='country']/Value".format(extension_name)
                        }
                    ]
                }
            }
        })

    email = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name, _sddraft_key_email:
                            "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value"
                            .format(extension_name, _sddraft_key_email)
                        }
                    ]
                }
            }
        }
    )

    keyword = EditorProperty(
        {
            "formats": {
                 "agsJson": {
                    "paths": [
                        {
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{0}')].properties.keywords".format(extension_name),
                            "parentPath": lambda extension_name: "$.extensions[?(@.typeName = '{0}')].properties".format(extension_name),
                            "key": "keywords"
                        }
                    ]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name, _sddraft_key_keyword: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='{1}']/Value".format(extension_name, _sddraft_key_keyword)
                        }
                    ]
                }
            }
        })

    fees = EditorProperty(
        {
            "formats": {
                 "agsJson": {
                    "paths": [
                        {
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{0}')].properties.fees".format(extension_name),
                            "parentPath": lambda extension_name: "$.extensions[?(@.typeName = '{0}')].properties".format(extension_name),
                            "key": "fees"
                        }
                    ]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='fees']/Value".format(extension_name)
                        }
                    ]
                }
            }
        })

    name = EditorProperty(
        {
            "formats": {
                 "agsJson": {
                    "paths": [
                        {
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{0}')].properties.name".format(extension_name),
                            "parentPath": lambda extension_name: "$.extensions[?(@.typeName = '{0}')].properties".format(extension_name),
                            "key": "name"
                        }
                    ]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='name']/Value".format(extension_name)
                        }
                    ]
                }
            }
        })

    title = EditorProperty(
        {
            "formats": {
                 "agsJson": {
                    "paths": [
                        {
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{0}')].properties.title".format(extension_name),
                            "parentPath": lambda extension_name: "$.extensions[?(@.typeName = '{0}')].properties".format(extension_name),
                            "key": "title"
                        }
                    ]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='title']/Value".format(extension_name)
                        }
                    ]
                }
            }
        }
    )