import unittest

from dt.util.is_primitive import is_primitive

TEST_INT = 1
TEST_BOOLEAN = True
TEST_FLOAT = 1.0
TEST_STR = "TEST_STR"
TEST_OBJECT = object()
TEST_NONE = None


class IsPrimitiveTestCase(unittest.TestCase):

    def test_is_primitive_int(self) -> None:
        expected = True
        actual = is_primitive(TEST_INT)
        self.assertEqual(expected, actual)

    def test_is_primitive_float(self) -> None:
        expected = True
        actual = is_primitive(TEST_FLOAT)
        self.assertEqual(expected, actual)

    def test_is_primitive_str(self) -> None:
        expected = True
        actual = is_primitive(TEST_STR)
        self.assertEqual(expected, actual)

    def test_is_primitive_boolean(self) -> None:
        expected = True
        actual = is_primitive(TEST_BOOLEAN)
        self.assertEqual(expected, actual)

    def test_is_primitive_object(self) -> None:
        expected = False
        actual = is_primitive(TEST_OBJECT)
        self.assertEqual(expected, actual)

    def test_is_primitive_none(self) -> None:
        expected = False
        actual = is_primitive(TEST_NONE)
        self.assertEqual(expected, actual)
