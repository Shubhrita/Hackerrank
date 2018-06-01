#!/bin/python

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    
    if n >= 3 and n <= 10**7 and m >= 1 and m <= 2*(10^5):
        arr=[]
        for r in range(n):
            arr.append(int(0))

        for q in queries:
            if q != '':
                a=q[0]
                b=q[1]
                c=q[2]
                if  a >= 1 and a <= b and b <= n and c >= 0 and c <= 10**9:
                    a=a-1
                    b=b-1
                    for j in range(a,b+1):
                        arr[j] = arr[j]+c
                    print(arr)
                    
        
        output=0
        
        for a in arr:
            if a>output:
                output=a
            
        return output

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in xrange(m):
        queries.append(map(int, raw_input().rstrip().split()))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
