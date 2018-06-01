# Finding duplicate elements in an array


# Importing required libraries

from __future__ import print_function

import sys


# Taking input line by line

inp=[]
raw=0
while raw != '':
    try:
        raw = raw_input()
        inp.append(raw)
    except (EOFError):
        break #end of file reached


# Function to find duplicate in an array

def find_dup(arr):
    dup=[]
    new_list=[]
    for r in arr:
        if r not in new_list:
            new_list.append(r)
        else:
            dup.append(r)
            
    return dup


# Passing array to function to find duplicates

for i in range(int(inp[0])):
    passed = inp[2].split(' ')
    result = find_dup(passed)
    if result != []:
        for r in result:
            print(r,file=sys.stdout)
    else:
        print(-1,file=sys.stdout)


