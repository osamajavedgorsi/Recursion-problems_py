# Recursion-problems_py
solved two problems with recursion method.
## problem 1: Find n-th Tribonacci number by recursion method
Definition: A Tribonacci number is a sequence of integers where each number is the sum of the three preceding ones, starting from 0,1,1 
First of all we take a number as an input, to find user given tribonacci number.
Then we created a function tribonaci(n) that has n parameter
it has three base cases:
  if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 1
these base cases help to calculate recursive conditions properly
The recursive condition has following logic:
  return tribonaci(n-1) + tribonaci(n-2) + tribonaci(n-3)
It calls tribonaci() function three times making a recursive tree. function call keep happening until the base condition is met. then in the end the final answer is returned and printed outside the function by print statement giving num argument
print(tribonaci(num))


## problem 2: Check whether the given number is power of 3 by applying recursion method
The program takes an input from user
it defines a function is_POT(n) with three base cases
  if n==1:
        return True #if n is 1 then n is power of three
    if n%3!=0:
        return False #if remainder of n/3 is not 0, it means it is not divisible by 3 hence can't be power of 3
    elif n<=0:
        return False #any value equal or less than 0 can't be power of three

then the recursive method 
  return is_POT(n//3)
The recursive method keeps dividing n until it fulfils one of the above base cases, so in the very end, it will tell if n is constantly being divisible or not. if not the function will return false, if yes the function will return true.
