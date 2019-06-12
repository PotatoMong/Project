#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 09:48:48 2019

@author: samcho
"""
import pandas
import matplotlib
import numpy
b=[ "SepalLen","SepalWid","PetalLen","PetalWid","Class"]
a=pandas.read_csv("/Users/samcho/Documents/GitHub/Project/iris.data", header=None)

c=pandas.read_csv("/Users/samcho/Documents/GitHub/Project/iris.data", header=None,names=b)

"makes a new file called fi, w means write, and it puts c into it."
with open("fi.txt","w") as file:
    file.write(str(c))

print(c)
"""tabs->4spaces"""

"this bit filters out all but the rows with virginica"
d=c[c["Class"]=="Iris-virginica"]

print(d)
"flowers with sepal less than 3.2"
e=c[c["SepalWid"]<=3.2]
print(e)


"flowers with petal length more than 5.1"
f=c[c["PetalLen"]>=5.1]
print(f)
