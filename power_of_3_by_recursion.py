#check if the number is power of three or not by applyin recursion
num= int(input("Enter any number: "))
def is_POT(n):
    if n==1:
        return True
    if n%3!=0:
        return False
    elif n<=0:
        return False
    else:
        return is_POT(n//3)
        
    
print(is_POT(num))