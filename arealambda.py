# #Area of Rectangle using Lambda
area=lambda a,b:a*b
l=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
print("Area of Rectangle is:",area(l,b))

# #Area of Square using Lambda
area=lambda a:a*a
n=int(input("Enter the side:"))
print("Area of Square is:",area(n))

#Area of Triangle using Lambda
area=lambda b,h:0.5*b*h
b=int(input("Enter the breadth:"))
h=int(input("Enter the height:"))
print("Area of triangle is:",area(b,h))