#filter out only odd elements from a list
num=[2,56,33,90,76,11,39]
newlist=list(filter(lambda x: (x%2!=0), num))
print(num)
print(newlist)
