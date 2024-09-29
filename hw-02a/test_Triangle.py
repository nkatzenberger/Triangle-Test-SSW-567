# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classifyTriangle(5,5,5),'Equilateral','5,5,5 should be equilateral')
    #New tests
    def testIsosceles(self):
        self.assertEqual(classifyTriangle(3,3,5), 'Isosceles', 'should be Isosceles')
        self.assertEqual(classifyTriangle(6,6,4), 'Isosceles', 'should be Isosceles')
    
    def testScalene(self):
        self.assertEqual(classifyTriangle(4, 5, 6), "Scalene", "4,5,6 should return Scalene")
        self.assertEqual(classifyTriangle(6, 7, 9), "Scalene", "6,7,9 should return Scalene")

    def testFalseClassifications(self):
        self.assertNotEqual(classifyTriangle(3,4,5),'Isoceles','3,4,5 should be Right')
        self.assertNotEqual(classifyTriangle(3,4,5),'Equilateral','3,4,5 should be Right')
        self.assertNotEqual(classifyTriangle(5,4,5),'Scalene','3,4,5 should be Right')

    def testNonTriangles(self):
        self.assertEqual(classifyTriangle(3,4,9), 'NotATriangle')
        self.assertNotEqual(classifyTriangle(3,4,5),'NotATriangle','3,4,5 should be Right')    
    
    def testInvalidInputs(self):
        self.assertEqual(classifyTriangle(201,4,5), 'InvalidInput')
        self.assertEqual(classifyTriangle(-1,4,5), 'InvalidInput')
        self.assertEqual(classifyTriangle(3,0,5), 'InvalidInput')
        self.assertEqual(classifyTriangle(-1, 0, 400), 'InvalidInput')
        self.assertEqual(classifyTriangle(0.1, 2.2, 8), 'InvalidInput')
        
    def testStringInput(self):
        self.assertEqual(classifyTriangle('d', 4, 5), 'InvalidInput')
        self.assertEqual(classifyTriangle(5, "tool", 5), 'InvalidInput')
    

    def testInValidFails(self):
        self.assertNotEqual(classifyTriangle(4, 5, 8), 'InvalidInput')
        self.assertNotEqual(classifyTriangle(3, 4, 5), 'InvalidInput')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

