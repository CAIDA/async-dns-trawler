import unittest

from dt.client.dgraph.graphql.field import Field
from dt.client.dgraph.graphql.fragment import Fragment
from dt.client.dgraph.graphql.fragment_spread import FragmentSpread
from dt.client.dgraph.graphql.selection_set import SelectionSet

TEST_FIELD_NAME = "TEST_FIELD_NAME"
TEST_FRAGMENT_NAME = "TEST_FRAGMENT_NAME"
TEST_FRAGMENT_NAME_2 = "TEST_FRAGMENT_NAME_2"
TEST_TYPE_CONDITION = "TEST_TYPE_CONDITION"
TEST_TYPE_CONDITION_2 = "TEST_TYPE_CONDITION_2"
TEST_GRAPHQL_STR = "fragment TEST_FRAGMENT_NAME on TEST_TYPE_CONDITION {\n" + \
                   "...TEST_FRAGMENT_NAME_2\n" + \
                   "TEST_FIELD_NAME\n" + \
                   "}"


class FragmentTestCase(unittest.TestCase):
    def test_constructor(self) -> None:
        selection_set = SelectionSet(Field(name=TEST_FIELD_NAME))
        fragment = Fragment(name=TEST_FRAGMENT_NAME,
                            type_condition=TEST_TYPE_CONDITION,
                            selection_set=selection_set)

        self.assertEqual(fragment.name, TEST_FRAGMENT_NAME)
        self.assertEqual(fragment.type_condition, TEST_TYPE_CONDITION)
        self.assertEqual(fragment.selection_set, selection_set)

    def test_eq_equal(self) -> None:
        selection_set = SelectionSet(Field(name=TEST_FIELD_NAME))
        fragment = Fragment(name=TEST_FRAGMENT_NAME,
                            type_condition=TEST_TYPE_CONDITION,
                            selection_set=selection_set)
        fragment2 = Fragment(name=TEST_FRAGMENT_NAME,
                             type_condition=TEST_TYPE_CONDITION,
                             selection_set=selection_set)
        self.assertEqual(fragment, fragment2)

    def test_eq_not_equal_different_name(self) -> None:
        selection_set = SelectionSet(Field(name=TEST_FIELD_NAME))
        fragment = Fragment(name=TEST_FRAGMENT_NAME,
                            type_condition=TEST_TYPE_CONDITION,
                            selection_set=selection_set)
        fragment2 = Fragment(name=TEST_FRAGMENT_NAME_2,
                             type_condition=TEST_TYPE_CONDITION,
                             selection_set=selection_set)
        self.assertNotEqual(fragment, fragment2)

    def test_eq_not_equal_different_type_condition(self) -> None:
        selection_set = SelectionSet(Field(name=TEST_FIELD_NAME))
        fragment = Fragment(name=TEST_FRAGMENT_NAME,
                            type_condition=TEST_TYPE_CONDITION,
                            selection_set=selection_set)
        fragment2 = Fragment(name=TEST_FRAGMENT_NAME,
                             type_condition=TEST_TYPE_CONDITION_2,
                             selection_set=selection_set)
        self.assertNotEqual(fragment, fragment2)

    def test_eq_not_equal_different_selection_set(self) -> None:
        selection_set = SelectionSet(Field(name=TEST_FIELD_NAME))
        selection_set2 = SelectionSet(FragmentSpread(TEST_FRAGMENT_NAME_2))
        fragment = Fragment(name=TEST_FRAGMENT_NAME,
                            type_condition=TEST_TYPE_CONDITION,
                            selection_set=selection_set)
        fragment2 = Fragment(name=TEST_FRAGMENT_NAME,
                             type_condition=TEST_TYPE_CONDITION,
                             selection_set=selection_set2)
        self.assertNotEqual(fragment, fragment2)

    def test_eq_not_equal_different_class(self) -> None:
        selection_set = SelectionSet(Field(name=TEST_FIELD_NAME))
        fragment = Fragment(name=TEST_FRAGMENT_NAME,
                            type_condition=TEST_TYPE_CONDITION,
                            selection_set=selection_set)
        fragment2 = object()
        self.assertNotEqual(fragment, fragment2)

    def test_hash_equal(self) -> None:
        selection_set = SelectionSet(Field(name=TEST_FIELD_NAME))
        fragment = Fragment(name=TEST_FRAGMENT_NAME,
                            type_condition=TEST_TYPE_CONDITION,
                            selection_set=selection_set)
        fragment2 = Fragment(name=TEST_FRAGMENT_NAME,
                             type_condition=TEST_TYPE_CONDITION,
                             selection_set=selection_set)
        self.assertEqual(hash(fragment), hash(fragment2))

    def test_hash_not_equal(self) -> None:
        selection_set = SelectionSet(Field(name=TEST_FIELD_NAME))
        fragment = Fragment(name=TEST_FRAGMENT_NAME,
                            type_condition=TEST_TYPE_CONDITION,
                            selection_set=selection_set)
        fragment2 = Fragment(name=TEST_FRAGMENT_NAME_2,
                             type_condition=TEST_TYPE_CONDITION,
                             selection_set=selection_set)
        self.assertNotEqual(hash(fragment), hash(fragment2))

    def test_fragment_spread(self) -> None:
        selection_set = SelectionSet(Field(name=TEST_FIELD_NAME))
        fragment = Fragment(name=TEST_FRAGMENT_NAME,
                            type_condition=TEST_TYPE_CONDITION,
                            selection_set=selection_set)
        expected = FragmentSpread(TEST_FRAGMENT_NAME)
        actual = fragment.fragment_spread()
        self.assertEqual(expected, actual)

    def test_to_graphql(self) -> None:
        selection_set = SelectionSet(
            Field(name=TEST_FIELD_NAME),
            FragmentSpread(TEST_FRAGMENT_NAME_2)
        )
        fragment = Fragment(name=TEST_FRAGMENT_NAME,
                            type_condition=TEST_TYPE_CONDITION,
                            selection_set=selection_set)
        expected = TEST_GRAPHQL_STR
        actual = fragment.to_graphql()
        self.assertEqual(actual, expected)
