"""agsconfig


"""

# setup module logging with null handler
import logging as _logging
_logging.getLogger(__name__).addHandler(_logging.NullHandler())

from ._version import *
from .agsconfig import (
    load_geocode_sddraft, load_geocode_service, load_geodata_sddraft, load_geodata_service, load_geoprocessing_sddraft,
    load_geoprocessing_service, load_image_sddraft, load_image_service, load_map_sddraft, load_map_service,
    load_vector_tile_sddraft, load_vector_tile_service, load_hosted_feature_sddraft, load_hosted_feature_service
)
from .services.map_server import MapServer
from .services.geodata_server import GeodataServer
from .services.image_server import ImageServer
from .services.vector_tile_server import VectorTileServer, VectorTileServerExtension
from .services.wms_server_extension import WMSServerExtension
from .services.wfs_server_extension import WFSServerExtension
from .services.kml_server_extension import KmlServerExtension
from .services.na_server_extension import NAServerExtension
from .services.feature_server_extension import FeatureServerExtension