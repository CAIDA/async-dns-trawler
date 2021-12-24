import unittest

from dt.client.dgraph.graphql.field import Field
from dt.client.dgraph.graphql.fragment_spread import FragmentSpread
from dt.client.dgraph.graphql.selection_set import SelectionSet

TEST_FIELD_NAME = "TEST_FIELD_NAME"
TEST_FRAGMENT_NAME = "TEST_FRAGMENT_NAME"
TEST_GRAPHQL_STR = "...TEST_FRAGMENT_NAME\n" + \
                   "TEST_FIELD_NAME"


class SelectionSetTestCase(unittest.TestCase):
    def test_constructor(self) -> None:
        field = Field(TEST_FIELD_NAME)
        selection_set = SelectionSet(field)
        expected = {field}
        actual = selection_set.items
        self.assertEqual(actual, expected)

    def test_eq_equal(self) -> None:
        field = Field(TEST_FIELD_NAME)
        selection_set = SelectionSet(field)
        selection_set2 = SelectionSet(field)
        self.assertEqual(selection_set, selection_set2)

    def test_eq_not_equal(self) -> None:
        field = Field(TEST_FIELD_NAME)
        fragment_spread = FragmentSpread(TEST_FRAGMENT_NAME)
        selection_set = SelectionSet(field)
        selection_set2 = SelectionSet(fragment_spread)
        self.assertNotEqual(selection_set, selection_set2)

    def test_eq_not_equal_different_class(self) -> None:
        field = Field(TEST_FIELD_NAME)
        selection_set = SelectionSet(field)
        selection_set2 = object()
        self.assertNotEqual(selection_set, selection_set2)

    def test_hash_equal(self) -> None:
        field = Field(TEST_FIELD_NAME)
        selection_set = SelectionSet(field)
        selection_set2 = SelectionSet(field)
        self.assertEqual(hash(selection_set), hash(selection_set2))

    def test_hash_not_equal(self) -> None:
        field = Field(TEST_FIELD_NAME)
        fragment_spread = FragmentSpread(TEST_FRAGMENT_NAME)
        selection_set = SelectionSet(field)
        selection_set2 = SelectionSet(fragment_spread)
        self.assertNotEqual(hash(selection_set), hash(selection_set2))

    def test_to_graphql(self) -> None:
        field = Field(TEST_FIELD_NAME)
        fragment_spread = FragmentSpread(TEST_FRAGMENT_NAME)
        selection_set = SelectionSet(field, fragment_spread)
        expected = TEST_GRAPHQL_STR
        actual = selection_set.to_graphql()
        self.assertEqual(actual, expected)
