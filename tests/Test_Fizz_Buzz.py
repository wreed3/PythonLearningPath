import unittest
from src import fizz_buzz
from unittest.mock import MagicMock

class TestFizzBuzz(unittest.TestCase):

    def test_can_call_fizzbuzz(self):
        # mock = fizz_buzz
        mock = MagicMock(name='fizz_buzz')
        mock.fizz_buzz(1)
        mock.fizz_buzz.assert_called_with(1)

    def test_returns_1_when_1_passed_in(self):
        value = fizz_buzz.fizz_buzz(1)
        self.assertEqual(value, "1")

    def test_returns_2_when_2_passed_in(self):
        value = fizz_buzz.fizz_buzz(2)
        self.assertEqual(value, "2")

    def test_returns_fizz_when_3_passed_in(self):
        value = fizz_buzz.fizz_buzz(3)
        self.assertEqual(value, "Fizz")

    def test_returns_buzz_when_5_passed_in(self):
        value = fizz_buzz.fizz_buzz(5)
        self.assertEqual(value, "Buzz")

    def test_returns_fizz_for_multiples_of_3_passed_in(self):
        value1 = fizz_buzz.fizz_buzz(6)
        value2 = fizz_buzz.fizz_buzz(9)
        value3 = fizz_buzz.fizz_buzz(12)


        self.assertEqual(value1, "Fizz")
        self.assertEqual(value2, "Fizz")
        self.assertEqual(value3, "Fizz")


    def test_returns_buzz_for_multiples_of_5_passed_in(self):
        value1 = fizz_buzz.fizz_buzz(10)
        value2 = fizz_buzz.fizz_buzz(20)

        self.assertEqual(value1, "Buzz")
        self.assertEqual(value2, "Buzz")

    def test_returns_fizzbuzz_when_value_is_multiple_of_3_and_5(self):
        value = fizz_buzz.fizz_buzz(15)
        self.assertEqual(value,"FizzBuzz")


if __name__ == '__main__':
    unittest.main()
