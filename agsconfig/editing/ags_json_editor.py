# coding=utf-8
"""This module contains a JSON-editor for editing ArcGIS Server REST Admin configuration."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

import copy
import json
import re

import jsonpath_ng as jp
from jsonpath_ng.ext import parse

from .editor_base import EditorBase


class AgsJsonEditor(EditorBase):
    """
    The AgsJsonEditor class is a JSON editor for editing ArcGIS Server REST Admin JSON documents.

    This class is not intended to be instantiated independently, and should be created via factory functions at the root
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

    def export(self):
        return (copy.deepcopy(self._main), copy.deepcopy(self._item_info))

    def save(self):
        self._overwrite_file(self._main_file, self._main)
        self._overwrite_file(self._item_info_file, self._item_info)

    def save_a_copy(self, main_json_output_path, item_info_output_path):
        self._save_json_to_file(self._main, main_json_output_path)
        self._save_json_to_file(self._item_info, item_info_output_path)

    def _create_node(self, document, path, path_info, obj):
        """Creates a new node on the JSON document."""

        # get parent element path
        parent_node_path = re.match(r"(.*)(?![^\[]*\])(?=[\[\.])", path).groups()[0]
        parent_path_info = self._resolve_lambda(path_info, obj, "parent")["parent"]
        self._create_node_structure(document, parent_node_path, parent_path_info, obj)

    def _create_node_structure(self, document, path, path_info, obj):
        # attempt to find the provided path
        current_node = parse(path).find(document)

        if not current_node:
            # must recurse up a level
            if not "parent" in path_info:
                # can't go up a level
                raise Exception("Can't create JSON structure, no parent information at this level: {}".format(path))

            # calculate the path for the parent of the current path by capturing up until the end of the previous level of the JSON structure
            current_node_parent_path = re.match(r"(.*)(?![^\[]*\])(?=[\[\.])", path).groups()[0]

            parent_path_info = self._resolve_lambda(path_info, obj, "parent")["parent"]
            self._create_node_structure(document, current_node_parent_path, parent_path_info, obj)

            # get current element again, should exist now
            current_node = parse(path).find(document)

            if not current_node:
                raise Exception("Failed to create JSON node at path: {}".format(path))

        current_node = current_node[0].value

        if "children" in path_info:
            for child_path_info in path_info["children"]:
                self._create_child_nodes(current_node, child_path_info, obj)

    def _create_child_nodes(self, parent_node, path_info, obj):
        """Recursively creates child nodes for a parent node in a JSON document."""

        new_value = self._resolve_lambda(path_info, obj, "value")["value"] if "value" in path_info else None

        if "key" in path_info:
            # value is being inserted into a dictionary
            # resolve a possible lambda on the "key" name for a property
            path_info = self._resolve_lambda(path_info, obj, "key")
            parent_node[path_info["key"]] = new_value
        else:
            # value is being appended to a list
            parent_node.append(new_value)

        if "children" in path_info:
            if new_value is None:
                new_value = {}

            for child in path_info["children"]:
                self._create_child_nodes(obj, new_value, child)

    def _get_value(self, path_info):
        document = self._document_map.get(path_info["document"])

        # find value in document based on path
        values = parse(path_info["path"]).find(document)

        if not values:
            return None

        # special case, don't convert strings starting with a "+", probably a phone number
        try:
            if values[0].value.startswith("+"):
                return values[0].value
        except AttributeError:
            pass

        # Return pythonic things for known types
        try:
            val = float(values[0].value)
            return int(val) if val.is_integer() else val
        except (ValueError, TypeError):
            pass

        try:
            if values[0].value.upper() == "TRUE":
                return True
        except AttributeError:
            pass

        try:
            if values[0].value.upper() == "FALSE":
                return False
        except AttributeError:
            pass

        try:
            if len(values[0].value.split(',')) > 1:
                return values[0].value.split(',')
        except AttributeError:
            pass

        return values[0].value

    def _set_value(self, value, path_info, obj):
        document = self._document_map.get(path_info["document"])

        # check if node exists
        if not parse(path_info["path"]).find(document):
            # node does not exist, create
            self._create_node(document, path_info["path"], path_info, obj)

        parse(path_info["path"]).update(document, value)

    @staticmethod
    def _overwrite_file(file_obj, obj_to_write):
        file_obj.seek(0)
        file_obj.truncate()
        file_obj.write(json.dumps(obj_to_write, indent=4).encode("utf-8"))

    @staticmethod
    def _save_json_to_file(input_json, file_path):
        with open(file_path, "w", encoding="utf-8") as fp:
            fp.write(json.dumps(input_json, indent=4, separators=(',', ': '), sort_keys=True, ensure_ascii=False))
