#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 13:55:20 2020

@author: carter
"""

class Calculator:
    """
    A class that acts like a calculator
    value = the current calculator value
    """
    def __init__(self,value = 0):
        self.value = value

    """Addition: self.value + num"""
    def add(self, num):
        self.value += num
        return self.value

    """Subtraction: self.value - num"""
    def sub(self, num):
        self.value -= num
        return self.value

    """Multiplication: self.value * num"""
    def mul(self, num):
        self.value *= num
        return self.value

    """Divide: self.value / num"""

    def div(self, num):
        self.value /= num
        return self.value

    """Clr: Clear the current value"""
    def clr(self):
        self.value = 0
        return
    """Print the result"""
    def result(self):
        return self.value

        """ Sup dude - Anthony"""
