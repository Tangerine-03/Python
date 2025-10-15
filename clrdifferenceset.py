
a=input("Enter colors for the first list:").split(",")
set1 = set( a)
b=input("Enter colors for the second list:").split(",")
set2 = set( b)
c=set1.difference(set2)
print(c)

