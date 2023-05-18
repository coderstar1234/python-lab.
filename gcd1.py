a=int(input("Enter the no a:-"))
b=int(input("Enter the no b:-"))
def hcf(a,b):
    if(b == 0):
            return abs(a)
        else:
            return hcf(b, a % b)
print("The gcd of a and b is : ",end="")
print(hcf(a,b))
