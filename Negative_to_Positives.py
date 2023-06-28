"""
Please write a program that asks the user for a positive integer N. The program then prints out all numbers between -N and N inclusive, but leaves out the number 0. Each number should be printed on a separate line.

An example of expected behavior:

Sample output
Please type in a positive integer: 4
-4
-3
-2
-1
1
2
3
4

"""

n = int(input("Please type in a positive integer:"))

for i in range(-n, 0, 1):  ### code for printing -n to 0
    print(i)

for i in range(1, n+1, 1): ### codes for printing 0 to n
    print(i)
