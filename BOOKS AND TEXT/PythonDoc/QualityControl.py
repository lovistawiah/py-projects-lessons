def average(values=[]):
    """
    Computes the arithmetic mean of a list of numbers

    """
    return sum(values)/len(values)

list1 =[1,34,5,36,36,2,6]
avg = average(list1)
print(avg)

#TODO: learn doctest module
import doctest
print(doctest.testmod())

import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()