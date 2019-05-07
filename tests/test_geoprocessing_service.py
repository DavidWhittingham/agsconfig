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

# import fixtures
from .helpers import geoprocessing_service_config as service_config
from agsconfig.services.geoprocessing_server import GeoprocessingServer

def test_load_service_config(service_config):
    # this just tests the fixture setup
    assert True


@pytest.mark.parametrize(
    ("attribute", "expected_value", "exception"),
    [
        ("britney_spears", "should cause an", AttributeError),  # because she isn't a member
        ("capabilities", [], None),
        ("execution_type", GeoprocessingServer.ExecutionType.asynchronous, None),
        ("cluster", "default", None),
        ("description", None, None),
        ("folder", 'Test', None),
        ("high_isolation", True, None),
        ("idle_timeout", 1800, None),
        ("instances_per_container", 1, None),
        ("max_instances", 2, None),
        ("maximum_records", 1000, None),
        ("min_instances", 1, None),
        ("name", "TTool2", None),
        ("recycle_interval", None, None),
        ("recycle_start_time", None, None),
        ("replace_existing", False, None),
        ("result_map_server", False, None),
        ("summary", "Test Extraction Service", None),
        ("show_messages", GeoprocessingServer.MessageLevel.none, None),
        ("usage_timeout", 600, None),
        ("wait_timeout", 60, None)
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
        ("execution_type", GeoprocessingServer.ExecutionType.asynchronous, GeoprocessingServer.ExecutionType.asynchronous, None),
        ("execution_type", "Synchronous", GeoprocessingServer.ExecutionType.synchronous, None),
        ("execution_type", "balls", None, ValueError),
        ("cluster", "any", "any", None),
        ("description", "Some description", "Some description", None),
        ("folder", 'Test2', "Test2", None),
        ("high_isolation", False, False, None),
        ("high_isolation", "blah", None, ValueError),
        ("idle_timeout", 180, 180, None),
        ("idle_timeout", "x", None, ValueError),
        ("instances_per_container", 2, 2, None),
        ("instances_per_container", 'x', None, ValueError),
        ("instances_per_container", -1, None, ValueError),
        ("max_instances", 3, 3, None),
        ("max_instances", -1, None, ValueError),
        ("max_instances", "x", None, ValueError),
        ("maximum_records", None, None, None),
        ("min_instances", 1, 1, None),
        ("min_instances", "x", None, ValueError),
        ("min_instances", -1, None, ValueError),
        ("name", "TTool2", "TTool2", None),
        ("recycle_interval", 10, 10, None),
        ("recycle_start_time", "23:00", datetime.time(23, 0), None),
        ("replace_existing", True, True, None),
        ("result_map_server", True, True, None),
        ("summary", "Service", "Service", None),
        ("show_messages", "Debug", GeoprocessingServer.MessageLevel.debug, None),
        ("usage_timeout", 60, 60, None),
        ("usage_timeout", -1, None, ValueError),
        ("usage_timeout", "x", None, ValueError),
        ("wait_timeout", 50, 50, None),
        ("wait_timeout", -1, None, ValueError),
        ("wait_timeout", "x", None, ValueError)
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