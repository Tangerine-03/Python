numbers=[1,2,3,4,5,6]
sum=0
for item in numbers:
    sum=sum+item
print("The Sum is:",sum)

#External Input
n=list(map(int,input("Enter the numbers:").split(",")))
sum=0
for item in n:
    sum=sum+item
print("The Sum is:",sum)
