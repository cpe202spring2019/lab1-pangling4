import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc0 = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc0),"Location('SLO', 35.3, -120.7)")

        loc1 = Location("Antarctica 1", 82.9, 135)
        self.assertEqual(repr(loc1),"Location('Antarctica 1', 82.9, 135.0)")

        loc2 = Location("SLO", 35.30000001, -120.70000005)
        self.assertEqual(loc2 == loc0, True)

        loc3 = Location("SLO", 35.30000001, -120.7000005)
        self.assertEqual(loc2 == loc3, False)


if __name__ == "__main__":
        unittest.main()
