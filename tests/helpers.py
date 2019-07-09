# coding=utf-8
"""This module contains helpers that are used across multiple test modules."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

# Python lib imports
import errno
import io
import os
import shutil

# Third-party imports
import pytest
from contextlib2 import ExitStack

# Local imports
import agsconfig

TRUEISH_TEST_PARAMS = [
    (True, True), ("TRUE", True), ("T", True), ("tRUe", True), ("t", True), (False, False), ("FALSE", False),
    ("F", False), ("faLSe", False), ("f", False), (1, True), (0, False), (2, False), (-1, False)
]

GEODATA_SDDRAFT_FILE_PATH = os.path.abspath("{0}/samples/geodataservice.sddraft".format(os.path.dirname(__file__)))
GEODATA_SDDRAFT_FILE_PATH_COPY = os.path.abspath(
    "{0}/samples/geodataservice.copy.sddraft".format(os.path.dirname(__file__))
)

GEODATA_MAIN_JSON_FILE_PATH = os.path.abspath("{0}/samples/geodataservice.main.json".format(os.path.dirname(__file__)))
GEODATA_MAIN_JSON_FILE_PATH_COPY = os.path.abspath(
    "{0}/samples/geodataservice.main.copy.json".format(os.path.dirname(__file__))
)

GEODATA_INFO_JSON_FILE_PATH = os.path.abspath(
    "{0}/samples/geodataservice.itemInfo.json".format(os.path.dirname(__file__))
)
GEODATA_INFO_JSON_FILE_PATH_COPY = os.path.abspath(
    "{0}/samples/geodataservice.itemInfo.copy.json".format(os.path.dirname(__file__))
)

MAP_SDDRAFT_FILE_PATH = os.path.abspath("{0}/samples/mapservice.sddraft".format(os.path.dirname(__file__)))
MAP_SDDRAFT_FILE_PATH_COPY = os.path.abspath("{0}/samples/mapservice.copy.sddraft".format(os.path.dirname(__file__)))

MAP_MAIN_JSON_FILE_PATH = os.path.abspath("{0}/samples/mapservice.main.json".format(os.path.dirname(__file__)))
MAP_MAIN_JSON_FILE_PATH_COPY = os.path.abspath(
    "{0}/samples/mapservice.main.copy.json".format(os.path.dirname(__file__))
)

MAP_INFO_JSON_FILE_PATH = os.path.abspath("{0}/samples/mapservice.itemInfo.json".format(os.path.dirname(__file__)))
MAP_INFO_JSON_FILE_PATH_COPY = os.path.abspath(
    "{0}/samples/mapservice.itemInfo.copy.json".format(os.path.dirname(__file__))
)

IMAGE_SDDRAFT_FILE_PATH = os.path.abspath("{0}/samples/imageservice.sddraft".format(os.path.dirname(__file__)))
IMAGE_SDDRAFT_FILE_PATH_COPY = os.path.abspath(
    "{0}/samples/imageservice.copy.sddraft".format(os.path.dirname(__file__))
)
IMAGE_MAIN_JSON_FILE_PATH = os.path.abspath("{0}/samples/imageservice.main.json".format(os.path.dirname(__file__)))
IMAGE_MAIN_JSON_FILE_PATH_COPY = os.path.abspath(
    "{0}/samples/imageservice.main.copy.json".format(os.path.dirname(__file__))
)
IMAGE_INFO_JSON_FILE_PATH = os.path.abspath("{0}/samples/imageservice.itemInfo.json".format(os.path.dirname(__file__)))
IMAGE_INFO_JSON_FILE_PATH_COPY = os.path.abspath(
    "{0}/samples/imageservice.itemInfo.copy.json".format(os.path.dirname(__file__))
)

VECTOR_TILE_SDDRAFT_FILE_PATH = os.path.abspath(
    "{0}/samples/vectortileservice.sddraft".format(os.path.dirname(__file__))
)
VECTOR_TILE_SDDRAFT_FILE_PATH_COPY = os.path.abspath(
    "{0}/samples/vectortileservice.copy.sddraft".format(os.path.dirname(__file__))
)
VECTOR_TILE_MAIN_JSON_FILE_PATH = os.path.abspath(
    "{0}/samples/vectortileservice.main.json".format(os.path.dirname(__file__))
)
VECTOR_TILE_MAIN_JSON_FILE_PATH_COPY = os.path.abspath(
    "{0}/samples/vectortileservice.main.copy.json".format(os.path.dirname(__file__))
)
VECTOR_TILE_INFO_JSON_FILE_PATH = os.path.abspath(
    "{0}/samples/vectortileservice.itemInfo.json".format(os.path.dirname(__file__))
)
VECTOR_TILE_INFO_JSON_FILE_PATH_COPY = os.path.abspath(
    "{0}/samples/vectortileservice.itemInfo.copy.json".format(os.path.dirname(__file__))
)

GEOPROCESSING_FILE_PATH = os.path.abspath("{0}/samples/pythongpservice.sddraft".format(os.path.dirname(__file__)))
GEOPROCESSING_FILE_PATH_COPY = os.path.abspath(
    "{0}/samples/pythongpservice.copy.sddraft".format(os.path.dirname(__file__))
)

HOSTED_FEATURE_SDDRAFT = os.path.abspath("{0}/samples/hosted_feature.sddraft".format(os.path.dirname(__file__)))
HOSTED_FEATURE_SDDRAFT_COPY = os.path.abspath(
    "{0}/samples/hosted_feature.copy.sddraft".format(os.path.dirname(__file__))
)
HOSTED_FEATURE_MAIN_JSON = os.path.abspath("{0}/samples/hosted_feature.main.json".format(os.path.dirname(__file__)))
HOSTED_FEATURE_MAIN_JSON_COPY = os.path.abspath(
    "{0}/samples/hosted_feature.main.copy.json".format(os.path.dirname(__file__))
)
HOSTED_FEATURE_INFO_JSON = os.path.abspath("{0}/samples/hosted_feature.itemInfo.json".format(os.path.dirname(__file__)))
HOSTED_FEATURE_INFO_JSON_COPY = os.path.abspath(
    "{0}/samples/hosted_feature.itemInfo.copy.json".format(os.path.dirname(__file__))
)


def get_map_sddraft(file_path):
    return agsconfig.load_map_sddraft(file_path)


def get_map_service(main_json_fp, info_json_fp):
    # Reading files in and turning into binary file objects
    # This is the most likely use case for editing this data (following on from requesting the REST objects from ArcGIS
    # Server and having them in memory), so we need a test case that makes sure this works.
    main_json_bin = main_json_fp.read()
    info_json_bin = info_json_fp.read()
    return agsconfig.load_map_service(io.BytesIO(main_json_bin), io.BytesIO(info_json_bin))


def get_geodata_sddraft(file_path):
    return agsconfig.load_geodata_sddraft(file_path)


def get_geodata_service(main_json_fp, info_json_fp):
    # Reading files in and turning into binary file objects
    # This is the most likely use case for editing this data (following on from requesting the REST objects from ArcGIS
    # Server and having them in memory), so we need a test case that makes sure this works.
    main_json_bin = main_json_fp.read()
    info_json_bin = info_json_fp.read()
    return agsconfig.load_geodata_service(io.BytesIO(main_json_bin), io.BytesIO(info_json_bin))


def get_image_sddraft(file_path):
    return agsconfig.load_image_sddraft(file_path)


def get_image_service(main_json_fp, info_json_fp):
    return agsconfig.load_image_service(main_json_fp, info_json_fp)


def get_vector_tile_sddraft(file_path):
    return agsconfig.load_vector_tile_sddraft(file_path)


def get_vector_tile_service(main_json_fp, info_json_fp):
    return agsconfig.load_vector_tile_service(main_json_fp, info_json_fp)


def get_geoprocessing_sddraft(file_path):
    return agsconfig.load_geoprocessing_sddraft(file_path)


def get_hosted_feature_sddraft(file_path):
    return agsconfig.load_hosted_feature_sddraft(file_path)


def get_hosted_feature_service(main_json_fp, info_json_fp):
    return agsconfig.load_hosted_feature_service(main_json_fp, info_json_fp)


@pytest.fixture(
    scope="function",
    params=[
        {
            "func": get_map_sddraft,
            "paths": [(MAP_SDDRAFT_FILE_PATH, MAP_SDDRAFT_FILE_PATH_COPY)]
        },
        {
            "func": get_map_service,
            "paths": [
                (MAP_MAIN_JSON_FILE_PATH, MAP_MAIN_JSON_FILE_PATH_COPY),
                (MAP_INFO_JSON_FILE_PATH, MAP_INFO_JSON_FILE_PATH_COPY)
            ]
        }
    ]
)
def map_service_config(request):
    for s in _load_service_yield_on_func(request):
        yield s


@pytest.fixture(
    scope="function",
    params=[
        {
            "func": get_hosted_feature_sddraft,
            "paths": [(HOSTED_FEATURE_SDDRAFT, HOSTED_FEATURE_SDDRAFT_COPY)]
        },
        {
            "func":
            get_hosted_feature_service,
            "paths": [
                (HOSTED_FEATURE_MAIN_JSON, HOSTED_FEATURE_MAIN_JSON_COPY),
                (HOSTED_FEATURE_INFO_JSON, HOSTED_FEATURE_INFO_JSON_COPY)
            ]
        }
    ]
)
def hosted_feature_config(request):
    for s in _load_service_yield_on_func(request):
        yield s


@pytest.fixture(
    scope="function",
    params=[{
        "func": get_geoprocessing_sddraft,
        "paths": [(GEOPROCESSING_FILE_PATH, GEOPROCESSING_FILE_PATH_COPY)]
    }]
)
def geoprocessing_service_config(request):
    for s in _load_service_yield_on_func(request):
        yield s


@pytest.fixture(
    scope="function",
    params=[
        {
            "func": get_geodata_sddraft,
            "paths": [(GEODATA_SDDRAFT_FILE_PATH, GEODATA_SDDRAFT_FILE_PATH_COPY)]
        },
        {
            "func":
            get_geodata_service,
            "paths": [
                (GEODATA_MAIN_JSON_FILE_PATH, GEODATA_MAIN_JSON_FILE_PATH_COPY),
                (GEODATA_INFO_JSON_FILE_PATH, GEODATA_INFO_JSON_FILE_PATH_COPY)
            ]
        }
    ]
)
def geodata_service_config(request):
    for s in _load_service_yield_on_func(request):
        yield s


@pytest.fixture(
    scope="function",
    params=[
        {
            "func": get_map_sddraft,
            "paths": [(MAP_SDDRAFT_FILE_PATH, MAP_SDDRAFT_FILE_PATH_COPY)]
        },
        {
            "func":
            get_map_service,
            "paths": [
                (MAP_MAIN_JSON_FILE_PATH, MAP_MAIN_JSON_FILE_PATH_COPY),
                (MAP_INFO_JSON_FILE_PATH, MAP_INFO_JSON_FILE_PATH_COPY)
            ]
        }, {
            "func": get_image_sddraft,
            "paths": [(IMAGE_SDDRAFT_FILE_PATH, IMAGE_SDDRAFT_FILE_PATH_COPY)]
        },
        {
            "func":
            get_image_service,
            "paths": [
                (IMAGE_MAIN_JSON_FILE_PATH, IMAGE_MAIN_JSON_FILE_PATH_COPY),
                (IMAGE_INFO_JSON_FILE_PATH, IMAGE_INFO_JSON_FILE_PATH_COPY)
            ]
        }
    ]
)
def map_and_image_service_config(request):
    for s in _load_service_yield_on_func(request):
        yield s


@pytest.fixture(
    scope="function",
    params=[
        {
            "func": get_image_sddraft,
            "paths": [(IMAGE_SDDRAFT_FILE_PATH, IMAGE_SDDRAFT_FILE_PATH_COPY)]
        },
        {
            "func":
            get_image_service,
            "paths": [
                (IMAGE_MAIN_JSON_FILE_PATH, IMAGE_MAIN_JSON_FILE_PATH_COPY),
                (IMAGE_INFO_JSON_FILE_PATH, IMAGE_INFO_JSON_FILE_PATH_COPY)
            ]
        }
    ]
)
def image_service_config(request):
    for s in _load_service_yield_on_func(request):
        yield s


@pytest.fixture(
    scope="function",
    params=[
        {
            "func": get_vector_tile_sddraft,
            "paths": [(VECTOR_TILE_SDDRAFT_FILE_PATH, VECTOR_TILE_SDDRAFT_FILE_PATH_COPY)]
        },
        {
            "func":
            get_vector_tile_service,
            "paths": [
                (VECTOR_TILE_MAIN_JSON_FILE_PATH, VECTOR_TILE_MAIN_JSON_FILE_PATH_COPY),
                (VECTOR_TILE_INFO_JSON_FILE_PATH, VECTOR_TILE_INFO_JSON_FILE_PATH_COPY)
            ]
        }
    ]
)
def vector_tile_service_config(request):
    for s in _load_service_yield_on_func(request):
        yield s


def silentremove(filename):
    try:
        os.remove(filename)
    except OSError as e:  # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT:  # errno.ENOENT = no such file or directory
            raise  # re-raise exception if a different error occurred


def _load_service_yield_on_func(request):
    for path in request.param["paths"]:
        shutil.copyfile(path[0], path[1])

    with ExitStack() as stack:
        files = [stack.enter_context(open(path[1], mode="rb+")) for path in request.param["paths"]]
        yield request.param["func"](*files)

    for path in request.param["paths"]:
        os.remove(path[1])