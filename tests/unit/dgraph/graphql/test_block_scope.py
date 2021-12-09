import unittest

from dt.dgraph.graphql.block_scope import BlockScope

TEST_LABEL = "TEST_LABEL"
TEST_BODY = "TEST_BODY"
TEST_PARAMETERS = "TEST_PARAMETERS"
TEST_BLOCK_TYPE = "TEST_BLOCK_TYPE"
TEST_GRAPHQL_STR_1 = ""
TEST_GRAPHQL_STR_2 = "TEST_BLOCK_TYPE TEST_LABEL(TEST_PARAMETERS) {\n" + \
                     "TEST_BODY\n" + \
                     "}"
TEST_GRAPHQL_STR_3 = "TEST_BLOCK_TYPE"
TEST_GRAPHQL_STR_4 = "TEST_LABEL"
TEST_GRAPHQL_STR_5 = "(TEST_PARAMETERS)"
TEST_GRAPHQL_STR_6 = "{\n" + \
                     "TEST_BODY\n" + \
                     "}"
TEST_GRAPHQL_STR_7 = "TEST_BLOCK_TYPE TEST_LABEL(TEST_PARAMETERS)"


class BlockScopeTestCase(unittest.TestCase):
    def test_constructor(self) -> None:
        block_scope = BlockScope(block_type=TEST_BLOCK_TYPE,
                                 label=TEST_LABEL,
                                 parameters=TEST_PARAMETERS,
                                 body=TEST_BODY)
        self.assertEqual(block_scope.block_type, TEST_BLOCK_TYPE)
        self.assertEqual(block_scope.label, TEST_LABEL)
        self.assertEqual(block_scope.parameters, TEST_PARAMETERS)
        self.assertEqual(block_scope.body, TEST_BODY)

    def test_to_graphql_empty(self) -> None:
        block_scope = BlockScope()
        self.assertEqual(block_scope.to_graphql(), TEST_GRAPHQL_STR_1)

    def test_to_graphql_full(self) -> None:
        block_scope = BlockScope(block_type=TEST_BLOCK_TYPE,
                                 label=TEST_LABEL,
                                 parameters=TEST_PARAMETERS,
                                 body=TEST_BODY)
        self.assertEqual(block_scope.to_graphql(), TEST_GRAPHQL_STR_2)

    def test_to_graphql_block_type(self) -> None:
        block_scope = BlockScope(block_type=TEST_BLOCK_TYPE)
        self.assertEqual(block_scope.to_graphql(), TEST_GRAPHQL_STR_3)

    def test_to_graphql_label(self) -> None:
        block_scope = BlockScope(label=TEST_LABEL)
        self.assertEqual(block_scope.to_graphql(), TEST_GRAPHQL_STR_4)

    def test_to_graphql_parameters(self) -> None:
        block_scope = BlockScope(parameters=TEST_PARAMETERS)
        self.assertEqual(block_scope.to_graphql(), TEST_GRAPHQL_STR_5)

    def test_to_graphql_body(self) -> None:
        block_scope = BlockScope(body=TEST_BODY)
        self.assertEqual(block_scope.to_graphql(), TEST_GRAPHQL_STR_6)

    def test_to_graphql_no_body(self) -> None:
        block_scope = BlockScope(block_type=TEST_BLOCK_TYPE,
                                 label=TEST_LABEL,
                                 parameters=TEST_PARAMETERS)
        self.assertEqual(block_scope.to_graphql(), TEST_GRAPHQL_STR_7)
