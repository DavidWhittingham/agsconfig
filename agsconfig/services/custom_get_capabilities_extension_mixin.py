"""This module contains the Custom Get Capabilities extension mixin"""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

from ..editing.edit_prop import EditorProperty
from .extension_base import ExtensionBase

class CustomGetCapabilitiesExtensionMixin(ExtensionBase):
    """ Attributes for custom Get Capabilities on ArcGIS services """

    extension_name = None

    def __init__(self, editor, extensionName):
        super().__init__(editor, extensionName)
        extension_name = super().get_extension_name()

    customGetCapabilities = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name : "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='customGetCapabilities']/Value".format(extension_name)
                        }
                    ]
                }
            }
        })

    pathToCustomGetCapabilitiesFiles = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name : "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='pathToCustomGetCapabilitiesFiles']/Value".format(extension_name)
                        }
                    ]
                }
            }
        })

