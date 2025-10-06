##Hybrid_inheritance.py
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_details(self):
        return(f'My name is {self.name} and my age is {self.age}')
class employee(person):
    def __init__(self, name, age,id):
        super().__init__(name, age)
        self.id=id
    def showEmployeeDetails(self):
        print(f'{super().display_details()} and my empid is {self.id}')
class work:
    def work(self):
        print("I am Working:")
class manager(person,work):
    def __init__(self, name, age,id,depart):
        super().__init__(name, age)
        self.department=depart
        self.id=id
    def work(self):
        print("Managing Team")
    def display_details(self):
        print(f"name:{self.name}\n age:{self.age} \n id:{self.id} \n departemnt:{self.department}")
o=manager("Ganesha",19,23,'CSE')
o.work()
o.display_details()
work.work(o)
