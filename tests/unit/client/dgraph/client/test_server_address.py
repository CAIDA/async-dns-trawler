import unittest

from dt.client.dgraph.client.server_address import ServerAddress

TEST_HOST = "TEST_HOST"
TEST_HOST_2 = "TEST_HOST_2"
TEST_PORT = 8080
TEST_REPR = "ServerAddress(TEST_HOST:8080)"
TEST_ADDRESS_1 = "TEST_HOST"
TEST_ADDRESS_2 = "TEST_HOST:8080"


class ServerAddressTestCase(unittest.TestCase):
    def test_constructor_no_port(self) -> None:
        server_address = ServerAddress(TEST_HOST)
        self.assertEqual(server_address.host, TEST_HOST)
        self.assertIsNone(server_address.port)

    def test_constructor_with_port(self) -> None:
        server_address = ServerAddress(TEST_HOST, TEST_PORT)
        self.assertEqual(server_address.host, TEST_HOST)
        self.assertEqual(server_address.port, TEST_PORT)

    def test_hash_equal(self) -> None:
        server_address = ServerAddress(TEST_HOST, TEST_PORT)
        server_address2 = ServerAddress(TEST_HOST, TEST_PORT)
        self.assertEqual(hash(server_address), hash(server_address2))

    def test_hash_not_equal(self) -> None:
        server_address = ServerAddress(TEST_HOST, TEST_PORT)
        server_address2 = ServerAddress(TEST_HOST_2, TEST_PORT)
        self.assertNotEqual(hash(server_address), hash(server_address2))

    def test_eq_equal(self) -> None:
        server_address = ServerAddress(TEST_HOST, TEST_PORT)
        server_address2 = ServerAddress(TEST_HOST, TEST_PORT)
        self.assertEqual(server_address, server_address2)

    def test_eq_not_equal(self) -> None:
        server_address = ServerAddress(TEST_HOST, TEST_PORT)
        server_address2 = ServerAddress(TEST_HOST_2, TEST_PORT)
        self.assertNotEqual(server_address, server_address2)

    def test_eq_not_equal_different_class(self) -> None:
        server_address = ServerAddress(TEST_HOST, TEST_PORT)
        server_address2 = object()
        self.assertNotEqual(server_address, server_address2)

    def test_repr(self) -> None:
        server_address = ServerAddress(TEST_HOST, TEST_PORT)
        self.assertEqual(repr(server_address), TEST_REPR)

    def test_get_address_no_port(self) -> None:
        server_address = ServerAddress(TEST_HOST)
        self.assertEqual(server_address.get_address(), TEST_ADDRESS_1)

    def test_get_address_with_port(self) -> None:
        server_address = ServerAddress(TEST_HOST, TEST_PORT)
        self.assertEqual(server_address.get_address(), TEST_ADDRESS_2)
