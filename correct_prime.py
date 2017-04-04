import unittest
from prime_number_sum import list_of_prime_numbers


class Test_prime(unittest.TestCase):
    def test_correct_output(self):
        self.assertEqual(list_of_prime_numbers(5), [2, 3, 5],msg='The values entered are wrong')
