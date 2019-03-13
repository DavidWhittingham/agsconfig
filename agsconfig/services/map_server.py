# coding=utf-8
"""This module contains the MapServer class for editing MapServer configuration pre or post publish"""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

from enum import Enum

from .cacheable_mixin import CacheableMixin
from .image_dimensions_mixin import ImageDimensionsMixin
from .output_dir_mixin import OutputDirMixin
from .service_base import ServiceBase


class MapServer(OutputDirMixin, CacheableMixin, ImageDimensionsMixin, ServiceBase):
    class AntiAliasingMode(Enum):
        none = "None"
        fastest = "Fastest"
        fast = "Fast"
        normal = "Normal"
        best = "Best"

    class Capability(Enum):
        map = "Map"
        query = "Query"
        data = "Data"

    class TextAntiAliasingMode(Enum):
        none = "None"
        force = "Force"
        normal = "Normal"

    def __init__(self, editor):
        super().__init__(editor)
