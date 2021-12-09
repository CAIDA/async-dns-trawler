import unittest

from dt.dgraph.constants.comparison_function import ComparisonFunction
from dt.dgraph.dql.query_function import QueryFunction
from dt.dgraph.dql.query_root import QueryRoot
from dt.dgraph.graphql.argument import Argument
from dt.dgraph.graphql.value import Value

TEST_COMPARISON_FUNCTION = ComparisonFunction.EQ
TEST_ARG_1 = "TEST_ARG_1"
TEST_ARG_2 = "TEST_ARG_2"
TEST_FIRST = 1
TEST_OFFSET = 2
TEST_AFTER = 3


class QueryRootTestCase(unittest.TestCase):
    def test_constructor(self) -> None:
        args = (Value(TEST_ARG_1), Value(TEST_ARG_2))
        query_function = QueryFunction(TEST_COMPARISON_FUNCTION, args)
        query_root = QueryRoot(func=query_function,
                               first=TEST_FIRST,
                               offset=TEST_OFFSET,
                               after=TEST_AFTER)
        self.assertEqual(query_root.func, query_function)
        self.assertEqual(query_root.first, TEST_FIRST)
        self.assertEqual(query_root.offset, TEST_OFFSET)
        self.assertEqual(query_root.after, TEST_AFTER)

    def test_to_argument_set_only_func(self) -> None:
        args = (Value(TEST_ARG_1), Value(TEST_ARG_2))
        query_function = QueryFunction(TEST_COMPARISON_FUNCTION, args)
        query_root = QueryRoot(func=query_function)
        expected = {Argument("func", query_function)}
        actual = query_root.to_argument_set()
        self.assertEqual(actual, expected)

    def test_to_argument_set_only_func(self) -> None:
        args = (Value(TEST_ARG_1), Value(TEST_ARG_2))
        query_function = QueryFunction(TEST_COMPARISON_FUNCTION, args)
        query_root = QueryRoot(func=query_function)
        expected = {Argument("func", query_function)}
        actual = query_root.to_argument_set()
        self.assertEqual(actual, expected)

    def test_to_argument_set_func_with_first(self) -> None:
        args = (Value(TEST_ARG_1), Value(TEST_ARG_2))
        query_function = QueryFunction(TEST_COMPARISON_FUNCTION, args)
        query_root = QueryRoot(func=query_function,
                               first=TEST_FIRST)
        expected = {
            Argument("func", query_function),
            Argument("first", Value(TEST_FIRST))
        }
        actual = query_root.to_argument_set()
        self.assertEqual(actual, expected)

    def test_to_argument_set_func_with_offset(self) -> None:
        args = (Value(TEST_ARG_1), Value(TEST_ARG_2))
        query_function = QueryFunction(TEST_COMPARISON_FUNCTION, args)
        query_root = QueryRoot(func=query_function,
                               offset=TEST_OFFSET)
        expected = {
            Argument("func", query_function),
            Argument("offset", Value(TEST_OFFSET))
        }
        actual = query_root.to_argument_set()
        self.assertEqual(actual, expected)

    def test_to_argument_set_func_with_after(self) -> None:
        args = (Value(TEST_ARG_1), Value(TEST_ARG_2))
        query_function = QueryFunction(TEST_COMPARISON_FUNCTION, args)
        query_root = QueryRoot(func=query_function,
                               after=TEST_AFTER)
        expected = {
            Argument("func", query_function),
            Argument("after", Value(TEST_AFTER))
        }
        actual = query_root.to_argument_set()
        self.assertEqual(actual, expected)

    def test_to_argument_set_func_full(self) -> None:
        args = (Value(TEST_ARG_1), Value(TEST_ARG_2))
        query_function = QueryFunction(TEST_COMPARISON_FUNCTION, args)
        query_root = QueryRoot(func=query_function,
                               first=TEST_FIRST,
                               offset=TEST_OFFSET,
                               after=TEST_AFTER)
        expected = {
            Argument("func", query_function),
            Argument("first", Value(TEST_FIRST)),
            Argument("offset", Value(TEST_OFFSET)),
            Argument("after", Value(TEST_AFTER))
        }
        actual = query_root.to_argument_set()
        self.assertEqual(actual, expected)
