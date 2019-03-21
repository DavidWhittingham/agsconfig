# coding=utf-8
"""This module contains top-level functionality for the agsconfig module."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

from .editing.sdd_editor import SDDraftEditor
from .editing.ags_json_editor import AgsJsonEditor
from .services.map_server import MapServer
from .services.vectortile_server import VectorTileServer
from .services.image_server import ImageServer

def load_map_sddraft(sddraft_file):
    return MapServer(SDDraftEditor(sddraft_file))

def load_vectortile_sddraft(sddraft_file):
    return VectorTileServer(SDDraftEditor(sddraft_file))

def load_image_sddraft(sddraft_file):
    return ImageServer(SDDraftEditor(sddraft_file))

def load_map_service(service_file, item_info_file):
    return MapServer(AgsJsonEditor(service_file, item_info_file))