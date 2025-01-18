import student,teacher,trade,event,exam,admin,stock

Ali = student.Student(1,"Ali","Usman","None","None","1000")
StudentRecord = Ali.getStudent()
print(StudentRecord)


Aqib = teacher.Teacher("Aaqib","Amir","None","50,000")
TeacherRecord = Aqib.getteacher()
print(TeacherRecord)

Amir = admin.Admin("Amir","Akram","Aslam","Akhter","Asif")
AdminRecord = Amir.getAdmin()
print(AdminRecord)
