import inspect

from . import fields
from .utils import fn_name_to_pretty_label


class BaseActions(object):
    """ Classes that hold a collection of actions to use with the rules
    engine should inherit from this.
    """
    @classmethod
    def get_all_actions(cls):
        pass

def _validate_action_parameters(func, params):
    """ Verifies that the parameters specified are actual parameters for the
    function `func`, and that the field types are FIELD_* types in fields.
    """
    pass

def rule_action(label=None, params=None):
    """ Decorator to make a function into a rule action
    """
    def wrapper(func):
        pass
    pass
