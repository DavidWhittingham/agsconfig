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


OGC_GETTER_TEST_CASES = [ #yapf:disable
    ('abstract', "This is the abstract.", None),
    ('access_constraints', "There are no access constraints.", None),
    ('address', "123 Fake St.", None),
    ('administrative_area', "Queensland", None),
    ('city', "Brisbane", None),
    ('country', "Australia", None),
    ('email', "mail@mail.com", None),
    ('facsimile', "+987654321", None),
    ('fees', "There are no fees.", None),
    ('individual_name', "John Doe", None),
    ('keywords', "These Are Keywords", None),
    ('phone', "+123456789", None),
    ('position_name', "Officer", None),
    ('postal_code', "ABC123", None),
    ('provider_name', "GIS Pty. Ltd.", None),
    ('title', "Test Service", None)
] #yapf:enable

OGC_SETTER_TEST_CASES = [ #yapf:disable
    ('abstract', 'abstract', 'abstract', None),
    ('access_constraints', 'ac', 'ac', None),
    ('address', "456 Real Lane", "456 Real Lane", None),
    ('administrative_area', 'admin', 'admin', None),
    ('city', 'city', 'city', None),
    ('country', 'country', 'country', None),
    ('email', 'email', 'email', None),
    ('facsimile', 'fax', 'fax', None),
    ('fees', '$10/hr', '$10/hr', None),
    ('individual_name', 'Jane Doe', 'Jane Doe', None),
    ('keywords', 'kw', 'kw', None),
    ('phone', 'phone', 'phone', None),
    ('position_name', 'Director', 'Director', None),
    ('postal_code', 'postcode', 'postcode', None),
    ('provider_name', "GIS Inc.", "GIS Inc.", None),
    ('title', 'Prod Service', 'Prod Service', None)
] #yapf:enable