"""This module contains the ValidationServer extension class"""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

from .extension_base import ExtensionBase
from .._enum import StrEnum as Enum


class ValidationServerExtension(ExtensionBase):
    """ ValidationServer extension properties for ArcGIS services """
    class Capability(Enum):
        evaluate = "Evaluate"
        update_errors = "UpdateErrors"

    def __init__(self, editor):
        super().__init__(editor, "ValidationServer")
