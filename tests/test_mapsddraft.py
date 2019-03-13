# Python 2/3 compatibility
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()

import os.path
import shutil

import agsconfig

import pytest

from contextlib2 import ExitStack

SDDRAFT_FILE_PATH = os.path.abspath("{0}/samples/mapservice.sddraft".format(os.path.dirname(__file__)))
SDDRAFT_FILE_PATH_COPY = os.path.abspath("{0}/samples/mapservice.copy.sddraft".format(os.path.dirname(__file__)))
SDDRAFT_SAVE_TEST_FILE_PATH = os.path.abspath(
    "{0}/samples/mapservice.savetest.sddraft".format(os.path.dirname(__file__))
)

MAIN_JSON_FILE_PATH = os.path.abspath("{0}/samples/mapservice.main.json".format(os.path.dirname(__file__)))
MAIN_JSON_FILE_PATH_COPY = os.path.abspath("{0}/samples/mapservice.main.copy.json".format(os.path.dirname(__file__)))
MAIN_JSON_SAVE_TEST_FILE_PATH = os.path.abspath(
    "{0}/samples/mapservice.main.savetest.json".format(os.path.dirname(__file__))
)

INFO_JSON_FILE_PATH = os.path.abspath("{0}/samples/mapservice.itemInfo.json".format(os.path.dirname(__file__)))
INFO_JSON_FILE_PATH_COPY = os.path.abspath(
    "{0}/samples/mapservice.itemInfo.copy.json".format(os.path.dirname(__file__))
)
INFO_JSON_SAVE_TEST_FILE_PATH = os.path.abspath(
    "{0}/samples/mapservice.itemInfo.savetest.json".format(os.path.dirname(__file__))
)


def get_map_sddraft(fp):
    return agsconfig.load_map_sddraft(fp)


def get_map_service(main_json_fp, info_json_fp):
    return agsconfig.load_map_service(main_json_fp, info_json_fp)


@pytest.fixture(
    params=[
        {
            "func": get_map_sddraft,
            "paths": [(SDDRAFT_FILE_PATH, SDDRAFT_FILE_PATH_COPY)]
        },
        {
            "func": get_map_service,
            "paths": [(MAIN_JSON_FILE_PATH, MAIN_JSON_FILE_PATH_COPY), (INFO_JSON_FILE_PATH, INFO_JSON_FILE_PATH_COPY)]
        }
    ]
)
def service_config(request):
    for p in request.param["paths"]:
        shutil.copyfile(p[0], p[1])

    with ExitStack() as stack:
        files = [stack.enter_context(open(p[1], mode="rb+")) for p in request.param["paths"]]
        yield request.param["func"](*files)


# import tests that should be applied to MapServer
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-position
from .sddraftbase import *
from .cacheable import *
from .image_dimensions import *
from .max_record_count import *
from .output_dir import *
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-position


def test_load_service_config(service_config):
    # this just tests the fixture setup
    assert True


def test_save(service_config):
    service_config.save()
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
