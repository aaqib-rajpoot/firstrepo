class Classroom:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def get_details(self):
        return f"Classroom Name: {self.name}, Capacity: {self.capacity}"
