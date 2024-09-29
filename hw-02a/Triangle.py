# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classifyTriangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """
      # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)): #reorganized this snippet to top to prevent conversion errors
        return 'InvalidInput' #removed ;
    
    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
        
    if a <= 0 or b <= 0 or c <= 0: #fixed typo b <=b
        return 'InvalidInput'
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    sides = sorted([a, b, c]) #added sorting function to ensure a, b, and c are assigned correctly
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)): #changed - to +
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b and b == c: #changed b == a to b==c to ensure all sides are equal
        return 'Equilateral'
    elif ((a**2) + (b**2)) == (c**2): #changed * to **
        return 'Right'
    elif (a != b) and  (b != c) and (a != c): #changed a !=b to a != c to ensure all sides are NOT equal
        return 'Scalene'
    else:
        return 'Isosceles' #typo of Isosceles corrected
