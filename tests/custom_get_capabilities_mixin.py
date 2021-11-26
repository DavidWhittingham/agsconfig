# coding=utf-8
"""Tests for ogc metadata attributes. """

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

CUSTOM_GET_CAPABILITIES_GETTER_TEST_CASES = [ #yapf:disable
    ('custom_get_capabilities', False, None),
    ('path_to_custom_get_capabilities_files', None, None)
] #yapf:enable

CUSTOM_GET_CAPABILITIES_SETTER_TEST_CASES = [ #yapf:disable
    ('custom_get_capabilities', False, False, None),
    ('custom_get_capabilities', True, True, None),
    ('custom_get_capabilities', 'x', None, ValueError),
    ('path_to_custom_get_capabilities_files', 'a:/path', 'a:/path', None)
] #yapf:enable