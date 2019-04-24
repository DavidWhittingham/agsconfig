# coding=utf-8
"""This module contains the ModelBase base class for all models in agsconfig."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

from abc import ABCMeta

ATTR_MISSING = object()

class ModelBase(object):
    __metaclass__ = ABCMeta

    def __getitem__(self, item):
        return getattr(self, item)

    def __setattr__(self, name, value):
        """
        Prevents setting of unknown attributes.

        This helps eliminate a whole class of errors in testing.
        """

        a = getattr(self, name, ATTR_MISSING)
        if a is not ATTR_MISSING:
            object.__setattr__(self, name, value)
        else:
            raise TypeError('Cannot set name {0} on object of type {1}'.format(name, self.__class__.__name__))