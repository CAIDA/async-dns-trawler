from typing import Any, Dict, Optional
from unittest.mock import MagicMock

from pydgraph import DgraphClient

from tests.util.mock_builder import MockBuilder


class DGraphClientMocker:
    @staticmethod
    def _get_mock_txn(client: DgraphClient) -> MockBuilder:
        if not isinstance(client.txn, MagicMock):
            return MockBuilder().returns_mock()
        returned_txn = client.txn.return_value
        query = returned_txn.query
        mutate = returned_txn.mutate
        return MockBuilder().returns_mock() \
            .with_attr("query", query) \
            .with_attr("mutate", mutate)

    @staticmethod
    def mock_query(client: DgraphClient, returns: Optional[Dict[str, Any]]
                   = None, triggers: Optional[Any] = None) -> None:
        mock_txn_builder = DGraphClientMocker._get_mock_txn(client)
        mock_query_builder = mock_txn_builder.with_mock_attr("query")
        if triggers:
            mock_query_builder.triggers(triggers)
        if returns:
            mock_query_builder.returns_mock().from_dict(returns)
        else:
            mock_query_builder.returns(None)
        mock_txn = mock_query_builder.build_all()
        setattr(client, "txn", mock_txn)

    @staticmethod
    def mock_mutate(client: DgraphClient, returns: Optional[Dict[str, Any]]
                    = None, triggers: Optional[Any] = None) -> None:
        mock_txn_builder = DGraphClientMocker._get_mock_txn(client)
        mock_mutate_builder = mock_txn_builder.with_mock_attr("mutate")
        if triggers:
            mock_mutate_builder.triggers(triggers)
        if returns:
            mock_mutate_builder.returns_mock().from_dict(returns)
        else:
            mock_mutate_builder.returns(None)
        mock_txn = mock_mutate_builder.build_all()
        setattr(client, "txn", mock_txn)

    @staticmethod
    def mock_alter(client: DgraphClient, returns: Optional[Any] = None, triggers: Optional[Any] = None) -> None:
        mock_alter = MagicMock(return_value=returns, side_effect=triggers)
        setattr(client, "alter", mock_alter)
