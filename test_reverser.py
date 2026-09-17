import unittest

from reverser import is_prime, reverse_string


class ReverseStringTest(unittest.TestCase):
    def test_reverse_string(self) -> None:
        self.assertEqual(reverse_string("hello"), "olleh")


class PrimeNumberTest(unittest.TestCase):
    def test_prime_numbers(self) -> None:
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(97))

    def test_non_prime_numbers(self) -> None:
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(100))


if __name__ == "__main__":
    unittest.main()
