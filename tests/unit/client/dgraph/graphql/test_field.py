import unittest

from dt.client.dgraph.graphql.argument import Argument
from dt.client.dgraph.graphql.field import Field
from dt.client.dgraph.graphql.fragment_spread import FragmentSpread
from dt.client.dgraph.graphql.selection_set import SelectionSet
from dt.client.dgraph.graphql.value import Value

TEST_FIELD_NAME = "TEST_FIELD_NAME"
TEST_FIELD_NAME_2 = "TEST_FIELD_NAME_2"
TEST_ARGUMENT_NAME = "TEST_ARGUMENT_NAME"
TEST_FRAGMENT_NAME = "TEST_FRAGMENT_NAME"
TEST_ALIAS = "TEST_ALIAS"
TEST_VALUE = "TEST_VALUE"
TEST_GRAPHQL_STR = "TEST_FIELD_NAME"
TEST_GRAPHQL_STR_2 = "TEST_ALIAS: TEST_FIELD_NAME"
TEST_GRAPHQL_STR_3 = "TEST_FIELD_NAME(TEST_ARGUMENT_NAME: TEST_VALUE)"
TEST_GRAPHQL_STR_4 = "TEST_FIELD_NAME {\n" + \
                     "...TEST_FRAGMENT_NAME\n" + \
                     "TEST_FIELD_NAME_2\n" + \
                     "}"
TEST_GRAPHQL_STR_5 = "TEST_ALIAS: TEST_FIELD_NAME(TEST_ARGUMENT_NAME: TEST_VALUE) {\n" + \
                     "...TEST_FRAGMENT_NAME\n" + \
                     "TEST_FIELD_NAME_2\n" + \
                     "}"


class FieldTestCase(unittest.TestCase):
    def test_constructor(self) -> None:
        value = Value(TEST_VALUE)
        arguments = {Argument(TEST_ARGUMENT_NAME, value)}
        selection_set = SelectionSet(FragmentSpread(TEST_FRAGMENT_NAME))
        field = Field(name=TEST_FIELD_NAME,
                      alias=TEST_ALIAS,
                      arguments=arguments,
                      selection_set=selection_set)
        self.assertEqual(field.name, TEST_FIELD_NAME)
        self.assertEqual(field.arguments, arguments)
        self.assertEqual(field.alias, TEST_ALIAS)
        self.assertEqual(field.selection_set, selection_set)

    def test_eq_equal(self) -> None:
        value = Value(TEST_VALUE)
        arguments = {Argument(TEST_ARGUMENT_NAME, value)}
        selection_set = SelectionSet(FragmentSpread(TEST_FRAGMENT_NAME))

        field = Field(name=TEST_FIELD_NAME,
                      alias=TEST_ALIAS,
                      arguments=arguments,
                      selection_set=selection_set)
        field2 = Field(name=TEST_FIELD_NAME,
                       alias=TEST_ALIAS,
                       arguments=arguments,
                       selection_set=selection_set)
        self.assertEqual(field, field2)

    def test_eq_not_equal_different_name(self) -> None:
        value = Value(TEST_VALUE)
        arguments = {Argument(TEST_ARGUMENT_NAME, value)}
        selection_set = SelectionSet(FragmentSpread(TEST_FRAGMENT_NAME))
        field = Field(name=TEST_FIELD_NAME,
                      alias=TEST_ALIAS,
                      arguments=arguments,
                      selection_set=selection_set)
        field2 = Field(name=TEST_FIELD_NAME_2,
                       alias=TEST_ALIAS,
                       arguments=arguments,
                       selection_set=selection_set)
        self.assertNotEqual(field, field2)

    def test_eq_not_equal_different_alias(self) -> None:
        value = Value(TEST_VALUE)
        arguments = {Argument(TEST_ARGUMENT_NAME, value)}
        selection_set = SelectionSet(FragmentSpread(TEST_FRAGMENT_NAME))
        field = Field(name=TEST_FIELD_NAME,
                      alias=TEST_ALIAS,
                      arguments=arguments,
                      selection_set=selection_set)
        field2 = Field(name=TEST_FIELD_NAME,
                       arguments=arguments,
                       selection_set=selection_set)
        self.assertNotEqual(field, field2)

    def test_eq_not_equal_different_arguments(self) -> None:
        value = Value(TEST_VALUE)
        arguments = {Argument(TEST_ARGUMENT_NAME, value)}
        selection_set = SelectionSet(FragmentSpread(TEST_FRAGMENT_NAME))
        field = Field(name=TEST_FIELD_NAME,
                      alias=TEST_ALIAS,
                      arguments=arguments,
                      selection_set=selection_set)
        field2 = Field(name=TEST_FIELD_NAME,
                       alias=TEST_ALIAS,
                       selection_set=selection_set)
        self.assertNotEqual(field, field2)

    def test_eq_not_equal_different_selection_set(self) -> None:
        value = Value(TEST_VALUE)
        arguments = {Argument(TEST_ARGUMENT_NAME, value)}
        selection_set = SelectionSet(FragmentSpread(TEST_FRAGMENT_NAME))
        field = Field(name=TEST_FIELD_NAME,
                      alias=TEST_ALIAS,
                      arguments=arguments,
                      selection_set=selection_set)
        field2 = Field(name=TEST_FIELD_NAME,
                       alias=TEST_ALIAS,
                       arguments=arguments)
        self.assertNotEqual(field, field2)

    def test_eq_not_equal_different_class(self) -> None:
        field = Field(TEST_FIELD_NAME)
        field2 = object()
        self.assertNotEqual(field, field2)

    def test_hash_equal(self) -> None:
        value = Value(TEST_VALUE)
        arguments = {Argument(TEST_ARGUMENT_NAME, value)}
        selection_set = SelectionSet(FragmentSpread(TEST_FRAGMENT_NAME))
        field = Field(name=TEST_FIELD_NAME,
                      alias=TEST_ALIAS,
                      arguments=arguments,
                      selection_set=selection_set)
        field2 = Field(name=TEST_FIELD_NAME,
                       alias=TEST_ALIAS,
                       arguments=arguments,
                       selection_set=selection_set)
        self.assertEqual(hash(field), hash(field2))

    def test_hash_not_equal(self) -> None:
        value = Value(TEST_VALUE)
        arguments = {Argument(TEST_ARGUMENT_NAME, value)}
        selection_set = SelectionSet(FragmentSpread(TEST_FRAGMENT_NAME))
        field = Field(name=TEST_FIELD_NAME,
                      alias=TEST_ALIAS,
                      arguments=arguments,
                      selection_set=selection_set)
        field2 = Field(name=TEST_FIELD_NAME_2)
        self.assertNotEqual(hash(field), hash(field2))

    def test_to_graphql_only_name(self) -> None:
        field = Field(name=TEST_FIELD_NAME)
        expected = TEST_GRAPHQL_STR
        actual = field.to_graphql()
        self.assertEqual(actual, expected)

    def test_to_graphql_with_alias(self) -> None:
        field = Field(name=TEST_FIELD_NAME,
                      alias=TEST_ALIAS)
        expected = TEST_GRAPHQL_STR_2
        actual = field.to_graphql()
        self.assertEqual(actual, expected)

    def test_to_graphql_with_arguments(self) -> None:
        value = Value(TEST_VALUE)
        arguments = {Argument(TEST_ARGUMENT_NAME, value)}
        field = Field(name=TEST_FIELD_NAME,
                      arguments=arguments)
        expected = TEST_GRAPHQL_STR_3
        actual = field.to_graphql()
        self.assertEqual(actual, expected)

    def test_to_graphql_with_selection_set(self) -> None:
        selection_set = SelectionSet(
            FragmentSpread(TEST_FRAGMENT_NAME),
            Field(TEST_FIELD_NAME_2)
        )
        field = Field(name=TEST_FIELD_NAME,
                      selection_set=selection_set)
        expected = TEST_GRAPHQL_STR_4
        actual = field.to_graphql()
        self.assertEqual(actual, expected)

    def test_to_graphql_full(self) -> None:
        value = Value(TEST_VALUE)
        arguments = {Argument(TEST_ARGUMENT_NAME, value)}
        selection_set = SelectionSet(
            FragmentSpread(TEST_FRAGMENT_NAME),
            Field(TEST_FIELD_NAME_2)
        )
        field = Field(name=TEST_FIELD_NAME,
                      alias=TEST_ALIAS,
                      arguments=arguments,
                      selection_set=selection_set)
        expected = TEST_GRAPHQL_STR_5
        actual = field.to_graphql()
        self.assertEqual(actual, expected)
