
# coding: utf-8

# In[1]:

#Importing Required Libraries

import math

# Calculating Pearson Coefficient

def PearsonCoefficient(x,y):
    N=len(x)
    xy=[a*b for a,b in zip(x,y)]
    x2=[]
    y2=[]
    for i in x:
        x2.append(i ** 2)
    for i in y:
        y2.append(i ** 2)
        
    sumxy=sum(xy)
    sumx2=sum(x2)
    sumy2=sum(y2)
    sumx=sum(x)
    sumy=sum(y)
    r=((N*sumxy)-(sumx*sumy))/math.sqrt(((N*sumx2)-(sumx)**2)*(((N*sumy2)-(sumy)**2)))
    print("%.2f" % r)
    
    
x=input('Enter 1st set of Scores: ')
y=input('Enter 2nd set of Scores: ')
PearsonCoefficient(x,y)


# Pearson Coefficient Calculation using scipy

#Importing & Exporting Required Libraries

get_ipython().system(u'pip install scipy')
import scipy
from scipy import stats
from decimal import *

TWOPLACES = Decimal(10) ** -2
a,b = scipy.stats.pearsonr(x, y)
var=(Decimal(a),Decimal(b))
print(var[0].quantize(TWOPLACES))


# In[ ]:



