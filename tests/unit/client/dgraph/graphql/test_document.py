import unittest

from dt.client.dgraph.constants.graphql_operation import GraphQLOperation
from dt.client.dgraph.graphql.document import Document
from dt.client.dgraph.graphql.field import Field
from dt.client.dgraph.graphql.fragment import Fragment
from dt.client.dgraph.graphql.operation import Operation
from dt.client.dgraph.graphql.selection_set import SelectionSet
from dt.client.dgraph.graphql.variable import Variable
from dt.client.dgraph.graphql.variable_set import VariableSet

TEST_OPERATION_TYPE = GraphQLOperation.QUERY
TEST_FIELD_NAME = "TEST_FIELD_NAME"
TEST_TYPE_CONDITION = "TEST_TYPE_CONDITION"
TEST_VARIABLE_NAME = "TEST_VARIABLE_NAME"
TEST_OPERATION_NAME = "TEST_OPERATION_NAME"
TEST_VARIABLE_TYPE = "TEST_VARIABLE_TYPE"
TEST_FRAGMENT_NAME = "TEST_FRAGMENT_NAME"
TEST_GRAPHQL_STR = \
    "query TEST_OPERATION_NAME($TEST_VARIABLE_NAME: TEST_VARIABLE_TYPE) {\n" + \
    "...TEST_FRAGMENT_NAME\n" + \
    "}\n" + \
    "fragment TEST_FRAGMENT_NAME on TEST_TYPE_CONDITION {\n" + \
    "TEST_FIELD_NAME\n" + \
    "}"


class DocumentTestCase(unittest.TestCase):
    def test_constructor(self) -> None:
        field = Field(TEST_FIELD_NAME)
        selection_set = SelectionSet(field)
        fragment = Fragment(name=TEST_FRAGMENT_NAME,
                            type_condition=TEST_TYPE_CONDITION,
                            selection_set=selection_set)
        selection_set2 = SelectionSet(fragment.fragment_spread())
        variables = VariableSet(
            Variable(name=TEST_VARIABLE_NAME,
                     variable_type=TEST_VARIABLE_TYPE)
        )
        operation = Operation(operation_type=TEST_OPERATION_TYPE,
                              name=TEST_OPERATION_NAME,
                              selection_set=selection_set2,
                              variables=variables)

        document = Document([operation, fragment])
        expected = [operation, fragment]
        actual = document.definitions
        self.assertEqual(actual, expected)

    def test_eq_equal(self) -> None:
        field = Field(TEST_FIELD_NAME)
        selection_set = SelectionSet(field)
        fragment = Fragment(name=TEST_FRAGMENT_NAME,
                            type_condition=TEST_TYPE_CONDITION,
                            selection_set=selection_set)
        selection_set2 = SelectionSet(fragment.fragment_spread())
        variables = VariableSet(
            Variable(name=TEST_VARIABLE_NAME,
                     variable_type=TEST_VARIABLE_TYPE)
        )
        operation = Operation(operation_type=TEST_OPERATION_TYPE,
                              name=TEST_OPERATION_NAME,
                              selection_set=selection_set2,
                              variables=variables)

        document = Document([operation, fragment])
        document2 = Document([operation, fragment])
        self.assertEqual(document, document2)

    def test_eq_not_equal(self) -> None:
        field = Field(TEST_FIELD_NAME)
        selection_set = SelectionSet(field)
        fragment = Fragment(name=TEST_FRAGMENT_NAME,
                            type_condition=TEST_TYPE_CONDITION,
                            selection_set=selection_set)
        selection_set2 = SelectionSet(fragment.fragment_spread())
        variables = VariableSet(
            Variable(name=TEST_VARIABLE_NAME,
                     variable_type=TEST_VARIABLE_TYPE)
        )
        operation = Operation(operation_type=TEST_OPERATION_TYPE,
                              name=TEST_OPERATION_NAME,
                              selection_set=selection_set2,
                              variables=variables)

        document = Document([operation, fragment])
        document2 = Document([operation])
        self.assertNotEqual(document, document2)

    def test_eq_not_equal_different_class(self) -> None:
        field = Field(TEST_FIELD_NAME)
        selection_set = SelectionSet(field)
        fragment = Fragment(name=TEST_FRAGMENT_NAME,
                            type_condition=TEST_TYPE_CONDITION,
                            selection_set=selection_set)
        selection_set2 = SelectionSet(fragment.fragment_spread())
        variables = VariableSet(
            Variable(name=TEST_VARIABLE_NAME,
                     variable_type=TEST_VARIABLE_TYPE)
        )
        operation = Operation(operation_type=TEST_OPERATION_TYPE,
                              name=TEST_OPERATION_NAME,
                              selection_set=selection_set2,
                              variables=variables)

        document = Document([operation, fragment])
        document2 = object()
        self.assertNotEqual(document, document2)

    def test_hash_equal(self) -> None:
        field = Field(TEST_FIELD_NAME)
        selection_set = SelectionSet(field)
        fragment = Fragment(name=TEST_FRAGMENT_NAME,
                            type_condition=TEST_TYPE_CONDITION,
                            selection_set=selection_set)
        selection_set2 = SelectionSet(fragment.fragment_spread())
        variables = VariableSet(
            Variable(name=TEST_VARIABLE_NAME,
                     variable_type=TEST_VARIABLE_TYPE)
        )
        operation = Operation(operation_type=TEST_OPERATION_TYPE,
                              name=TEST_OPERATION_NAME,
                              selection_set=selection_set2,
                              variables=variables)

        document = Document([operation, fragment])
        document2 = Document([operation, fragment])
        self.assertEqual(hash(document), hash(document2))

    def test_hash_not_equal(self) -> None:
        field = Field(TEST_FIELD_NAME)
        selection_set = SelectionSet(field)
        fragment = Fragment(name=TEST_FRAGMENT_NAME,
                            type_condition=TEST_TYPE_CONDITION,
                            selection_set=selection_set)
        selection_set2 = SelectionSet(fragment.fragment_spread())
        variables = VariableSet(
            Variable(name=TEST_VARIABLE_NAME,
                     variable_type=TEST_VARIABLE_TYPE)
        )
        operation = Operation(operation_type=TEST_OPERATION_TYPE,
                              name=TEST_OPERATION_NAME,
                              selection_set=selection_set2,
                              variables=variables)

        document = Document([operation, fragment])
        document2 = Document([operation])
        self.assertNotEqual(hash(document), hash(document2))

    def test_to_graphql(self) -> None:
        field = Field(TEST_FIELD_NAME)
        selection_set = SelectionSet(field)
        fragment = Fragment(name=TEST_FRAGMENT_NAME,
                            type_condition=TEST_TYPE_CONDITION,
                            selection_set=selection_set)
        selection_set2 = SelectionSet(fragment.fragment_spread())
        variables = VariableSet(
            Variable(name=TEST_VARIABLE_NAME,
                     variable_type=TEST_VARIABLE_TYPE)
        )
        operation = Operation(operation_type=TEST_OPERATION_TYPE,
                              name=TEST_OPERATION_NAME,
                              selection_set=selection_set2,
                              variables=variables)

        document = Document([operation, fragment])
        expected = TEST_GRAPHQL_STR
        actual = document.to_graphql()
        self.assertEqual(actual, expected)
