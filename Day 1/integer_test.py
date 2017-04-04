import unittest
import prime_number_sum
from prime_number_sum import list_of_prime_numbers


class Test_intergers(unittest.TestCase):
    def test_for_intergers(self):

        if int:
            self.assertRaises(TypeError,list_of_prime_numbers(5),2, msg='Only interger values are allowed')
