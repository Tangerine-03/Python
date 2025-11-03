class employee:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def displayemployee(self):
        print("Name:",self.name)
        print("ID:",self.id)
        print("Salary:",self.salary)
emp1=employee("Thomas",1011,80000)
emp2=employee("Philip",1012,80000)
emp1.displayemployee()
emp2.displayemployee()