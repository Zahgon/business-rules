import inspect
import re
from functools import wraps
from six import string_types, integer_types

from .fields import (FIELD_TEXT, FIELD_NUMERIC, FIELD_NO_INPUT,
                     FIELD_SELECT, FIELD_SELECT_MULTIPLE)
from .utils import fn_name_to_pretty_label, float_to_decimal
from decimal import Decimal, Inexact, Context

class BaseType(object):
    def __init__(self, value):
        self.value = self._assert_valid_value_and_cast(value)

    def _assert_valid_value_and_cast(self, value):
        pass

    @classmethod
    def get_all_operators(cls):
        pass


def export_type(cls):
    """ Decorator to expose the given class to business_rules.export_rule_data. """
    pass


def type_operator(input_type, label=None,
                  assert_type_for_arguments=True):
    """ Decorator to make a function into a type operator.

    - assert_type_for_arguments - if True this patches the operator function
      so that arguments passed to it will have _assert_valid_value_and_cast
      called on them to make type errors explicit.
    """
    def wrapper(func):
        @wraps(func)
        def inner(self, *args, **kwargs):
            pass
        pass
    pass


@export_type
class StringType(BaseType):

    name = "string"

    def _assert_valid_value_and_cast(self, value):
        pass

    @type_operator(FIELD_TEXT)
    def equal_to(self, other_string):
        pass

    @type_operator(FIELD_TEXT, label="Equal To (case insensitive)")
    def equal_to_case_insensitive(self, other_string):
        pass

    @type_operator(FIELD_TEXT)
    def starts_with(self, other_string):
        pass

    @type_operator(FIELD_TEXT)
    def ends_with(self, other_string):
        pass

    @type_operator(FIELD_TEXT)
    def contains(self, other_string):
        pass

    @type_operator(FIELD_TEXT)
    def matches_regex(self, regex):
        pass

    @type_operator(FIELD_NO_INPUT)
    def non_empty(self):
        pass


@export_type
class NumericType(BaseType):
    EPSILON = Decimal('0.000001')

    name = "numeric"

    @staticmethod
    def _assert_valid_value_and_cast(value):
        pass

    @type_operator(FIELD_NUMERIC)
    def equal_to(self, other_numeric):
        pass

    @type_operator(FIELD_NUMERIC)
    def greater_than(self, other_numeric):
        pass

    @type_operator(FIELD_NUMERIC)
    def greater_than_or_equal_to(self, other_numeric):
        pass

    @type_operator(FIELD_NUMERIC)
    def less_than(self, other_numeric):
        pass

    @type_operator(FIELD_NUMERIC)
    def less_than_or_equal_to(self, other_numeric):
        pass


@export_type
class BooleanType(BaseType):

    name = "boolean"

    def _assert_valid_value_and_cast(self, value):
        pass

    @type_operator(FIELD_NO_INPUT)
    def is_true(self):
        pass

    @type_operator(FIELD_NO_INPUT)
    def is_false(self):
        pass

@export_type
class SelectType(BaseType):

    name = "select"

    def _assert_valid_value_and_cast(self, value):
        pass

    @staticmethod
    def _case_insensitive_equal_to(value_from_list, other_value):
        pass

    @type_operator(FIELD_SELECT, assert_type_for_arguments=False)
    def contains(self, other_value):
        pass

    @type_operator(FIELD_SELECT, assert_type_for_arguments=False)
    def does_not_contain(self, other_value):
        pass


@export_type
class SelectMultipleType(BaseType):

    name = "select_multiple"

    def _assert_valid_value_and_cast(self, value):
        pass

    @type_operator(FIELD_SELECT_MULTIPLE)
    def contains_all(self, other_value):
        pass

    @type_operator(FIELD_SELECT_MULTIPLE)
    def is_contained_by(self, other_value):
        pass

    @type_operator(FIELD_SELECT_MULTIPLE)
    def shares_at_least_one_element_with(self, other_value):
        pass

    @type_operator(FIELD_SELECT_MULTIPLE)
    def shares_exactly_one_element_with(self, other_value):
        pass

    @type_operator(FIELD_SELECT_MULTIPLE)
    def shares_no_elements_with(self, other_value):
        pass
