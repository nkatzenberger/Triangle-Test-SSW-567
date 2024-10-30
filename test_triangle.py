# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 16:32:52 2024

@author: njkat
"""
import unittest
import math
from Triangle import classify_triangle

class TriangleTest(unittest.TestCase):
    """Class representing tests for Triangle"""
    def test_init(self):
        """Tests initialization of Triangles"""
        t = classify_triangle(3,4,5)
        self.assertEqual(t.a,3)
        self.assertEqual(t.b,4)
        self.assertEqual(t.c,5)
    def test_is_a_triangle(self):
        """Tests if inputs return triangles"""
        t = classify_triangle(3,1,2)
        self.assertFalse(t.is_A_Triangle())
        self.assertTrue(classify_triangle(3, 4, 5).is_A_Triangle())
        self.assertFalse(classify_triangle(4, 5, 10).is_A_Triangle())
    def test_right_triangle(self):
        """Tests if inputs return right triangles"""
        t = classify_triangle(3,4,5)
        self.assertTrue(t.is_right_triangle())
        self.assertTrue(classify_triangle(5,4,3).is_right_triangle())
        self.assertFalse(classify_triangle(3,3,3).is_right_triangle())
        self.assertTrue(classify_triangle(4, 4, math.sqrt(32)).is_right_triangle())
    def test_triangle_type_equilateral(self):
        """Tests if inputs return equilateral triangles"""
        self.assertEqual(classify_triangle(3,3,3).triangle_Type(), "Equilateral")
        self.assertNotEqual(classify_triangle(4,4,5).triangle_Type(), "Equillateral")
    def test_traingle_type_isosceles(self):
        """Tests if inputs return isoceles triangles"""
        self.assertNotEqual(classify_triangle(4,4,4).triangle_Type(), "Isosceles")
        self.assertEqual(classify_triangle(3,3,4).triangle_Type(), "Isosceles")
        self.assertEqual(classify_triangle(8, 8, math.sqrt(128)).triangle_Type(), "Isosceles and Right")
    def test_triangle_type_scalene(self):
        """Tests if inputs return scalene triangles"""
        self.assertEqual(classify_triangle(15, 32, 34).triangle_Type(), "Scalene")
        self.assertEqual(classify_triangle(3,4,5).triangle_Type(), "Scalene and Right")
        self.assertNotEqual(classify_triangle(10,10,5).triangle_Type(), "Scalene")
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
