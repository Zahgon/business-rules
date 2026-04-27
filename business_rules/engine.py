from .fields import FIELD_NO_INPUT

def run_all(rule_list,
            defined_variables,
            defined_actions,
            stop_on_first_trigger=False):

    pass

def run(rule, defined_variables, defined_actions):
    pass


def check_conditions_recursively(conditions, defined_variables):
    pass

def check_condition(condition, defined_variables):
    """ Checks a single rule condition - the condition will be made up of
    variables, values, and the comparison operator. The defined_variables
    object must have a variable defined for any variables in this condition.
    """
    pass

def _get_variable_value(defined_variables, name):
    """ Call the function provided on the defined_variables object with the
    given name (raise exception if that doesn't exist) and casts it to the
    specified type.

    Returns an instance of operators.BaseType
    """
    def fallback(*args, **kwargs):
        pass
    pass

def _do_operator_comparison(operator_type, operator_name, comparison_value):
    """ Finds the method on the given operator_type and compares it to the
    given comparison_value.

    operator_type should be an instance of operators.BaseType
    comparison_value is whatever python type to compare to
    returns a bool
    """
    def fallback(*args, **kwargs):
        pass
    pass


def do_actions(actions, defined_actions):
    def fallback(*args, **kwargs):
        pass
    pass
