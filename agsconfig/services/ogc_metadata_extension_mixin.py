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

    # ArcGIS Server JSON key names
    _AGSJSON_KEY_ABSTRACT = "abstract"
    _AGSJSON_KEY_ACCESS_CONSTRAINTS = "accessConstraints"
    _AGSJSON_KEY_ADDRESS = "address"
    _AGSJSON_KEY_ADMINISTRATIVE_AREA = "administrativeArea"
    _AGSJSON_KEY_CITY = "city"
    _AGSJSON_KEY_COUNTRY = "country"
    _AGSJSON_KEY_EMAIL = "electronicMailAddress"
    _AGSJSON_KEY_FACSIMILE = "facsimile"
    _AGSJSON_KEY_FEES = "fees"
    _AGSJSON_KEY_INDIVIDUAL_NAME = "individualName"
    _AGSJSON_KEY_KEYWORDS = "keyword"
    _AGSJSON_KEY_NAME = "name"
    _AGSJSON_KEY_PHONE = "phone"
    _AGSJSON_KEY_POSITION_NAME = "positionName"
    _AGSJSON_KEY_POSTAL_CODE = "postalCode"
    _AGSJSON_KEY_PROVIDER_NAME = "providerName"
    _AGSJSON_KEY_TITLE = "title"

    # Service Definition Draft key names
    _SDDRAFT_KEY_ABSTRACT = "abstract"
    _SDDRAFT_KEY_ACCESS_CONSTRAINTS = "accessConstraints"
    _SDDRAFT_KEY_ADMINISTRATIVE_AREA = "administrativeArea"
    _SDDRAFT_KEY_ADDRESS = "address"
    _SDDRAFT_KEY_CITY = "city"
    _SDDRAFT_KEY_COUNTRY = "country"
    _SDDRAFT_KEY_EMAIL = "electronicMailAddress"
    _SDDRAFT_KEY_FACSIMILE = "facsimile"
    _SDDRAFT_KEY_FEES = "fees"
    _SDDRAFT_KEY_INDIVIDUAL_NAME = "individualName"
    _SDDRAFT_KEY_KEYWORDS = "keyword"
    _SDDRAFT_KEY_NAME = "name"
    _SDDRAFT_KEY_PHONE = "phone"
    _SDDRAFT_KEY_POSITION_NAME = "positionName"
    _SDDRAFT_KEY_POSTAL_CODE = "postalCode"
    _SDDRAFT_KEY_PROVIDER_NAME = "providerName"
    _SDDRAFT_KEY_TITLE = "title"
    

    abstract = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {# yapf: disable
                            "document": "main",
                            "path": lambda extension_name, _AGSJSON_KEY_ABSTRACT: "$.extensions[?(@.typeName = '{}')].properties.{}".format(extension_name, _AGSJSON_KEY_ABSTRACT),
                            "parentPath": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties".format(extension_name),
                            "key": lambda _AGSJSON_KEY_ABSTRACT: _AGSJSON_KEY_ABSTRACT
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_ABSTRACT:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_ABSTRACT)
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    access_constraints = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {# yapf: disable
                            "document": "main",
                            "path": lambda extension_name, _AGSJSON_KEY_ACCESS_CONSTRAINTS: "$.extensions[?(@.typeName = '{}')].properties.{}".format(extension_name, _AGSJSON_KEY_ACCESS_CONSTRAINTS),
                            "parentPath": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties".format(extension_name),
                            "key": lambda _AGSJSON_KEY_ACCESS_CONSTRAINTS: _AGSJSON_KEY_ACCESS_CONSTRAINTS
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_ACCESS_CONSTRAINTS:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_ACCESS_CONSTRAINTS)
                        }# yapf: enable
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
                            "path": lambda extension_name, _AGSJSON_KEY_ADDRESS: "$.extensions[?(@.typeName = '{}')].{}".format(extension_name, _AGSJSON_KEY_ADDRESS),
                            "parentPath": lambda extension_name: "$.extensions[?(@.typeName = '{}')]".format(extension_name),
                            "key": "address"
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_ADDRESS: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_ADDRESS)
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    administrative_area = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {# yapf: disable
                            "document": "main",
                            "path": lambda extension_name, _AGSJSON_KEY_ADMINISTRATIVE_AREA: "$.extensions[?(@.typeName = '{}')].{}".format(extension_name, _AGSJSON_KEY_ADMINISTRATIVE_AREA),
                            "parentPath": lambda extension_name: "$.extensions[?(@.typeName = '{}')]".format(extension_name),
                            "key": lambda _AGSJSON_KEY_ADMINISTRATIVE_AREA: _AGSJSON_KEY_ADMINISTRATIVE_AREA
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_ADMINISTRATIVE_AREA: 
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_ADMINISTRATIVE_AREA)
                        }# yapf: enable
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
                        {# yapf: disable
                            "document": "main",
                            "path": lambda extension_name, _AGSJSON_KEY_CITY: "$.extensions[?(@.typeName = '{}')].properties.{}".format(extension_name, _AGSJSON_KEY_CITY),
                            "parentPath": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties".format(extension_name),
                            "key": lambda _AGSJSON_KEY_CITY: _AGSJSON_KEY_CITY
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_CITY:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_CITY)
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    country = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {# yapf: disable
                            "document": "main",
                            "path": lambda extension_name, _AGSJSON_KEY_COUNTRY: "$.extensions[?(@.typeName = '{}')].properties.{}".format(extension_name, _AGSJSON_KEY_COUNTRY),
                            "parentPath": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties".format(extension_name),
                            "key": lambda _AGSJSON_KEY_COUNTRY: _AGSJSON_KEY_COUNTRY
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_COUNTRY:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_COUNTRY)
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    email = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {# yapf: disable
                            "document": "main",
                            "path": lambda extension_name, _AGSJSON_KEY_EMAIL: "$.extensions[?(@.typeName = '{}')].properties.{}".format(extension_name, _AGSJSON_KEY_EMAIL),
                            "parentPath": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties".format(extension_name),
                            "key": lambda _AGSJSON_KEY_EMAIL: _AGSJSON_KEY_EMAIL
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_EMAIL:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_EMAIL)
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    facsimile = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {# yapf: disable
                            "document": "main",
                            "path": lambda extension_name, _AGSJSON_KEY_FACSIMILE: "$.extensions[?(@.typeName = '{}')].properties.{}".format(extension_name, _AGSJSON_KEY_FACSIMILE),
                            "parentPath": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties".format(extension_name),
                            "key": lambda _AGSJSON_KEY_FACSIMILE: _AGSJSON_KEY_FACSIMILE
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_FACSIMILE:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_FACSIMILE)
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    fees = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {# yapf: disable
                            "document": "main",
                            "path": lambda extension_name, _AGSJSON_KEY_FEES: "$.extensions[?(@.typeName = '{}')].properties.{}".format(extension_name, _AGSJSON_KEY_FEES),
                            "parentPath": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties".format(extension_name),
                            "key": lambda _AGSJSON_KEY_FEES: _AGSJSON_KEY_FEES
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_FEES:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_FEES)
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    individual_name = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {# yapf: disable
                            "document": "main",
                            "path": lambda extension_name, _AGSJSON_KEY_INDIVIDUAL_NAME: "$.extensions[?(@.typeName = '{}')].properties.{}".format(extension_name, _AGSJSON_KEY_INDIVIDUAL_NAME),
                            "parentPath": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties".format(extension_name),
                            "key": lambda _AGSJSON_KEY_INDIVIDUAL_NAME: _AGSJSON_KEY_INDIVIDUAL_NAME
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_INDIVIDUAL_NAME:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_INDIVIDUAL_NAME)
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    keywords = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {# yapf: disable
                            "document": "main",
                            "path": lambda extension_name, _AGSJSON_KEY_KEYWORDS: "$.extensions[?(@.typeName = '{}')].properties.{}".format(extension_name, _AGSJSON_KEY_KEYWORDS),
                            "parentPath": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties".format(extension_name),
                            "key": lambda _AGSJSON_KEY_KEYWORDS: _AGSJSON_KEY_KEYWORDS
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_KEYWORDS:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_KEYWORDS)
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    name = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "constraints": {
                        "readOnly": True
                    },
                    "paths": [
                        {# yapf: disable
                            "document": "main",
                            "path": lambda extension_name, _AGSJSON_KEY_NAME: "$.extensions[?(@.typeName = '{}')].properties.{}".format(extension_name, _AGSJSON_KEY_NAME),
                            "parentPath": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties".format(extension_name),
                            "key": lambda _AGSJSON_KEY_NAME: _AGSJSON_KEY_NAME
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path":
                            lambda extension_name, _SDDRAFT_KEY_NAME: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_NAME)
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    phone = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {# yapf: disable
                            "document": "main",
                            "path": lambda extension_name, _AGSJSON_KEY_PHONE: "$.extensions[?(@.typeName = '{}')].properties.{}".format(extension_name, _AGSJSON_KEY_PHONE),
                            "parentPath": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties".format(extension_name),
                            "key": lambda _AGSJSON_KEY_PHONE: _AGSJSON_KEY_PHONE
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_PHONE:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_PHONE)
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    position_name = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {# yapf: disable
                            "document": "main",
                            "path": lambda extension_name, _AGSJSON_KEY_POSITION_NAME: "$.extensions[?(@.typeName = '{}')].properties.{}".format(extension_name, _AGSJSON_KEY_POSITION_NAME),
                            "parentPath": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties".format(extension_name),
                            "key": lambda _AGSJSON_KEY_POSITION_NAME: _AGSJSON_KEY_POSITION_NAME
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_POSITION_NAME:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_POSITION_NAME)
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    postal_code = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {# yapf: disable
                            "document": "main",
                            "path": lambda extension_name, _AGSJSON_KEY_POSTAL_CODE: "$.extensions[?(@.typeName = '{}')].properties.{}".format(extension_name, _AGSJSON_KEY_POSTAL_CODE),
                            "parentPath": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties".format(extension_name),
                            "key": lambda _AGSJSON_KEY_POSTAL_CODE: _AGSJSON_KEY_POSTAL_CODE
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_POSTAL_CODE:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_POSTAL_CODE)
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    provider_name = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {# yapf: disable
                            "document": "main",
                            "path": lambda extension_name, _AGSJSON_KEY_PROVIDER_NAME: "$.extensions[?(@.typeName = '{}')].properties.{}".format(extension_name, _AGSJSON_KEY_PROVIDER_NAME),
                            "parentPath": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties".format(extension_name),
                            "key": lambda _AGSJSON_KEY_PROVIDER_NAME: _AGSJSON_KEY_PROVIDER_NAME
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_PROVIDER_NAME:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_PROVIDER_NAME)
                        }# yapf: enable
                    ]
                }
            }
        }
    )

    title = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [
                        {# yapf: disable
                            "document": "main",
                            "path": lambda extension_name, _AGSJSON_KEY_TITLE: "$.extensions[?(@.typeName = '{}')].properties.{}".format(extension_name, _AGSJSON_KEY_TITLE),
                            "parentPath": lambda extension_name: "$.extensions[?(@.typeName = '{}')].properties".format(extension_name),
                            "key": lambda _AGSJSON_KEY_TITLE: _AGSJSON_KEY_TITLE
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path":
                            lambda extension_name, _SDDRAFT_KEY_TITLE: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_TITLE)
                        }# yapf: enable
                    ]
                }
            }
        }
    )