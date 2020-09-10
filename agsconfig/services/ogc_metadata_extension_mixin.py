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
    _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE = {
        "children": [{
            "key": "properties",
            "value": {}
        }],
        "parent": lambda _AGSJSON_EXTENSION_STRUCTURE: _AGSJSON_EXTENSION_STRUCTURE
    }

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
                            "parent": {
                                "children": [
                                    {
                                        "key": lambda _AGSJSON_KEY_ABSTRACT: _AGSJSON_KEY_ABSTRACT
                                    }
                                ],
                                "parent": lambda _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE: _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE
                            }
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_ABSTRACT:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_ABSTRACT),
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
                                                    "value": lambda _SDDRAFT_KEY_ABSTRACT: "{}".format(_SDDRAFT_KEY_ABSTRACT)
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
                    "conversions": [{
                        "id": "htmlToText"
                    }],
                    "paths": [
                        {# yapf: disable
                            "document": "main",
                            "path": lambda extension_name, _AGSJSON_KEY_ACCESS_CONSTRAINTS: "$.extensions[?(@.typeName = '{}')].properties.{}".format(extension_name, _AGSJSON_KEY_ACCESS_CONSTRAINTS),
                            "parent": {
                                "children": [
                                    {
                                        "key": lambda _AGSJSON_KEY_ACCESS_CONSTRAINTS: _AGSJSON_KEY_ACCESS_CONSTRAINTS
                                    }
                                ],
                                "parent": lambda _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE: _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE
                            }
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "conversions": [{
                        "id": "htmlToText"
                    }],
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_ACCESS_CONSTRAINTS:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_ACCESS_CONSTRAINTS),
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
                                                    "value": lambda _SDDRAFT_KEY_ACCESS_CONSTRAINTS: "{}".format(_SDDRAFT_KEY_ACCESS_CONSTRAINTS)
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
                            "parent": {
                                "children": [
                                    {
                                        "key": "address"
                                    }
                                ],
                                "parent": lambda _AGSJSON_EXTENSION_STRUCTURE: _AGSJSON_EXTENSION_STRUCTURE
                            }
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_ADDRESS: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_ADDRESS),
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
                                                    "value": lambda _SDDRAFT_KEY_ADDRESS: "{}".format(_SDDRAFT_KEY_ADDRESS)
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
                            "parent": {
                                "children": [
                                    {
                                        "key": lambda _AGSJSON_KEY_ADMINISTRATIVE_AREA: _AGSJSON_KEY_ADMINISTRATIVE_AREA
                                    }
                                ],
                                "parent": lambda _AGSJSON_EXTENSION_STRUCTURE: _AGSJSON_EXTENSION_STRUCTURE
                            }
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_ADMINISTRATIVE_AREA:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_ADMINISTRATIVE_AREA),
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
                                                    "value": lambda _SDDRAFT_KEY_ADMINISTRATIVE_AREA: "{}".format(_SDDRAFT_KEY_ADMINISTRATIVE_AREA)
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
                            "parent": {
                                "children": [
                                    {
                                        "key": lambda _AGSJSON_KEY_CITY: _AGSJSON_KEY_CITY
                                    }
                                ],
                                "parent": lambda _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE: _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE
                            }
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_CITY:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_CITY),
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
                                                    "value": lambda _SDDRAFT_KEY_CITY: "{}".format(_SDDRAFT_KEY_CITY)
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
                            "parent": {
                                "children": [
                                    {
                                        "key": lambda _AGSJSON_KEY_COUNTRY: _AGSJSON_KEY_COUNTRY
                                    }
                                ],
                                "parent": lambda _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE: _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE
                            }
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_COUNTRY:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_COUNTRY),
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
                                                    "value": lambda _SDDRAFT_KEY_COUNTRY: "{}".format(_SDDRAFT_KEY_COUNTRY)
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
                            "parent": {
                                "children": [
                                    {
                                        "key": lambda _AGSJSON_KEY_EMAIL: _AGSJSON_KEY_EMAIL
                                    }
                                ],
                                "parent": lambda _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE: _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE
                            }
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_EMAIL:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_EMAIL),
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
                                                    "value": lambda _SDDRAFT_KEY_EMAIL: "{}".format(_SDDRAFT_KEY_EMAIL)
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
                            "parent": {
                                "children": [
                                    {
                                        "key": lambda _AGSJSON_KEY_FACSIMILE: _AGSJSON_KEY_FACSIMILE
                                    }
                                ],
                                "parent": lambda _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE: _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE
                            }
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_FACSIMILE:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_FACSIMILE),
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
                                                    "value": lambda _SDDRAFT_KEY_FACSIMILE: "{}".format(_SDDRAFT_KEY_FACSIMILE)
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
                            "parent": {
                                "children": [
                                    {
                                        "key": lambda _AGSJSON_KEY_FEES: _AGSJSON_KEY_FEES
                                    }
                                ],
                                "parent": lambda _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE: _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE
                            }
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_FEES:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_FEES),
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
                                                    "value": lambda _SDDRAFT_KEY_FEES: "{}".format(_SDDRAFT_KEY_FEES)
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
                            "parent": {
                                "children": [
                                    {
                                        "key": lambda _AGSJSON_KEY_INDIVIDUAL_NAME: _AGSJSON_KEY_INDIVIDUAL_NAME
                                    }
                                ],
                                "parent": lambda _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE: _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE
                            }
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_INDIVIDUAL_NAME:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_INDIVIDUAL_NAME),
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
                                                    "value": lambda _SDDRAFT_KEY_INDIVIDUAL_NAME: "{}".format(_SDDRAFT_KEY_INDIVIDUAL_NAME)
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
                            "parent": {
                                "children": [
                                    {
                                        "key": lambda _AGSJSON_KEY_KEYWORDS: _AGSJSON_KEY_KEYWORDS
                                    }
                                ],
                                "parent": lambda _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE: _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE
                            }
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_KEYWORDS:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_KEYWORDS),
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
                                                    "value": lambda _SDDRAFT_KEY_KEYWORDS: "{}".format(_SDDRAFT_KEY_KEYWORDS)
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
                            "parent": {
                                "children": [
                                    {
                                        "key": lambda _AGSJSON_KEY_NAME: _AGSJSON_KEY_NAME
                                    }
                                ],
                                "parent": lambda _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE: _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE
                            }
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path":
                                lambda extension_name, _SDDRAFT_KEY_NAME:
                                    "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_NAME),
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
                                                    "value": lambda _SDDRAFT_KEY_NAME: "{}".format(_SDDRAFT_KEY_NAME)
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
                            "parent": {
                                "children": [
                                    {
                                        "key": lambda _AGSJSON_KEY_PHONE: _AGSJSON_KEY_PHONE
                                    }
                                ],
                                "parent": lambda _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE: _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE
                            }
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_PHONE:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_PHONE),
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
                                                    "value": lambda _SDDRAFT_KEY_PHONE: "{}".format(_SDDRAFT_KEY_PHONE)
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
                            "parent": {
                                "children": [
                                    {
                                        "key": lambda _AGSJSON_KEY_POSITION_NAME: _AGSJSON_KEY_POSITION_NAME
                                    }
                                ],
                                "parent": lambda _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE: _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE
                            }
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_POSITION_NAME:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_POSITION_NAME),
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
                                                    "value": lambda _SDDRAFT_KEY_POSITION_NAME: "{}".format(_SDDRAFT_KEY_POSITION_NAME)
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
                            "parent": {
                                "children": [
                                    {
                                        "key": lambda _AGSJSON_KEY_POSTAL_CODE: _AGSJSON_KEY_POSTAL_CODE
                                    }
                                ],
                                "parent": lambda _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE: _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE
                            }
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_POSTAL_CODE:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_POSTAL_CODE),
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
                                                    "value": lambda _SDDRAFT_KEY_POSTAL_CODE: "{}".format(_SDDRAFT_KEY_POSTAL_CODE)
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
                            "parent": {
                                "children": [
                                    {
                                        "key": lambda _AGSJSON_KEY_PROVIDER_NAME: _AGSJSON_KEY_PROVIDER_NAME
                                    }
                                ],
                                "parent": lambda _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE: _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE
                            }
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path": lambda extension_name, _SDDRAFT_KEY_PROVIDER_NAME:
                                "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_PROVIDER_NAME),
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
                                                    "value": lambda _SDDRAFT_KEY_PROVIDER_NAME: "{}".format(_SDDRAFT_KEY_PROVIDER_NAME)
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
                            "parent": {
                                "children": [
                                    {
                                        "key": lambda _AGSJSON_KEY_TITLE: _AGSJSON_KEY_TITLE
                                    }
                                ],
                                "parent": lambda _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE: _AGSJSON_EXTENSION_PROPERTIES_STRUCTURE
                            }
                        }# yapf: enable
                    ]
                },
                "sddraft": {
                    "paths": [
                        {# yapf: disable
                            "path":
                                lambda extension_name, _SDDRAFT_KEY_TITLE:
                                    "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{}']/Props/PropertyArray/PropertySetProperty[Key='{}']/Value".format(extension_name, _SDDRAFT_KEY_TITLE),
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
                                                    "value": lambda _SDDRAFT_KEY_TITLE: "{}".format(_SDDRAFT_KEY_TITLE)
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
                        }# yapf: enable
                    ]
                }
            }
        }
    )