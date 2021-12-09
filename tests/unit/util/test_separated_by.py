import unittest

from dt.util.separated_by import (comma_separated, newline_separated,
                                  single_space_separated)

TEST_ELEMENTS = ["EL1", "EL2", "EL3"]
TEST_COMMA_SEPARATED = "EL1, EL2, EL3"
TEST_NEWLINE_SEPARATED = "EL1\nEL2\nEL3"
TEST_SINGLE_SPACE_SEPARATED = "EL1 EL2 EL3"


class SeparatedByTestCase(unittest.TestCase):

    def test_comma_separated(self) -> None:
        expected = TEST_COMMA_SEPARATED
        actual = comma_separated(TEST_ELEMENTS)
        self.assertEqual(expected, actual)

    def test_newline_separated(self) -> None:
        expected = TEST_NEWLINE_SEPARATED
        actual = newline_separated(TEST_ELEMENTS)
        self.assertEqual(expected, actual)

    def test_single_space_separated(self) -> None:
        expected = TEST_SINGLE_SPACE_SEPARATED
        actual = single_space_separated(TEST_ELEMENTS)
        self.assertEqual(expected, actual)
