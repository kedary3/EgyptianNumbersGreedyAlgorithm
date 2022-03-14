# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 13:57:20 2022

@author: Kedar
"""
import numpy as np
import fractions as fr
def GreedyEgyptianNum(x,y):
    if x==0:
        return "MAX denom reached"
    if x==1 or y%x==0:
        return fr.Fraction(x,y).limit_denominator()
    else:
        num = (-1*y)%x
        den = y*np.ceil(y/x)
        return fr.Fraction(1/np.ceil(y/x)).limit_denominator(),GreedyEgyptianNum(fr.Fraction(num/den).limit_denominator()._numerator,fr.Fraction(num/den).limit_denominator()._denominator)
print(GreedyEgyptianNum(31,311))