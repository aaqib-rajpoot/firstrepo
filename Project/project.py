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
        student_fees,
        student_trade_name
        ):
        self.student_id = student_id
        self.student_name = student_name
        self.student_f_name = student_f_name
        self.student_phone_number = student_phone_number
        self.student_address = student_address
        self.student_fees = student_fees
        self.student_trade_name = student_trade_name    

    def getStudent(self):    
        return f"id = {self.student_id},name = {self.student_name},father name = {self.student_f_name},phone number = {self.student_phone_number},address = {self.student_address},fee = {self.student_fees},exams = {self.student},classname = {self.student_trade_name}"     

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
    def __init__(self, FDO, vice_principal, cashier, principal, admin):
        self.FDO = FDO
        self.vice_principal = vice_principal
        self.cashier = cashier
        self.principal= principal
        self.admin = admin
    def getStudent(self):
        return f"FDO = {self.FDO},vice principal = {self.vice_principal},cashier = {self.cashier},principal = {self.principal},admin = {self.admin},"

class Classrooms(School):
    def__init__(self, class_name, class_teacher, class_room, num_of_students):
      self.class_name = class_name
      self.class_teacher = class_teacher
      self.class_room = class_room
      self.num_of_students = num_of_students
    def getclassroom(self):
        return f"class_name = {self.class_name}, class_teacher ={self.class_teacher}, class_room ={self.class_room}, num_of_students ={self.num_of_students}"        
    
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
    def __init__(self, name, quantity, price_per_item, category, supplier):
        self.name = name
        self.quantity = quantity
        self.price_per_item = price_per_item
        self.category = category 
        self.supplier = supplier
    def get(self):
        total_value = self.quantity * self.price_per_item
        return {
            "name": self.name,
            "quantity": self.quantity,
            "price_per_item": self.price_per_item,
            "total_value": total_value,
            "category" : self.category,
            "supplier": self.supplier
        }
