# Hackerrank
Code1 - Calculating Pearson Coefficient of Correlation between 2 score lists

Code2 - 

Hacker has a duplicate brother tracker. Tracker gave him an array containing elements with the task to track the duplicate elements. Tracker loves memory and time. He wants hacker to do it as efficiently as possible.

Input Format

Input begins with an integer T, the number of test cases. Each test case begins with an integer N, the number of elements in array. N digits of the array follow.

Constraint: 1

Output Format

Print all the duplicate elements. Output -1 when no repeating elements are found.

Sample Input

1
7
1 2 3 1 3 6 6

Sample Output

1
3
6

Explanation

1 3 6 are the repeating elements


Code3 - 

Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in your array.

For example, the length of your array of zeros . Your list of queries is as follows:

    a b k
    1 5 3
    4 8 7
    6 9 1
Add the values of  between the indices  and  inclusive:

idx	 1 2 3  4  5 6 7 8 9 10
	[0,0,0, 0, 0,0,0,0,0, 0]
	[3,3,3, 3, 3,0,0,0,0, 0]
	[3,3,3,10,10,7,7,7,0, 0]
	[3,3,3,10,10,8,8,8,1, 0]
The largest value is  after all operations are performed.

Function Description Complete the function arrayManipulation in the editor below. It must return an integer, the maximum value in the resulting array.

arrayManipulation has the following parameters:

n - the number of elements in your array
queries - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.
Input Format

The first line contains two space-separated integers  and , the size of the array and the number of operations. 
Each of the next  lines contains three space-separated integers ,  and , the left index, right index and summand.

Constraints

Output Format

Return the integer maximum value in the finished array.
