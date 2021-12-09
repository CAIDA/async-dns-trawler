from typing import Iterable


def comma_separated(elements: Iterable[str]) -> str:
    return ", ".join(elements)


def newline_separated(elements: Iterable[str]) -> str:
    return "\n".join(elements)


def single_space_separated(elements: Iterable[str]) -> str:
    return " ".join(elements)
