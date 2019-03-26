# coding=utf-8
"""This module contains tests for map services."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

import os.path
import shutil

import pytest
from contextlib2 import ExitStack

import agsconfig

# Import shared fixtures
# pylint: disable=unused-import
from .helpers import map_service_config as service_config
# pylint: enable=unused-import

# import tests that should be applied to MapServer
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-position
from .service_base import *
from .cacheable_core import *
from .cacheable_ext import *
from .feature_server_extension import *
from .kml_server_extension import *
from .image_dimensions import *
from .max_record_count import *
from .na_server_extension import *
from .output_dir import *
from .wcs_server_extension import *
from .wfs_server_extension import *
from .wms_server_extension import *
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-position


def test_load_service_config(service_config):
    # this just tests the fixture setup
    assert True


def test_save(service_config):
    service_config.save()
    assert True

def test_save_a_copy(service_config):
    sddraft_file = "{0}/samples/mapservice.sddraft".format(os.path.dirname(__file__))
    with open(sddraft_file, "rb+") as f:
        draft = agsconfig.load_map_sddraft(f)
    draft.save_a_copy(sddraft_file.replace('.sddraft', '.copy.sddraft'))
    assert True

@pytest.mark.parametrize(
    ("capabilities", "expected", "ex"),
    [
        ([agsconfig.MapServer.Capability.map], [agsconfig.MapServer.Capability.map], None),
        ([], [], None),
        (["Query"], [agsconfig.MapServer.Capability.query], None),
        (["Fail"], None, ValueError),
        ([123], None, TypeError)
    ]
)  # yapf: disable
def test_capabilities(service_config, capabilities, expected, ex):
    if ex != None:
        with pytest.raises(ex):
            service_config.capabilities = capabilities
    else:
        service_config.capabilities = capabilities
        assert set(service_config.capabilities) == set(expected)
