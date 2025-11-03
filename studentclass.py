class student:
    def __init__(self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course
    def displaystudent(self):
        print("Roll Number:",self.rollno)
        print("Name:",self.name)
        print("Course:",self.course)
stud1=student(10,"Mathew","MCA")
stud2=student(11,"Mark","MCA")
stud1.displaystudent()
stud2.displaystudent()