from django.test import TestCase
from app.calc import add

class CaclcTests(TestCase):

    '''The test functions must begin with test.'''
    def test_add_numbers(self):
        '''Test that two numbers are added together'''
        self.assertEqual(add(3,8), 11)
