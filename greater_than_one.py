import unittest
import prime_number_sum
from prime_number_sum import  list_of_prime_numbers

class Test_positive_values(unittest.TestCase):
    def test_greater_than_one(self):
        if prime_number_sum.list_of_prime_numbers<1:
            self.assertFalse(list_of_prime_numbers(),1,msg='Enter values greater than 1')

