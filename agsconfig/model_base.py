# coding=utf-8
"""This module contains the ModelBase base class for all models in agsconfig."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
from future.utils import raise_
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

import sys as _sys

from abc import ABCMeta as _ABCMeta

ATTR_MISSING = object()


class ModelBase(object):
    __metaclass__ = _ABCMeta

    def __getitem__(self, item):
        return getattr(self, item)

    def __setattr__(self, name, value):
        """
        Prevents setting of unknown attributes.

        This helps eliminate a whole class of errors in testing.
        """

        if getattr(self, name, ATTR_MISSING) is ATTR_MISSING:
            raise AttributeError('Cannot set name {0} on object of type {1}'.format(name, self.__class__.__name__))

        object.__setattr__(self, name, value)

    def _set_props_from_dict(self, prop_dict, ignore_not_implemented=False):
        """Method for setting properties from a dictionary where keys match property names.
        Can be overridden by sub-classes.
        """

        type_self = type(self)

        for key, value in prop_dict.items():

            # check if property exists on this class at all
            if not hasattr(type_self, key):
                # property doesn't exist
                if ignore_not_implemented:
                    continue
                else:
                    raise AttributeError("The '{}' attribute doesn't exist on '{}'.".format(key, type_self.__name__))

            # attribute may not be implemented for this format, try getting it to eliminate that possibility
            try:
                getattr(self, key)
            except NotImplementedError:
                # Getting or setting this attribute isn't implemented on this format
                t, v, tb = _sys.exc_info()
                if ignore_not_implemented:
                    self._logger.warning(
                        "Tried to set the '%s' property to '%s', but this is not supported on the supplied configuration format.",
                        key, value
                    )
                    continue
                else:
                    raise_(t, v, tb)

            # attribute exists, attempt to set it
            try:
                # try to set the keyed attribute to the provided value
                setattr(self, key, value)
            except NotImplementedError:
                # Setting this attribute isn't implemented on this format
                t, v, tb = _sys.exc_info()
                if ignore_not_implemented:
                    self._logger.warning(
                        "Tried to set the '%s' property to '%s', but this is not supported on the supplied configuration format.",
                        key, value
                    )
                    continue
                else:
                    raise_(t, v, tb)
            except AttributeError:
                # Attribute can't be set, but we know it exists and is implemented, probably an extension
                # Get the attribute and try and set properties on it
                getattr(self, key)._set_props_from_dict(value, ignore_not_implemented)
            except Exception:
                t, v, tb = _sys.exc_info()
                self._logger.error("An unknown exception was thrown setting the '%s' property.", key)
                raise_(t, v, tb)