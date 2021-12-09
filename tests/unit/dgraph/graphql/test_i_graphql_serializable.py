import unittest

from dt.dgraph.graphql.i_graphql_serializable import IGraphQLSerializable

TEST_GRAPHQL_STR = "TEST_GRAPHQL_STR"
TEST_REPR = "TestSubclass[TEST_GRAPHQL_STR]"


class TestSubclass(IGraphQLSerializable):
    def to_graphql(self) -> str:
        return TEST_GRAPHQL_STR


class IGraphQLSerializableTestCase(unittest.TestCase):
    def test_repr(self) -> None:
        obj = TestSubclass()
        expected = TEST_REPR
        actual = repr(obj)
        self.assertEqual(actual, expected)
