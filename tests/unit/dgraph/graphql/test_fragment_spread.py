import unittest

from dt.dgraph.graphql.fragment_spread import FragmentSpread

TEST_FRAGMENT_NAME = "TEST_FRAGMENT_NAME"
TEST_OTHER_FRAGMENT_NAME = "TEST_OTHER_FRAGMENT_NAME"
TEST_GRAPHQL_STR = "...TEST_FRAGMENT_NAME"


class FragmentSpreadTestCase(unittest.TestCase):
    def test_constructor(self) -> None:
        fragment_spread = FragmentSpread(TEST_FRAGMENT_NAME)
        self.assertEqual(fragment_spread.fragment_name, TEST_FRAGMENT_NAME)

    def test_eq_equal(self) -> None:
        fragment_spread = FragmentSpread(TEST_FRAGMENT_NAME)
        fragment_spread2 = FragmentSpread(TEST_FRAGMENT_NAME)
        self.assertEqual(fragment_spread, fragment_spread2)

    def test_eq_not_equal(self) -> None:
        fragment_spread = FragmentSpread(TEST_FRAGMENT_NAME)
        fragment_spread2 = FragmentSpread(TEST_OTHER_FRAGMENT_NAME)
        self.assertNotEqual(fragment_spread, fragment_spread2)

    def test_eq_not_equal_different_class(self) -> None:
        fragment_spread = FragmentSpread(TEST_FRAGMENT_NAME)
        fragment_spread2 = object()
        self.assertNotEqual(fragment_spread, fragment_spread2)

    def test_hash_equal(self) -> None:
        fragment_spread = FragmentSpread(TEST_FRAGMENT_NAME)
        fragment_spread2 = FragmentSpread(TEST_FRAGMENT_NAME)
        self.assertEqual(hash(fragment_spread), hash(fragment_spread2))

    def test_hash_not_equal(self) -> None:
        fragment_spread = FragmentSpread(TEST_FRAGMENT_NAME)
        fragment_spread2 = FragmentSpread(TEST_OTHER_FRAGMENT_NAME)
        self.assertNotEqual(hash(fragment_spread), hash(fragment_spread2))

    def test_to_graphql_str(self) -> None:
        fragment_spread = FragmentSpread(TEST_FRAGMENT_NAME)
        expected = TEST_GRAPHQL_STR
        actual = fragment_spread.to_graphql()
        self.assertEqual(actual, expected)
