import unittest

from dt.dgraph.dql.dql_variable_set import DQLVariableSet
from dt.dgraph.graphql.value import Value
from dt.dgraph.graphql.variable import Variable

TEST_VARIABLE_NAME = "TEST_VARIABLE_NAME"
TEST_VARIABLE_NAME_2 = "TEST_VARIABLE_NAME_2"
TEST_VARIABLE_NAME_3 = "TEST_VARIABLE_NAME_3"
TEST_VARIABLE_NAME_4 = "TEST_VARIABLE_NAME_4"
TEST_VARIABLE_TYPE = "TEST_VARIABLE_TYPE"
TEST_VARIABLE_VALUE = "TEST_VARIABLE_VALUE"
TEST_VARIABLE_DEFAULT_VALUE = "TEST_VARIABLE_DEFAULT_VALUE"
TEST_VARIABLE_DICT = {
    "$TEST_VARIABLE_NAME": "TEST_VARIABLE_VALUE",
    "$TEST_VARIABLE_NAME_2": "TEST_VARIABLE_DEFAULT_VALUE",
    "$TEST_VARIABLE_NAME_3": None,
    "$TEST_VARIABLE_NAME_4": "TEST_VARIABLE_VALUE",
}


class DQLVariableSetTestCase(unittest.TestCase):
    def test_get_value_dict(self) -> None:
        variable = Variable(name=TEST_VARIABLE_NAME,
                            variable_type=TEST_VARIABLE_TYPE,
                            value=Value(TEST_VARIABLE_VALUE))

        variable2 = Variable(name=TEST_VARIABLE_NAME_2,
                             variable_type=TEST_VARIABLE_TYPE,
                             default_value=Value(TEST_VARIABLE_DEFAULT_VALUE))
        variable3 = Variable(name=TEST_VARIABLE_NAME_3,
                             variable_type=TEST_VARIABLE_TYPE)
        variable4 = Variable(name=TEST_VARIABLE_NAME_4,
                             variable_type=TEST_VARIABLE_TYPE,
                             value=Value(TEST_VARIABLE_VALUE),
                             default_value=Value(TEST_VARIABLE_DEFAULT_VALUE))
        variable_set = DQLVariableSet(variable, variable2, variable3, variable4)
        expected = TEST_VARIABLE_DICT
        actual = variable_set.get_value_dict()
        self.assertEqual(actual, expected)
