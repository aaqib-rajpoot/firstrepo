class School:
    pass

class Student(School):
    pass

class Teacher(School):
    pass

class Admin(School):
    pass

class Classrooms(School):
    pass

# Hina 
class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade

class Teacher:
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject

class Classroom:
    def __init__(self,name):
        self.name=name
        self.student=[]
        self.teacher=None

    def add_student(self,student):
        self.student.append(student)

    def assign_teacher(self,teacher):
        self.teacher=teacher

    def display_classroom(self):
        print(f"Classroom:{self.name}")
        print(f"Teacher:{self.teacher.name}({self.teacher.subject})")
        print("Students:")
        for student in self.students:
            print(f"{student.name} ({student.age})- Grade {student.grade}")


def main():
    #Create students
    student1=Student("Zeeshan",12,7)
    student2=Student("Rehman",11,6)

    #Create teacher
    teacher=Teacher("Ms.Uzma","chemistry")
    
    #Create classroom
    classroom=Classroom("Chemistry Class")

    #Add students to classroom
    classroom.add_student(student1)
    classroom.add_student(student2)

    #Assign teacher to classroom
    classroom.assign_teacher(teacher)

    #Display classroom
    classroom.display_classroom()

if __name__=="__main__":
    main()
