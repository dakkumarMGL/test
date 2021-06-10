#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 20:11:14 2021

@author: arunkumar
"""


mydict = {1:['a', 'b', 'c'], 2:['d', 'e', 'f']}
#mydict = {}

mykeys = []
for key in mydict.keys():
    mykeys.append(key)
    
print('bool(mydict) = ', bool(mydict))
