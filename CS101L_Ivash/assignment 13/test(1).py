import unittest
import Grades

class Grade_Test(unittest.TestCase):
    def test_total_returns_total_of_list(self):
        result = Grades.total([1,10,22])
        self.assertEqual(result,33,"The toal function should return 33")
    
    def test_total_returns_0(self):
        result = Grades.total([1,10,22])
        self.assertEqual(result,0,"The toal function should return 33")
    

unittest.main()