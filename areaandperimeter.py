class Rectangle:
    def getData(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def displayArea(self):
        area=self.length*self.breadth
        print("Area = ",area)
    def displayPerimeter(self):
        perimeter=2 * (self.length + self.breadth)
        print("Perimeter = ",perimeter)
l=int(input("Enter the Length: "))
b=int(input("Enter the Breadth: "))
rect1=Rectangle()
rect1.getData(l,b)
rect1.displayArea()
rect1.displayPerimeter()


