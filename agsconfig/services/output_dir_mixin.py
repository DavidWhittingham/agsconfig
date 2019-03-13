# coding=utf-8
"""This module contains the ServiceBase abstract base class for implementing ArcGIS Server service configuration models."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

from ..editing.edit_prop import EditorProperty


class OutputDirMixin(object):

    "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key = 'FilePath']/Value"

    output_dir = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.outputDir"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key = 'outputDir']/Value",
                            "parentPath":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray",
                            "tag":
                            "PropertySetProperty",
                            "attributes": {
                                "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:PropertySetProperty"
                            },
                            "children": [
                                {
                                    "tag": "Key",
                                    "value": "outputDir"
                                },
                                {
                                    "tag": "Value",
                                    "attributes": {
                                        "{http://www.w3.org/2001/XMLSchema-instance}type": "xs:string"
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        }
    )

    virtual_output_dir = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.virtualOutputDir"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key = 'virtualOutputDir']/Value",
                            "parentPath":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray",
                            "tag":
                            "PropertySetProperty",
                            "attributes": {
                                "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:PropertySetProperty"
                            },
                            "children": [
                                {
                                    "tag": "Key",
                                    "value": "virtualOutputDir"
                                },
                                {
                                    "tag": "Value",
                                    "attributes": {
                                        "{http://www.w3.org/2001/XMLSchema-instance}type": "xs:string"
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        }
    )
