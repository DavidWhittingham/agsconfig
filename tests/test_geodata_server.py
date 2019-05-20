"""Tests for Geodata services."""
# Python 2/3 compatibility
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()

import os.path
import agsconfig
from agsconfig.services.geodata_server import GeodataServer

import pytest

from .helpers import geodata_service_config as service_config


def test_load_service_config(service_config):
    """Load a vector tile into a map sddraft object."""
    # this just tests the fixture setup
    assert True


def test_save(service_config):
    service_config.save()
    assert True


@pytest.mark.parametrize(
    ("capabilities", "expected", "ex"),
    [
        ([agsconfig.GeodataServer.Capability.query], [agsconfig.GeodataServer.Capability.query], None),
        ([], [], None),
        (["Query"], [agsconfig.GeodataServer.Capability.query], None),
        (["Fail"], None, ValueError),
        ([123], None, ValueError)
    ]
)  # yapf: disable
def test_capabilities(service_config, capabilities, expected, ex):
    if ex is not None:
        with pytest.raises(ex):
            service_config.capabilities = capabilities
    else:
        service_config.capabilities = capabilities
        assert set(service_config.capabilities) == set(expected)
