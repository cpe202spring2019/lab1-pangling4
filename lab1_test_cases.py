import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """_____"""

        # used to check for exception
        tlist = None
        with self.assertRaises(ValueError):
            max_list_iter(tlist)

        # tests finding max in a list of consecutive positive integers
        self.assertEqual(max_list_iter([1,2,3,4,5]),5)

        # tests finding max in a very short list of integers
        self.assertEqual(max_list_iter([1,5]),5)

        # tests finding max in a list of repeating/non-consecutive integers
        self.assertEqual(max_list_iter([1,2,2,5,2]),5)

        # tests finding max when max is a repeating integer
        self.assertEqual(max_list_iter([1,2,2,0,2]),2)

    def test_reverse_rec(self):
        """______"""

        # used to check for exception
        tlist = None
        with self.assertRaises(ValueError):
            max_list_iter(tlist)

        # checks a simple list of consecutive integers
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

        # checks a list of non-consecutive/repeating integers
        self.assertEqual(reverse_rec([3,2,2,2,1,0,-5]),[-5,0,1,2,2,2,3])

    def test_bin_search(self):
        """______"""

        # used to check for exception
        tlist = None
        with self.assertRaises(ValueError):
            max_list_iter(tlist)

        # targets an integer in of a simple list of consecutive integers
        list_val1 =[0,1,2,3,4,7,8,9,10]
        self.assertEqual(bin_search(4, 0, len(list_val1)-1, list_val1), 4)

        # targets an integer in of a list of non-consecutive/repeating integers
        list_val2 =[0,2,3,4,6,8]
        self.assertEqual(bin_search(6, 0, len(list_val2)-1, list_val2), 4)

        # targets an integer that is not in a list of non-consecutive/negative integers
        list_val3 =[-5,-1,0,1,5]
        bin_search(6, 0, len(list_val3)-1, list_val3)
        self.assertEqual(bin_search(6, 0, len(list_val3)-1, list_val3), None)

        # targets a negative integer in a list of non-consecutive integers
        self.assertEqual(bin_search(-1, 0, len(list_val3)-1, list_val3), 1)

if __name__ == "__main__":
        unittest.main()
