list1=list(map(int, input("Enter numbers:").split(",")))
print("The list is:",list1)
list2=[]
for i in list1:
    if(i%2==0):
        continue;
    list2.append(i)
print("The list of Odd numbers:",list2)
