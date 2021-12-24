import unittest
from unittest.mock import Mock

from dt.client.dgraph.graphql.graphql import GraphQL
from dt.client.dgraph.graphql.value import Value
from tests.util.mock_builder import MockBuilder

TEST_GRAPHQL_STR = "TEST_GRAPHQL_STR"
TEST_GRAPHQL_STR_2 = "TEST_GRAPHQL_STR_2"


class GraphQLTestCase(unittest.TestCase):
    def test_graphql(self) -> None:
        mock = Mock(spec=Value)
        GraphQL(mock)
        mock.to_graphql.assert_called_once()

    def test_graphql_list(self) -> None:
        mock1 = MockBuilder(spec=Value) \
            .with_mock_attr('to_graphql') \
            .returns(TEST_GRAPHQL_STR) \
            .build_all()
        mock2 = MockBuilder(spec=Value) \
            .with_mock_attr('to_graphql') \
            .returns(TEST_GRAPHQL_STR_2) \
            .build_all()
        expected = [TEST_GRAPHQL_STR, TEST_GRAPHQL_STR_2]
        actual = GraphQL([mock1, mock2])
        self.assertEqual(expected, actual)
