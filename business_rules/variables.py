import inspect
from functools import wraps
from .utils import fn_name_to_pretty_label
from .operators import (BaseType,
                        NumericType,
                        StringType,
                        BooleanType,
                        SelectType,
                        SelectMultipleType)

class BaseVariables(object):
    """ Classes that hold a collection of variables to use with the rules
    engine should inherit from this.
    """
    @classmethod
    def get_all_variables(cls):
        pass


def rule_variable(field_type, label=None, options=None):
    """ Decorator to make a function into a rule variable
    """
    def wrapper(func):
        pass
    pass


def _rule_variable_wrapper(field_type, label):
    pass

def numeric_rule_variable(label=None):
    pass

def string_rule_variable(label=None):
    pass

def boolean_rule_variable(label=None):
    pass

def select_rule_variable(label=None, options=None):
    pass

def select_multiple_rule_variable(label=None, options=None):
    pass
