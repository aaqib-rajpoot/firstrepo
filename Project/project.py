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
    pass

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

stock_item1 = stock("chairs", 100, 50, "furniture", "furniture world")
stock_item2 = stock("Ball Pens", 300, 20, "stationry", "reyanolds")
stock_item3 = stock("books", 300, 500, "textbooks", "oxford")
stock_item4 = stock("fans" , 20 , 2000, " Electrical Appliances"," local electrical stores")
stock_item5 = stock("Water Dispenser", 5, 15000, "Electrical Appliances", "blue star")

print(stock_item1.get())
print(stock_item2.get())
print(stock_item3.get())
print(stock_item4.get())
print(stock_item5.get())



