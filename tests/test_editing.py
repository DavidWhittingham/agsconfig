"""Tests for editing functionality."""
# Python 2/3 compatibility
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()

import pytest
from agsconfig.editing.sdd_editor import SDDraftEditor
from lxml import etree as ET

@pytest.mark.parametrize(
    ('element', 'value', 'exception'),
    [
        (ET.Element("root"), 2000, None),
        (ET.Element("root"), '2000', None),
        (ET.Element("root"), 1.36518, None),
        (ET.Element("root"), [ET.Element("elem")], None)
    ]
)
def test_set_element_value(element, value, exception):
    if exception is not None:
        with pytest.raises(exception):
            SDDraftEditor._set_element_value(element, value, True, True)
    else:
        SDDraftEditor._set_element_value(element, value, True, True)
        pass

