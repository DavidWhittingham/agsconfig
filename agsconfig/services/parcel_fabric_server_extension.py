"""This module contains the ParcelFabricServer extension class"""

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


class ParcelFabricServerExtension(ExtensionBase):
    """ ParcelFabricServer extension properties for ArcGIS services """
    class Capability(Enum):
        assign_features_to_record = "AssignFeaturesToRecord"
        build = "Build"
        change_parcel_type = "ChangeParcelType"
        clip = "Clip"
        copy_lines_to_parcel_type = "CopyLinesToParcelType"
        create_seeds = "CreateSeeds"
        delete_parcels = "DeleteParcels"
        duplicate_parcels = "DuplicateParcels"
        merge = "Merge"
        update_parcel_history = "UpdateParcelHistory"

    def __init__(self, editor):
        super().__init__(editor, "ParcelFabricServer")
