# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 16:32:52 2024

@author: njkat
"""
import unittest
import math
from Triangle import classify_triangle

class TriangleTest(unittest.TestCase):
    def test_init(self):
        #Sides stored properly in __init__()
        t = classify_triangle(3,4,5)
        self.assertEqual(t.a,3)
        self.assertEqual(t.b,4)
        self.assertEqual(t.c,5)
        
    def test_is_A_Triangle(self):
        t = classify_triangle(3,1,2)
        self.assertFalse(t.is_A_Triangle())
        self.assertTrue(classify_triangle(3, 4, 5).is_A_Triangle())
        self.assertFalse(classify_triangle(4, 5, 10).is_A_Triangle())
        
    def test_right_triangle(self):
         #test right triangle detection
        t = classify_triangle(3,4,5)
        self.assertTrue(t.is_right_triangle())
        self.assertTrue(classify_triangle(5,4,3).is_right_triangle())
        self.assertFalse(classify_triangle(3,3,3).is_right_triangle())
        self.assertTrue(classify_triangle(4, 4, math.sqrt(32)).is_right_triangle())
        
    def test_triangle_type(self):
          self.assertEqual(classify_triangle(3,3,3).triangle_Type(), "Equilateral")
          self.assertNotEqual(classify_triangle(4,4,4).triangle_Type(), "Isosceles")
          self.assertEqual(classify_triangle(3,3,4).triangle_Type(), "Isosceles")
          self.assertEqual(classify_triangle(8, 8, math.sqrt(128)).triangle_Type(), "Isosceles and Right")
          self.assertNotEqual(classify_triangle(4,4,5).triangle_Type(), "Equillateral")
          self.assertEqual(classify_triangle(15, 32, 34).triangle_Type(), "Scalene")
          self.assertEqual(classify_triangle(3,4,5).triangle_Type(), "Scalene and Right")
          self.assertNotEqual(classify_triangle(10,10,5).triangle_Type(), "Scalene")
          if __name__ == '__main__':
            unittest.main(exit=False, verbosity=2)
t = TriangleTest()
t.test_init()
t.test_is_A_Triangle()
t.test_triangle_type()
t.test_right_triangle()
"""
class BuggyTriangle:
    def __init__(self, s1, s2, s3):
        self.a = s1
        self.b = s2
        self.c = s3
    def right_triangle(self):
        return round(((self.a ** 2) + (self.b ** 2)), 2) == round((self.c ** 2), 2)


class BuggyTriangleTest(unittest.TestCase):
    def test_init(self):
        # Sides stored properly in __init__() 
        t = BuggyTriangle(3,4,5)
        self.assertEqual(t.a,3)
        self.assertEqual(t.b,4)
        self.assertEqual(t.c,5)
    def test_right_triangle(self):
        # test right triangle detection 
        t = BuggyTriangle(3,4,5)
        self.assertTrue(t.right_triangle())
        self.assertTrue(BuggyTriangle(5,4,3).right_triangle())
        self.assertFalse(BuggyTriangle(3,3,3).right_triangle())
        if __name__ == '__main__':
            unittest.main(exit=False, verbosity=2)
t = BuggyTriangleTest()
t.test_init()
t.test_right_triangle() """