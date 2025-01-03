class School:
    pass

class Student(School):
    def __init__(
        self,
        student_id,
        student_name,
        student_f_name,
        student_phone_number,
        student_address,
        student_fees
        ):
        self.student_id = student_id
        self.student_name = student_name
        self.student_f_name = student_f_name
        self.student_phone_number = student_phone_number
        self.student_address = student_address
        self.student_fees = student_fees   

    def getStudent(self):    
        return f"id = {self.student_id},name = {self.student_name},father name = {self.student_f_name},phone number = {self.student_phone_number},address = {self.student_address},fee = {self.student_fees}"     

class Teacher(School):
    def __init__(self,
        teacher_name,
        teacher_f_name,
        teacher_phone_name,
        teacher_salary,
        ):
        self.teacher_name = teacher_name
        self.teacher_f_name = teacher_f_name
        self.teacher_phone_number = teacher_phone_name
        self.teacher_salary = teacher_salary

    def getteacher(self):
        return f" Name: {self.teacher_name}  Father Name: {self.teacher_f_name} Phone Number: {self.teacher_phone_number}"   

class Admin(School):
    pass

class Classrooms(School):
    pass
    
class Event(School):
    def__ init__(self, name,date,manager,time,menu, decoration , required_stock, participates, guests ,location,description):
        self.name = name
        self.date = date
        self.manager = manager
        self.time = time
        self.menu = menu
        self.dectoration = decoration
        self.required_stock = required_stock
        self.participates = participates
        self.guests = guests
        self.location = location
        self.description = description

class Exams(School):
    pass
  
class Stock(School):
    pass
