#A Circle instance accepts attribute radius (r)
#It has a method area that returns the area (A) of the circle using the formula A=πr2
#It has a method to calculate circumference (c) using the formula C=2πr
import math
class Circle():
    def __init__(self,r):
       self.r=r
    def area(self):
       return 3.14*self.r**2
    
    def circumference(self):
       return 2*3.14*self.r
       
    

