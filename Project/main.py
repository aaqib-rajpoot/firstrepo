import student,teacher,admin,event,exam,trade,stock

Ali = student.Student(1,"Ali","Usman","None","None","1000")
StudentRecord = Ali.getStudent()
print(StudentRecord)


Aqib = teacher.Teacher("Aaqib","Amir","None","50,000")
TeacherRecord = Aqib.getteacher()
print(TeacherRecord)

Amir = admin.Admin("Amir","Akram","Aslam","Akhter","Asif")
AdminRecord = Amir.getAdmin()
print(AdminRecord)

TeacherDay = event.Event("TeacherDay","Five,October,2025","Zain","8:00 AM","Cakes","Colddrink,Biscuits,Nimco","Students,Teachers","Deo","eabschool")
EventRecord = TeacherDay.getEvent()
print(EventRecord)

Exam = exam.Exams("Umar","Zerotwoninefourtwosix","threehundredfiftysix","fivehundredfifty","Allcleared","Fifteen,January,2025")
ExamRecord = Exam.getExams()
print(ExamRecord)
