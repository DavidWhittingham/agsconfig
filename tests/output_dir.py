# coding=utf-8
"""This module contains shared tests for all models that implement output directories."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

import pytest


@pytest.mark.parametrize(
    ("output_dir", "ex"),
    [("C:\\arcgisserver\\arcgisoutput", None), ("\\\\smbserver\\arcgisserver\\arcgisoutput", None)]
)
def test_output_dir(service_config, output_dir, ex):
    if (ex != None):
        with pytest.raises(ex):
            service_config.output_dir = output_dir
    else:
        service_config.output_dir = output_dir
        assert service_config.output_dir == output_dir
        service_config.save()


@pytest.mark.parametrize(("virtual_output_dir", "ex"), [("/rest/directories/arcgisoutput", None)])
def test_virtual_output_dir(service_config, virtual_output_dir, ex):
    if (ex != None):
        with pytest.raises(ex):
            service_config.virtual_output_dir = virtual_output_dir
    else:
        service_config.virtual_output_dir = virtual_output_dir
        assert service_config.virtual_output_dir == virtual_output_dir
        service_config.save()
