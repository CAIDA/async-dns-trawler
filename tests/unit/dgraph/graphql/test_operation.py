import unittest

from dt.dgraph.constants.graphql_operation import GraphQLOperation
from dt.dgraph.graphql.field import Field
from dt.dgraph.graphql.fragment_spread import FragmentSpread
from dt.dgraph.graphql.operation import Operation
from dt.dgraph.graphql.selection_set import SelectionSet
from dt.dgraph.graphql.value import Value
from dt.dgraph.graphql.variable import Variable
from dt.dgraph.graphql.variable_set import VariableSet

TEST_FIELD_NAME = "TEST_FIELD_NAME"
TEST_FRAGMENT_NAME = "TEST_FRAGMENT_NAME"
TEST_VARIABLE_NAME = "TEST_VARIABLE_NAME"
TEST_VARIABLE_NAME_2 = "TEST_VARIABLE_NAME_2"
TEST_VARIABLE_TYPE = "TEST_VARIABLE_TYPE"
TEST_DEFAULT_VALUE = "TEST_DEFAULT_VALUE"
TEST_OPERATION_TYPE = GraphQLOperation.QUERY
TEST_OPERATION_TYPE_2 = GraphQLOperation.MUTATION
TEST_OPERATION_NAME = "TEST_OPERATION_NAME"
TEST_OPERATION_NAME_2 = "TEST_OPERATION_NAME_2"
TEST_GRAPHQL_STR = "query {\n" + \
                   "...TEST_FRAGMENT_NAME\n" + \
                   "TEST_FIELD_NAME\n" + \
                   "}"
TEST_GRAPHQL_STR_2 = "query TEST_OPERATION_NAME {\n" + \
    "...TEST_FRAGMENT_NAME\n" + \
    "TEST_FIELD_NAME\n" + \
    "}"
TEST_GRAPHQL_STR_3 = \
    "query ($TEST_VARIABLE_NAME: TEST_VARIABLE_TYPE = TEST_DEFAULT_VALUE," + \
    " $TEST_VARIABLE_NAME_2: TEST_VARIABLE_TYPE) {\n" + \
    "...TEST_FRAGMENT_NAME\n" + \
    "TEST_FIELD_NAME\n" + \
    "}"
TEST_GRAPHQL_STR_4 = \
    "query TEST_OPERATION_NAME($TEST_VARIABLE_NAME: " + \
    "TEST_VARIABLE_TYPE = TEST_DEFAULT_VALUE," + \
    " $TEST_VARIABLE_NAME_2: TEST_VARIABLE_TYPE) {\n" + \
    "...TEST_FRAGMENT_NAME\n" + \
    "TEST_FIELD_NAME\n" + \
    "}"


class OperationTestCase(unittest.TestCase):
    def test_constructor(self) -> None:
        variables = VariableSet(
            Variable(name=TEST_VARIABLE_NAME,
                     variable_type=TEST_VARIABLE_TYPE)
        )
        selection_set = SelectionSet(Field(name=TEST_FIELD_NAME))
        operation = Operation(operation_type=TEST_OPERATION_TYPE,
                              selection_set=selection_set,
                              name=TEST_OPERATION_NAME,
                              variables=variables)

        self.assertEqual(operation.operation_type, TEST_OPERATION_TYPE)
        self.assertEqual(operation.selection_set, selection_set)
        self.assertEqual(operation.name, TEST_OPERATION_NAME)
        self.assertEqual(operation.variables, variables)

    def test_eq_equal(self) -> None:
        variables = VariableSet(
            Variable(name=TEST_VARIABLE_NAME,
                     variable_type=TEST_VARIABLE_TYPE)
        )
        selection_set = SelectionSet(Field(name=TEST_FIELD_NAME))
        operation = Operation(operation_type=TEST_OPERATION_TYPE,
                              selection_set=selection_set,
                              name=TEST_OPERATION_NAME,
                              variables=variables)
        operation2 = Operation(operation_type=TEST_OPERATION_TYPE,
                               selection_set=selection_set,
                               name=TEST_OPERATION_NAME,
                               variables=variables)
        self.assertEqual(operation, operation2)

    def test_eq_not_equal_different_operation_type(self) -> None:
        variables = VariableSet(
            Variable(name=TEST_VARIABLE_NAME,
                     variable_type=TEST_VARIABLE_TYPE)
        )
        selection_set = SelectionSet(Field(name=TEST_FIELD_NAME))
        operation = Operation(operation_type=TEST_OPERATION_TYPE,
                              selection_set=selection_set,
                              name=TEST_OPERATION_NAME,
                              variables=variables)
        operation2 = Operation(operation_type=TEST_OPERATION_TYPE_2,
                               selection_set=selection_set,
                               name=TEST_OPERATION_NAME,
                               variables=variables)
        self.assertNotEqual(operation, operation2)

    def test_eq_not_equal_different_name(self) -> None:
        variables = VariableSet(
            Variable(name=TEST_VARIABLE_NAME,
                     variable_type=TEST_VARIABLE_TYPE)
        )
        selection_set = SelectionSet(Field(name=TEST_FIELD_NAME))
        operation = Operation(operation_type=TEST_OPERATION_TYPE,
                              name=TEST_OPERATION_NAME,
                              selection_set=selection_set,
                              variables=variables)
        operation2 = Operation(operation_type=TEST_OPERATION_TYPE,
                               name=TEST_OPERATION_NAME_2,
                               selection_set=selection_set,
                               variables=variables)
        self.assertNotEqual(operation, operation2)

    def test_eq_not_equal_different_selection_set(self) -> None:
        selection_set = SelectionSet(Field(name=TEST_FIELD_NAME))
        selection_set2 = SelectionSet(FragmentSpread(TEST_FRAGMENT_NAME))
        variables = VariableSet(
            Variable(name=TEST_VARIABLE_NAME,
                     variable_type=TEST_VARIABLE_TYPE)
        )
        selection_set = SelectionSet(Field(name=TEST_FIELD_NAME))
        operation = Operation(operation_type=TEST_OPERATION_TYPE,
                              name=TEST_OPERATION_NAME,
                              selection_set=selection_set,
                              variables=variables)
        operation2 = Operation(operation_type=TEST_OPERATION_TYPE,
                               name=TEST_OPERATION_NAME,
                               selection_set=selection_set2,
                               variables=variables)
        self.assertNotEqual(operation, operation2)

    def test_eq_not_equal_different_variables(self) -> None:
        variables = VariableSet(
            Variable(name=TEST_VARIABLE_NAME,
                     variable_type=TEST_VARIABLE_TYPE)
        )
        variables2 = VariableSet(
            Variable(name=TEST_VARIABLE_NAME_2,
                     variable_type=TEST_VARIABLE_TYPE)
        )
        selection_set = SelectionSet(Field(name=TEST_FIELD_NAME))
        operation = Operation(operation_type=TEST_OPERATION_TYPE,
                              name=TEST_OPERATION_NAME,
                              selection_set=selection_set,
                              variables=variables)
        operation2 = Operation(operation_type=TEST_OPERATION_TYPE,
                               name=TEST_OPERATION_NAME,
                               selection_set=selection_set,
                               variables=variables2)
        self.assertNotEqual(operation, operation2)

    def test_eq_not_equal_different_class(self) -> None:
        selection_set = SelectionSet(Field(name=TEST_FIELD_NAME))
        operation = Operation(operation_type=TEST_OPERATION_TYPE,
                              name=TEST_OPERATION_NAME,
                              selection_set=selection_set)
        operation2 = object()
        self.assertNotEqual(operation, operation2)

    def test_hash_equal(self) -> None:
        selection_set = SelectionSet(Field(name=TEST_FIELD_NAME))
        operation = Operation(operation_type=TEST_OPERATION_TYPE,
                              name=TEST_OPERATION_NAME,
                              selection_set=selection_set)
        operation2 = Operation(operation_type=TEST_OPERATION_TYPE,
                               name=TEST_OPERATION_NAME,
                               selection_set=selection_set)
        self.assertEqual(hash(operation), hash(operation2))

    def test_hash_equal_with_variables(self) -> None:
        variables = VariableSet(
            Variable(name=TEST_VARIABLE_NAME,
                     variable_type=TEST_VARIABLE_TYPE)
        )
        selection_set = SelectionSet(Field(name=TEST_FIELD_NAME))
        operation = Operation(operation_type=TEST_OPERATION_TYPE,
                              name=TEST_OPERATION_NAME,
                              selection_set=selection_set,
                              variables=variables)
        operation2 = Operation(operation_type=TEST_OPERATION_TYPE,
                               name=TEST_OPERATION_NAME,
                               selection_set=selection_set,
                               variables=variables)
        self.assertEqual(hash(operation), hash(operation2))

    def test_hash_not_equal(self) -> None:
        selection_set = SelectionSet(Field(name=TEST_FIELD_NAME))
        operation = Operation(operation_type=TEST_OPERATION_TYPE,
                              name=TEST_OPERATION_NAME,
                              selection_set=selection_set)
        operation2 = Operation(operation_type=TEST_OPERATION_TYPE_2,
                               name=TEST_OPERATION_NAME,
                               selection_set=selection_set)
        self.assertNotEqual(hash(operation), hash(operation2))

    def test_to_graphql(self) -> None:
        selection_set = SelectionSet(
            Field(name=TEST_FIELD_NAME),
            FragmentSpread(TEST_FRAGMENT_NAME)
        )
        operation = Operation(operation_type=TEST_OPERATION_TYPE,
                              selection_set=selection_set)
        expected = TEST_GRAPHQL_STR
        actual = operation.to_graphql()
        self.assertEqual(actual, expected)

    def test_to_graphql_with_name(self) -> None:
        selection_set = SelectionSet(
            Field(name=TEST_FIELD_NAME),
            FragmentSpread(TEST_FRAGMENT_NAME)
        )
        operation = Operation(operation_type=TEST_OPERATION_TYPE,
                              name=TEST_OPERATION_NAME,
                              selection_set=selection_set)
        expected = TEST_GRAPHQL_STR_2
        actual = operation.to_graphql()
        self.assertEqual(actual, expected)

    def test_to_graphql_with_variables(self) -> None:
        default_value = Value(TEST_DEFAULT_VALUE)
        variables = VariableSet(
            Variable(name=TEST_VARIABLE_NAME,
                     variable_type=TEST_VARIABLE_TYPE,
                     default_value=default_value),
            Variable(name=TEST_VARIABLE_NAME_2, variable_type=TEST_VARIABLE_TYPE)
        )
        selection_set = SelectionSet(
            Field(name=TEST_FIELD_NAME),
            FragmentSpread(TEST_FRAGMENT_NAME)
        )
        operation = Operation(operation_type=TEST_OPERATION_TYPE,
                              variables=variables,
                              selection_set=selection_set)
        expected = TEST_GRAPHQL_STR_3
        actual = operation.to_graphql()
        self.assertEqual(actual, expected)

    def test_to_graphql_full(self) -> None:
        default_value = Value(TEST_DEFAULT_VALUE)
        variables = VariableSet(
            Variable(name=TEST_VARIABLE_NAME,
                     variable_type=TEST_VARIABLE_TYPE,
                     default_value=default_value),
            Variable(name=TEST_VARIABLE_NAME_2, variable_type=TEST_VARIABLE_TYPE)
        )
        selection_set = SelectionSet(
            Field(name=TEST_FIELD_NAME),
            FragmentSpread(TEST_FRAGMENT_NAME)
        )
        operation = Operation(operation_type=TEST_OPERATION_TYPE,
                              name=TEST_OPERATION_NAME,
                              variables=variables,
                              selection_set=selection_set)
        expected = TEST_GRAPHQL_STR_4
        actual = operation.to_graphql()
        self.assertEqual(actual, expected)
