# Python 2/3 compatibility
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
from future.utils import viewitems
install_aliases()

import collections

from lxml import etree as ET

from .editor_base import EditorBase


def get_element_value(element, default=None):
    if isinstance(element, collections.Sequence):
        if len(element) == 0:
            return element
        return [get_element_value(v, default) for v in element]

    if element == None or element.text == None:
        return default
    if element.text.upper() == "TRUE":
        return True
    if element.text.upper() == "FALSE":
        return False

    try:
        return int(element.text)
    except ValueError:
        pass

    try:
        return float(element.text)
    except ValueError:
        pass

    # value seems to be a string, get it as a Py2/3 compatible string
    return str(element.text)


class SDDraftEditor(EditorBase):

    def __init__(self, xml_file):
        self._xml_file = xml_file
        self._xml_tree = self._load_xml(xml_file)

        super().__init__(
            "sddraft", {"listToElements": self._deserialize_elements_to_list},
            {"listToElements": self._serialize_list_to_elements}
        )

    def save(self):
        if self._xml_file.closed:
            self._xml_file = open(self._xml_file.name, "rb+")

        self._xml_file.seek(0)
        self._xml_file.truncate()

        # explictly write it out to file as binary UTF-8
        self._xml_file.write(ET.tostring(self._xml_tree.getroot(), encoding="utf-8", pretty_print=True))

    def save_a_copy(self, path):
        with open(path, "wb+") as file:
            file.write(ET.tostring(self._xml_tree.getroot(), encoding="utf-8", pretty_print=True))

    def _create_element(self, path_info):
        # get parent element
        parent_element = self._xml_tree.find(path_info["parentPath"])

        self._create_child_elements(parent_element, path_info)

        return self._xml_tree.find(path_info["path"])

    def _create_child_elements(self, parent_element, path_info):
        new_element = ET.SubElement(parent_element, path_info["tag"], path_info.get("attributes", {}))

        if "value" in path_info:
            self._set_element_value(new_element, path_info["value"])

        if "children" in path_info:
            for child in path_info["children"]:
                self._create_child_elements(new_element, child)

    def _get_value(self, path_info):
        element = self._xml_tree.find(path_info["path"])

        if element != None and len(element) > 0:
            # element has children, return as iterable
            return element.getchildren()

        return self._get_element_value(element)

    def _set_value(self, value, path_info):
        element = self._xml_tree.find(path_info["path"])

        if element is None:
            element = self._create_element(path_info)

        self._set_element_value(element, value)

    @staticmethod
    def _get_element_value(element, default=None):
        return get_element_value(element, default)

    @staticmethod
    def _deserialize_elements_to_list(value, conversion, obj):
        if value == None or len(value) == 0:
            return []

        return [get_element_value(e) for e in value]

    @staticmethod
    def _serialize_list_to_elements(value, conversion, obj):
        tag_name = conversion["tag"]
        attributes = conversion.get("attributes", {})

        elems = []
        for i in value:
            elem = ET.Element(tag_name, attributes)
            elem.text = i
            elems.append(elem)

        return elems

    @staticmethod
    def _set_element_value(element, value, set_xsi_type=False, set_xsi_nil=False):
        if value == None:
            element.text = None

            if set_xsi_nil:
                if "{http://www.w3.org/2001/XMLSchema-instance}type" in element.attrib:
                    del element.attrib["{http://www.w3.org/2001/XMLSchema-instance}type"]
                element.set("{http://www.w3.org/2001/XMLSchema-instance}nil", "true")
            return
        elif set_xsi_nil:
            if "{http://www.w3.org/2001/XMLSchema-instance}nil" in element.attrib:
                del element.attrib["{http://www.w3.org/2001/XMLSchema-instance}nil"]

        if isinstance(value, bool):
            element.text = "true" if value is True else "false"
            if set_xsi_type:
                # elementtree doesn't seem to support mapping schemas for values
                # Arc seems to consistently use the XS namespace, so it's not a problem right now
                element.set("{http://www.w3.org/2001/XMLSchema-instance}type", "xs:boolean")
            return
        if isinstance(value, int):
            element.text = str(repr(value))
            if set_xsi_type:
                element.set("{http://www.w3.org/2001/XMLSchema-instance}type", "xs:int")
            return
        if isinstance(value, float):
            element.text = str(repr(value))
            if set_xsi_type:
                element.set("{http://www.w3.org/2001/XMLSchema-instance}type", "xs:float")
            return
        if isinstance(value, str):
            element.text = value
            if set_xsi_type:
                element.set("{http://www.w3.org/2001/XMLSchema-instance}type", "xs:string")
            return
        if isinstance(value, list):
            # assume list of elements, remove all current and set
            for elem in element:
                element.remove(elem)
            for elem in value:
                element.append(elem)
            return
        raise ValueError("Element value cannot be set, unknown type.")

    def _load_xml(self, xml_file):
        """Parses an XML file whilst preserving custom namespaces, which ElementTree doesn't do out of the box"""

        # seek to start of XML file for reading
        xml_file.seek(0)

        # remove blank text in order to pretty-print later
        parser = ET.XMLParser(remove_blank_text=True)
        return ET.parse(xml_file, parser)
