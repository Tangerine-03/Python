#Factorial using Recursive Function
def fact(n):
    if n==1:
        return 1
    else:
        return(n*fact(n-1))
num=int(input("Enter the number:"))
if num>=1:
    print("The Factorial of",num,":",fact(num))