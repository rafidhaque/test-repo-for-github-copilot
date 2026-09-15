import unittest

from reverser import reverse_string


class ReverseStringTest(unittest.TestCase):
    def test_reverse_string(self) -> None:
        self.assertEqual(reverse_string("hello"), "olleh")


if __name__ == "__main__":
    unittest.main()
