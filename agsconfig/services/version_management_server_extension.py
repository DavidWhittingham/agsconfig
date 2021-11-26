"""This module contains the VersionManagementServer extension class"""

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


class VersionManagementServerExtension(ExtensionBase):
    """ VersionManagementServer extension properties for ArcGIS services """
    class Capability(Enum):
        alter = "Alter"
        conflicts = "Conflicts"
        create = "Create"
        delete = "Delete"
        delete_forward_edits = "DeleteForwardEdits"
        differences = "Differences"
        inspect_conflicts = "InspectConflicts"
        lock_infos = "LockInfos"
        post = "Post"
        purge_lock = "PurgeLock"
        reconcile = "Reconcile"
        start_editing = "StartEditing"
        start_reading = "StartReading"
        stop_editing = "StopEditing"
        stop_reading = "StopReading"
        version_infos = "VersionInfos"

    def __init__(self, editor):
        super().__init__(editor, "VersionManagementServer")
