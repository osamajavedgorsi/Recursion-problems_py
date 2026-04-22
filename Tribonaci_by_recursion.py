#Find tribonacci number with application of recursion
num= int(input("Enter any number: "))
def tribonaci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        return tribonaci(n-1) + tribonaci(n-2) + tribonaci(n-3)
    

print(tribonaci(num))
