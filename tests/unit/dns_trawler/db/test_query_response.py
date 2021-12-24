import unittest
from typing import Any

from dt.dns_trawler.db.query_response import QueryResponse


class TestItem:
    def __init__(self, value: str):
        self.value = value

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, TestItem):
            return False
        return self.value == other.value


TEST_VALUE = "TEST_VALUE"
TEST_VALUE_2 = "TEST_VALUE_2"
TEST_NEXT_TOKEN = "TEST_NEXT_TOKEN"
TEST_NEXT_TOKEN_2 = "TEST_NEXT_TOKEN_2"


class QueryResponseTestCase(unittest.TestCase):
    def test_constructor(self) -> None:
        items = [TestItem(TEST_VALUE)]
        query_response = QueryResponse[TestItem](items, TEST_NEXT_TOKEN)
        self.assertEqual(query_response.items, items)
        self.assertEqual(query_response.next_token, TEST_NEXT_TOKEN)

    def test_eq_equal(self) -> None:
        items = [TestItem(TEST_VALUE)]
        query_response = QueryResponse[TestItem](items, TEST_NEXT_TOKEN)
        query_response2 = QueryResponse[TestItem](items, TEST_NEXT_TOKEN)
        self.assertEqual(query_response, query_response2)

    def test_eq_not_equal_different_items(self) -> None:
        items = [TestItem(TEST_VALUE)]
        items2 = [TestItem(TEST_VALUE_2)]
        query_response = QueryResponse[TestItem](items, TEST_NEXT_TOKEN)
        query_response2 = QueryResponse[TestItem](items2, TEST_NEXT_TOKEN)
        self.assertNotEqual(query_response, query_response2)

    def test_eq_not_equal_different_next_token(self) -> None:
        items = [TestItem(TEST_VALUE)]
        query_response = QueryResponse[TestItem](items, TEST_NEXT_TOKEN)
        query_response2 = QueryResponse[TestItem](items, TEST_NEXT_TOKEN_2)
        self.assertNotEqual(query_response, query_response2)

    def test_eq_not_equal_different_class(self) -> None:
        items = [TestItem(TEST_VALUE)]
        query_response = QueryResponse[TestItem](items, TEST_NEXT_TOKEN)
        query_response2 = object()
        self.assertNotEqual(query_response, query_response2)
