from __future__ import annotations

from typing import Any, Dict, Optional, Union
from unittest.mock import MagicMock


class MockBuilder:
    ''' Simplifies generating complex mock objects

    Attributes:
    parent: PMockBuilder which spawnned the current MockBuilder
    return_value: Value for mock to return when the mock is called
    '''

    def __init__(self, parent: Optional[MockBuilder] = None, **kwargs: Any):
        self.parent = parent
        self.mock = MagicMock(**kwargs)

    def returns(self, return_value: Any) -> MockBuilder:
        self.mock.return_value = return_value
        return self

    def triggers(self, side_effect: Any) -> MockBuilder:
        self.mock.side_effect = side_effect
        return self

    def from_dict(self, attrs: Dict[Any, Any]) -> MockBuilder:
        for key, value in attrs.items():
            setattr(self.mock, key, value)
        return self

    def with_attr(self, key: str, value: Any) -> MockBuilder:
        setattr(self.mock, key, value)
        return self

    def with_mock_attr(self, key: str, **kwargs: Any) -> MockBuilder:
        child_builder = MockBuilder(parent=self, **kwargs)
        setattr(self.mock, key, child_builder.mock)
        return child_builder

    def returns_mock(self, **kwargs: Any) -> MockBuilder:
        child_builder = MockBuilder(parent=self, **kwargs)
        self.mock.return_value = child_builder.mock
        return child_builder

    def build(self) -> Union[MagicMock, MockBuilder]:
        if self.parent is not None:
            return self.parent
        return self.mock

    def build_all(self) -> MagicMock:
        parent = self.parent
        current = self
        while parent is not None:
            current = parent
            parent = parent.parent
        return current.mock
