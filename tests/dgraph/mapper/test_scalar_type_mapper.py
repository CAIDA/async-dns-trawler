import unittest

from dt.dgraph.constants.scalar_type import ScalarType
from dt.dgraph.constants.rdf_type import RDFType
from dt.dgraph.mapper.scalar_type_mapper import ScalarTypeMapper


class ScalarTypeMapperTestCase(unittest.TestCase):
    def test_to_rdf_type_successful(self) -> None:
        expected = RDFType.INT
        actual = ScalarTypeMapper.to_rdf_type(ScalarType.INT)
        self.assertEqual(actual, expected)

    def test_to_rdf_type_successful_default(self) -> None:
        expected = RDFType.STRING
        actual = ScalarTypeMapper.to_rdf_type(ScalarType.DEFAULT)
        self.assertEqual(actual, expected)

    def test_from_rdf_type_successful(self) -> None:
        expected = ScalarType.STRING
        actual = ScalarTypeMapper.from_rdf_type(RDFType.STRING)
        self.assertEqual(actual, expected)
