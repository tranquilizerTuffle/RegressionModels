# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 15:19:03 2019

@author: t H u n d e r
"""

import enchant

if enchant.Dict("en_US"):
 print ('yes')
else:
 print ('no')
