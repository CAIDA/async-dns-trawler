from typing import Any


def is_primitive(value: Any) -> bool:
    return isinstance(value, (str, int, float, bool))
