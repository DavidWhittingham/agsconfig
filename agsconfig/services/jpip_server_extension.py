"""This module contains the jpip Server extension class"""

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

class JPIPServerExtension(ExtensionBase):
    """ jpip server extension properties for arcGIS services """

    def __init__(self, editor):
        super().__init__(editor, "JPIPServer")

    enabled = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name : "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Enabled".format(extension_name)
                        }
                    ]
                }
            }
        })
