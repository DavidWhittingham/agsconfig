# coding=utf-8
"""This module contains helpers that are used across multiple test modules."""

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

TRUEISH_TEST_PARAMS = [
    (True, True),
    ("TRUE", True),
    ("T", True),
    ("tRUe", True),
    ("t", True),
    (False, False),
    ("FALSE", False),
    ("F", False),
    ("faLSe", False),
    ("f", False),
    (1, True),
    (0, False),
    (2, False),
    (-1, False)
]

SDDRAFT_FILE_PATH = os.path.abspath("{0}/samples/mapservice.sddraft".format(os.path.dirname(__file__)))
SDDRAFT_FILE_PATH_COPY = os.path.abspath("{0}/samples/mapservice.copy.sddraft".format(os.path.dirname(__file__)))

MAIN_JSON_FILE_PATH = os.path.abspath("{0}/samples/mapservice.main.json".format(os.path.dirname(__file__)))
MAIN_JSON_FILE_PATH_COPY = os.path.abspath("{0}/samples/mapservice.main.copy.json".format(os.path.dirname(__file__)))

INFO_JSON_FILE_PATH = os.path.abspath("{0}/samples/mapservice.itemInfo.json".format(os.path.dirname(__file__)))
INFO_JSON_FILE_PATH_COPY = os.path.abspath(
    "{0}/samples/mapservice.itemInfo.copy.json".format(os.path.dirname(__file__))
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
def map_service_config(request):
    for p in request.param["paths"]:
        shutil.copyfile(p[0], p[1])

    with ExitStack() as stack:
        files = [stack.enter_context(open(p[1], mode="rb+")) for p in request.param["paths"]]
        yield request.param["func"](*files)