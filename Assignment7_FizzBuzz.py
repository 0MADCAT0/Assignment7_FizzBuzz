# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 17:30:18 2020

@author: MADCAT
"""




for i in range(1,101):
    
    if i % 3 == 0 and i % 15 != 0:
        print("Fizz")
    elif i % 5 == 0 and i % 15 != 0:
        print("Buzz")
    elif i % 15 == 0:
        print("FizzBuzz")
    else :
        print(i)