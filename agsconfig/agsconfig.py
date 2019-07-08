# coding=utf-8
"""This module contains top-level functionality for the agsconfig module."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position,no-name-in-module,import-error
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position,no-name-in-module,import-error

from .editing.sdd_editor import SDDraftEditor
from .editing.ags_json_editor import AgsJsonEditor
from .services.geocode_server import GeocodeServer
from .services.geodata_server import GeodataServer
from .services.geoprocessing_server import GeoprocessingServer
from .services.hosted_feature_server import HostedFeatureServer
from .services.image_server import ImageServer
from .services.map_server import MapServer
from .services.vector_tile_server import VectorTileServer


def load_geocode_sddraft(sddraft_file):
    return GeocodeServer(SDDraftEditor(sddraft_file))


def load_geocode_service(service_file, item_info_file):
    return GeocodeServer(AgsJsonEditor(service_file, item_info_file))


def load_geodata_sddraft(sddraft_file):
    return GeodataServer(SDDraftEditor(sddraft_file))


def load_geodata_service(service_file, item_info_file):
    return GeodataServer(AgsJsonEditor(service_file, item_info_file))


def load_geoprocessing_sddraft(sddraft_file):
    return GeoprocessingServer(SDDraftEditor(sddraft_file))


def load_geoprocessing_service(service_file, item_info_file):
    return GeoprocessingServer(AgsJsonEditor(service_file, item_info_file))


def load_hosted_feature_sddraft(sddraft_file):
    return HostedFeatureServer(SDDraftEditor(sddraft_file))


def load_hosted_feature_service(service_file, item_info_file):
    return HostedFeatureServer(AgsJsonEditor(service_file, item_info_file))


def load_image_sddraft(sddraft_file):
    return ImageServer(SDDraftEditor(sddraft_file))


def load_image_service(service_file, item_info_file):
    return ImageServer(AgsJsonEditor(service_file, item_info_file))


def load_map_sddraft(sddraft_file):
    return MapServer(SDDraftEditor(sddraft_file))


def load_map_service(service_file, item_info_file):
    return MapServer(AgsJsonEditor(service_file, item_info_file))


def load_vector_tile_sddraft(sddraft_file):
    return VectorTileServer(SDDraftEditor(sddraft_file))


def load_vector_tile_service(service_file, item_info_file):
    return VectorTileServer(AgsJsonEditor(service_file, item_info_file))
