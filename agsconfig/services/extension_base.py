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

from abc import ABCMeta
from enum import Enum
from ..model_base import ModelBase


class ExtensionBase(ModelBase):
    """Contains base settings/configuration that are common across ArcGIS Service extensions."""

    __metaclass__ = ABCMeta

    _editor = None
    extension_name = None

    class Capability(Enum):
        """Must be overridden by sub-classes if any capabilities are supported."""
        pass

    def __init__(self, editor, extensionName):
        """Initilises the class.

        Args:
            editor: An editor object that will receive metadata about each property
            extensionType: Used to find xpaths in sddrafts where there is more than one extension
        """

        self._editor = editor
        self.extension_name = extensionName

    def save(self):
        self._editor.save()

    def get_extension_name(self):
        return self.extension_name