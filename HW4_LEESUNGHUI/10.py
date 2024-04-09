class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def getName(self):
        print(self.name)
        
    def getAge(self):
        print(self.age)
    
class Employee(Person):
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.employeeID = id
        
    def getEmployeeID(self):
        print(self.employeeID)
    
    def getInfo(self):
        self.getName()
        self.getAge()
        self.getEmployeeID()
        
em = Employee("IoT", 65, 2018)
em.getInfo()