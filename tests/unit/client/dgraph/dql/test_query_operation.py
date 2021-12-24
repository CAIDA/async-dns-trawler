import unittest

from dt.client.dgraph.constants.comparison_function import ComparisonFunction
from dt.client.dgraph.constants.graphql_operation import GraphQLOperation
from dt.client.dgraph.dql.query_function import QueryFunction
from dt.client.dgraph.dql.query_operation import QueryOperation
from dt.client.dgraph.dql.query_root import QueryRoot
from dt.client.dgraph.graphql.argument import Argument
from dt.client.dgraph.graphql.field import Field
from dt.client.dgraph.graphql.selection_set import SelectionSet
from dt.client.dgraph.graphql.value import Value
from dt.client.dgraph.graphql.variable import Variable
from dt.client.dgraph.graphql.variable_set import VariableSet

TEST_OPERATION_NAME = "TEST_OPERATION_NAME"
TEST_COMPARISON_FUNCTION = ComparisonFunction.UID
TEST_ARG = "TEST_ARG"
TEST_VARIABLE_NAME = "TEST_VARIABLE_NAME"
TEST_VARIABLE_TYPE = "TEST_VARIABLE_TYPE"
TEST_FIELD_NAME = "TEST_FIELD_NAME"


class QueryOperationTestCase(unittest.TestCase):
    def test_constructor(self) -> None:
        args = (Value(TEST_ARG), )
        query_function = QueryFunction(TEST_COMPARISON_FUNCTION, args)
        query_root = QueryRoot(func=query_function)
        field = Field(name=TEST_FIELD_NAME)
        selection_set = SelectionSet(field)
        variables = VariableSet(Variable(name=TEST_VARIABLE_NAME,
                                         variable_type=TEST_VARIABLE_TYPE))
        query_operation = QueryOperation(name=TEST_OPERATION_NAME,
                                         selection_set=selection_set,
                                         query_root=query_root,
                                         variables=variables)
        self.assertEqual(query_operation.operation_type, GraphQLOperation.QUERY)
        self.assertEqual(query_operation.name, TEST_OPERATION_NAME)
        self.assertEqual(query_operation.selection_set, SelectionSet(
            Field(name=TEST_OPERATION_NAME,
                  arguments={Argument(name="func", input_value=query_function)},
                  selection_set=SelectionSet(field))
        ))
        self.assertEqual(query_operation.variables, variables)
