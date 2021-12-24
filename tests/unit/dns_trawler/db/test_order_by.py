import unittest

from dt.dns_trawler.constants.sort_direction import SortDirection
from dt.dns_trawler.db.order_by import OrderBy
from dt.dns_trawler.db.query_field import QueryField

TEST_FIELD_NAME = "TEST_FIELD_NAME"
TEST_FIELD_NAME_2 = "TEST_FIELD_NAME_2"
TEST_SORT_DIRECTION = SortDirection.ASC
TEST_SORT_DIRECTION_2 = SortDirection.DESC
TEST_REPR = "OrderBy(TEST_FIELD_NAME, ASC)"


class OrderByTestCase(unittest.TestCase):
    def test_constructor(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)
        order_by = OrderBy(query_field, TEST_SORT_DIRECTION)
        self.assertEqual(order_by.query_field, query_field)
        self.assertEqual(order_by.sort_direction, TEST_SORT_DIRECTION)

    def test_eq_equal(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)
        order_by = OrderBy(query_field, TEST_SORT_DIRECTION)
        order_by2 = OrderBy(query_field, TEST_SORT_DIRECTION)
        self.assertEqual(order_by, order_by2)

    def test_eq_not_equal_different_query_field(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)
        query_field2 = QueryField(TEST_FIELD_NAME_2)
        order_by = OrderBy(query_field, TEST_SORT_DIRECTION)
        order_by2 = OrderBy(query_field2, TEST_SORT_DIRECTION)
        self.assertNotEqual(order_by, order_by2)

    def test_eq_not_equal_different_sort_direction(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)
        order_by = OrderBy(query_field, TEST_SORT_DIRECTION)
        order_by2 = OrderBy(query_field, TEST_SORT_DIRECTION_2)
        self.assertNotEqual(order_by, order_by2)

    def test_eq_not_equal_different_class(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)
        order_by = OrderBy(query_field, TEST_SORT_DIRECTION)
        order_by2 = object()
        self.assertNotEqual(order_by, order_by2)

    def test_repr(self) -> None:
        query_field = QueryField(TEST_FIELD_NAME)
        order_by = OrderBy(query_field, TEST_SORT_DIRECTION)
        actual = repr(order_by)
        expected = TEST_REPR
        self.assertEqual(actual, expected)
