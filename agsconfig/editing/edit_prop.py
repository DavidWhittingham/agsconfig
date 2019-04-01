# coding=utf-8
"""This module contains the EditorProperty descriptor that difers object editing to an editor class."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()

# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position


class EditorProperty(object):
    """The EditorProperty class is a descriptor that defers getting and setting to editing objects.

    Args:
      meta (obj): Property metadata, by format key.

    """

    name = None

    def __init__(self, meta):
        self.meta = meta

    def __get__(self, obj, type=None):
        if obj is None:
            # this is used to get the property metadata via the type, if needed
            return self

        value = obj._editor.get_value(self.meta, obj)

        return value

    def __set__(self, obj, value):
        # perform any constraint checks that are specified before setting the value
        if "constraints" in self.meta:
            constraints = self.meta["constraints"]

            if "default" in constraints and value is None:
                value = constraints["default"]

            if "notEmpty" in constraints:
                if value is None or not value or str(value).isspace():
                    raise ValueError("Value of property '{}' cannot be null or empty.".format(self.name_of(obj)))

            if constraints.get("float", False) is True and not value is None:
                value = float(value)

            if constraints.get("int", False) is True and not value is None:
                value = int(value)

            if "min" in constraints:
                min_value = constraints["min"]
                if value < min_value:
                    raise ValueError(
                        "Value of property '{}' cannot be less than '{}'.".format(self.name_of(obj), min_value)
                    )

            if "max" in constraints:
                max_value = constraints["max"]
                if value > max_value:
                    raise ValueError(
                        "Value of property '{}' cannot be greater than '{}'.".format(self.name_of(obj), max_value)
                    )

            if "func" in constraints:
                value = constraints["func"](obj, value)

        obj._editor.set_value(value, self.meta, obj)

    def __delete__(self, obj):
        raise AttributeError("You cannot delete the '{}' property.".format(self.name_of(obj)))

    def name_of(self, instance):
        """Gets the name of the property a descriptor is assigned to."""

        # retrieved cached name if it exists
        if self.name is not None:
            return self.name

        attributes = set()

        for cls in type(instance).__mro__:
            # add all attributes from the class into 'attributes'
            attributes |= {attr for attr in dir(cls) if not attr.startswith('__')}

        for attr in attributes:
            if getattr(type(instance), attr) is self:
                self.name = attr
                return self.name

        # This should never happen.
        raise ValueError("This EditorProperty is not assigned to a name on the given instance.")
