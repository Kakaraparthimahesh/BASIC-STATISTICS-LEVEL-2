# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 22:59:01 2022

@author: MAHESH
"""

from scipy.stats import norm
nd=norm(45,8)#maean,sd
x1 = nd.cdf(50) 
1-nd.cdf(50)

# x1
# Output:0.26598552904870054