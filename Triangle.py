# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 16:11:53 2024

@author: njkat
"""
class classify_triangle:
    # Sort the sides to simplify the logic (so a, b, and c don't have to be in order)
    def __init__(self, s1, s2, s3):
        sides = sorted([s1, s2, s3])
        self.a = sides[0]
        self.b = sides[1]
        self.c = sides[2]
        # Check triangle inequality
    
    def is_A_Triangle(self):
        return ((self.a - self.b) < self.c and self.c < (self.a + self.b))
            
 
    def triangle_Type(self):
        # Determine type of triangle
        if(not self.is_A_Triangle()):
            return "Not a Triangle"
        else:
            Right = ""
            if self.is_right_triangle():
                Right = " and Right"
            if self.a == self.b == self.c:
                return "Equilateral" + Right
            elif self.a == self.b or self.b == self.c or self.a == self.c:
                return "Isosceles" + Right
            else:
                return "Scalene" + Right
        
    def is_right_triangle(self):
        # Check if it's a right triangle
       return (self.a**2 + self.b**2 == round(self.c**2, 2))
          
