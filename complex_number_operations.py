# Author: Weijia Fang
# Title: complex_number_operations.py
# Completion Date: Sep 2019

class Complex:    
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    #A function deal with adding 
    def __add__(self,other):
        #Seperate the object to 2 parts(realpart and imagpart) and deal with them seperately
        realpart = self.real + other.real 
        imagpart = self.imag + other.imag
        result = Complex(realpart,imagpart)
        return result #return an object

    #A function deal with subtracting
    def __sub__(self,other):
        realpart = self.real - other.real
        imagpart = self.imag - other.imag
        result = Complex(realpart,imagpart)
        return result

    #A function deal with multiplying 
    #Used the equation: (x+yi)(u+vi) = (xu-yv)+(xv+yu)i
    def __mul__(self,other):
        realpart = self.real * other.real - self.imag * other.imag
        imagpart = self.real * other.imag + self.imag * other.real
        result = Complex(realpart,imagpart)
        return result  

    #A function deal with number times object
    def __rmul__(self,other):
        realpart = self.real * other.real - self.imag * other.imag
        imagpart = self.real * other.imag + self.imag * other.real
        result = Complex(realpart,imagpart)
        return result  
    
    #A function deal with output without ()
    def __str__(self):
        if self.imag < 0: #If the imagary part is less than 0, return itself
            return str(self.real) + str(self.imag) + 'i'
        else: #If the imagary part is greater or equal to 0, use the plus sign to connect the real number part and the imagary number part
            return str(self.real) +'+'+ str(self.imag) + 'i'

    #A function deal with string outout with the format (a, bi)
    def __repr__(self):
        return '(' + str(self.real) + ', ' + str(self.imag) + 'i' + ')'

    #A function deal with conjugate
    @property #change the def to a property
    def conjugate(self):
        realpart = self.real  #real part stay the same      
        imagpart = self.imag * (-1) #times -1 to get the conjugate
        result = Complex(realpart,imagpart)
        return result

    #A function deal with comparison
    def __eq__(self,other):
        if self.real == other.real and self.imag == other.imag:
            return True
        else:
            return False
