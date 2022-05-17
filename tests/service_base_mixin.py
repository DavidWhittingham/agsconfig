# coding=utf-8
"""This module contains shared tests for all models that implement the ServiceBase class."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

import datetime

import pytest

from .helpers import TRUEISH_TEST_PARAMS


def test_invalid_getter(service_config):
    with pytest.raises(AttributeError):
        assert getattr(service_config, "non_existent_attribute") == "non-existent value"


def test_invalid_setter(service_config):
    with pytest.raises(AttributeError):
        setattr(service_config, "non_existent_attribute", "can't assign a value here")


@pytest.mark.parametrize(
    ("access_information"), [
        ("This is a test description"),
        (
            "This is a much longer test description. It should still work\nIt includes line breaks. We'll see how they go."
        ), ("These long descriptions cannot contain commas."), ("")
    ]
)
def test_access_information(service_config, access_information):
    service_config.access_information = access_information
    assert service_config.access_information == access_information


@pytest.mark.parametrize(
    ("cluster_name", "expected"), [("Default", "Default"), ("NonDefaultCluster", "NonDefaultCluster")]
)
def test_cluster(service_config, cluster_name, expected):
    service_config.cluster = cluster_name
    assert service_config.cluster == expected


@pytest.mark.parametrize(
    ("credit_text", "expected"), [
        ("These are some credits", "These are some credits"),
        ("These are some unicode ©redits", "These are some unicode ©redits")
    ]
)
def test_credits(service_config, credit_text, expected):
    service_config.credits = credit_text
    assert service_config.credits == expected


@pytest.mark.parametrize(
    ("description"), [
        ("This is a test description"),
        (
            "This is a much longer test description. It should still work\nIt includes line breaks. We'll see how they go."
        ), ("")
    ]
)
def test_description(service_config, description):
    service_config.description = description
    assert service_config.description == description


@pytest.mark.parametrize(
    ("folder", "expected", "ex"), [("TestName", "TestName", None), ("", None, None), (None, None, None)]
)
def test_folder(service_config, folder, expected, ex):
    if ex is not None:
        with pytest.raises(ex):
            service_config.folder = folder
    else:
        service_config.folder = folder
        assert service_config.folder == expected


@pytest.mark.parametrize(("high_isolation", "expected"), TRUEISH_TEST_PARAMS)
def test_high_isolation(service_config, high_isolation, expected):
    service_config.high_isolation = high_isolation
    assert service_config.high_isolation == expected


@pytest.mark.parametrize(("timeout", "ex"), [(0, None), (100, None), (99999, None), (-10, ValueError)])
def test_idle_timeout(service_config, timeout, ex):
    if ex is not None:
        with pytest.raises(ex):
            service_config.idle_timeout = timeout
    else:
        service_config.idle_timeout = timeout
        assert service_config.idle_timeout == timeout


@pytest.mark.parametrize(("instances"), [(1), (2), (8)])
def test_instances_per_container(service_config, instances):
    service_config.instances_per_container = instances
    assert service_config.instances_per_container == instances


@pytest.mark.parametrize(
    ("min_number", "max_number", "exp_min", "exp_max", "ex"), [
        (0, -1, None, None, ValueError), (0, 0, None, None, ValueError), (0, 2, 0, 2, None), (1, 8, 1, 8, None),
        (5, 2, 2, 2, None)
    ]
)
def test_instances_counts(service_config, min_number, max_number, exp_min, exp_max, ex):
    if ex is not None:
        with pytest.raises(ex):
            service_config.min_instances = min_number
            service_config.max_instances = max_number
    else:
        service_config.min_instances = min_number
        service_config.max_instances = max_number
        assert service_config.min_instances == exp_min
        assert service_config.max_instances == exp_max


@pytest.mark.parametrize(("name", "ex"), [("TestName", None), ("", ValueError)])
def test_name(service_config, name, ex):
    if ex is not None:
        with pytest.raises(ex):
            service_config.name = name
    else:
        service_config.name = name
        assert service_config.name == name


@pytest.mark.parametrize(
    ("interval", "expected", "exception"),
    [(1, 1, None), (12, 12, None), (0, None, ValueError), (-10, None, ValueError), (None, 24, None)]
)
def test_recycle_interval(service_config, interval, expected, exception):
    if exception is not None:
        with pytest.raises(exception):
            service_config.recycle_interval = interval
    else:
        service_config.recycle_interval = interval
        assert service_config.recycle_interval == expected


@pytest.mark.parametrize(
    ("input", "expected", "ex"), [
        ("12:01", datetime.time(12, 1), None), (datetime.time(14, 35), datetime.time(14, 35), None),
        ("nonsense", None, ValueError)
    ]
)
def test_recycle_start_time(service_config, input, expected, ex):
    if ex is not None:
        with pytest.raises(ex):
            service_config.recycle_start_time = input
    else:
        service_config.recycle_start_time = input
        assert service_config.recycle_start_time == expected


@pytest.mark.parametrize(("replace", "expected"), TRUEISH_TEST_PARAMS)
def test_replace_existing(service_config, replace, expected):
    service_config.replace_existing = replace
    assert service_config.replace_existing == expected


@pytest.mark.parametrize(("summary"), [("A test summary"), ("A test summary.\nIt also has line breaks."), ("")])
def test_summary(service_config, summary):
    service_config.summary = summary
    assert service_config.summary == summary


@pytest.mark.parametrize(
    ("tags", "expected", "ex"), [
        (["a tag"], ["a tag"], None), ("a tag", None, ValueError), ([], [], None),
        (["Multiple", "Tags"], ["Multiple", "Tags"], None)
    ]
)
def test_tags(service_config, tags, expected, ex):
    if ex is not None:
        with pytest.raises(ex):
            service_config.tags = tags
    else:
        service_config.tags = tags
        assert set(service_config.tags) == set(expected)


@pytest.mark.parametrize(
    ("title", "ex"), [
        ("This is a title", None),
        ("This is a much longer title. It should still work\nIt includes line breaks. We'll see how they go.", None),
        ("", None)
    ]
)
def test_title(service_config, title, ex):
    if ex is not None:
        with pytest.raises(ex):
            service_config.title = title
    else:
        service_config.title = title
        assert service_config.title == title


@pytest.mark.parametrize(("timeout", "ex"), [(0, None), (100, None), (99999, None), (-10, ValueError)])
def test_usage_timeout(service_config, timeout, ex):
    if ex is not None:
        with pytest.raises(ex):
            service_config.usage_timeout = timeout
    else:
        service_config.usage_timeout = timeout
        assert service_config.usage_timeout == timeout


@pytest.mark.parametrize(("timeout", "ex"), [(0, None), (100, None), (99999, None), (-10, ValueError)])
def test_wait_timeout(service_config, timeout, ex):
    if ex is not None:
        with pytest.raises(ex):
            service_config.wait_timeout = timeout
    else:
        service_config.wait_timeout = timeout
        assert service_config.wait_timeout == timeout
