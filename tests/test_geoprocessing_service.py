"""Tests for geoprocessing services."""

# Python 2/3 compatibility
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()

# Third-party imports
import pytest
import datetime

# import agsconfig bits for comparisons
from agsconfig.services.geoprocessing_server import GeoprocessingServer

# import fixtures
from .helpers import geoprocessing_service_config as service_config
from .output_dir_mixin import *
from .service_base_mixin import *
from .wps_server_extension_mixin import *


def test_load_service_config(service_config):
    # this just tests the fixture setup
    assert True


@pytest.mark.parametrize(
    ("attribute", "expected_value", "exception"),
    [
        ("britney_spears", "should cause an", AttributeError),  # because she isn't a member
        ("capabilities", [], None),
        ("cluster", "default", None),
        ("execution_type", GeoprocessingServer.ExecutionType.asynchronous, None),
        ("maximum_records", 1000, None),
        ("result_map_server", False, None),
        ("show_messages", GeoprocessingServer.MessageLevel.none, None)
    ]
)
def test_getters(service_config, attribute, expected_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            assert getattr(service_config, attribute) == expected_value
    else:
        assert getattr(service_config, attribute) == expected_value


@pytest.mark.parametrize(
    ("attribute", "new_value", "expected_value", "exception"),
    [
        ("britney_spears", "should cause a", None, TypeError),  # because she isn't a member
        ("capabilities", [GeoprocessingServer.Capability.uploads], [GeoprocessingServer.Capability.uploads], None),
        ("capabilities", ["Uploads"], [GeoprocessingServer.Capability.uploads], None),
        ("capabilities", "Guff", None, ValueError),
        (
            "execution_type", GeoprocessingServer.ExecutionType.asynchronous,
            GeoprocessingServer.ExecutionType.asynchronous, None
        ),
        ("execution_type", "Synchronous", GeoprocessingServer.ExecutionType.synchronous, None),
        ("execution_type", "balls", None, ValueError),
        ("maximum_records", None, None, None),
        ("result_map_server", True, True, None),
        ("show_messages", "Info", GeoprocessingServer.MessageLevel.info, None)
    ]
)
def test_setters(service_config, attribute, new_value, expected_value, exception):
    if exception is not None:
        with pytest.raises(exception):
            setattr(service_config, attribute, new_value)
    else:
        setattr(service_config, attribute, new_value)
        assert getattr(service_config, attribute) == expected_value


def test_setter(service_config):
    setattr(service_config, "usage_timeout", 10)