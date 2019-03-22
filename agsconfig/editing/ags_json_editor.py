# coding=utf-8
"""This module contains a JSON-editor for editing ArcGIS Server REST Admin configuration."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

import json

import jsonpath_ng as jp
from jsonpath_ng.ext import parse

from .editor_base import EditorBase


class AgsJsonEditor(EditorBase):
    """
    The AgsJsonEditor class is a JSON editor for editing ArcGIS Server REST Admin JSON documents.

    This class is not intended to be instanstiated indepdently, and should be created via factory functions at the root
    of the module.

    Args:
        main_json_file (file): A file or file-like object representing the main JSON document.
        item_info_json_file (file): A file or file-like object representing item-info JSON document.
    """

    def __init__(self, main_json_file, item_info_json_file):
        self._main_file = main_json_file
        self._item_info_file = item_info_json_file
        self._main = json.load(main_json_file)
        self._item_info = json.load(item_info_json_file)

        self._document_map = {"main": self._main, "itemInfo": self._item_info}

        super().__init__("agsJson")

    def save(self):
        self._overwrite_file(self._main_file, self._main)
        self._overwrite_file(self._item_info_file, self._item_info)

    def _get_value(self, path_info):
        document = self._document_map.get(path_info["document"])

        # find value in document based on path
        return parse(path_info["path"]).find(document)[0].value

    def _set_value(self, value, path_info):
        document = self._document_map.get(path_info["document"])
        parse(path_info["path"]).update(document, value)

    @staticmethod
    def _overwrite_file(file_obj, obj_to_write):
        file_obj.seek(0)
        file_obj.truncate()
        file_obj.write(json.dumps(obj_to_write, indent=4).encode("utf-8"))
