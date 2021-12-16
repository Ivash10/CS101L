import Grades
import unittest

class Test(unittest.TestCase):
    
    def test_odd(self):
        g = Grades()
        self.assertEqual(g.median([5,1,2]),2)
    
    def test_even(self):
        g = Grades()
        self.assertEqual(g.median([5,1,2,3]),2.5)

    def test_empty(self):
        g = Grades()
        with self.assertRaises(ValueError):
            g.median([])
    
unittest.main()