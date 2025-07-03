class Employee:
    cname="lpu"
    def __init__(self,name,age,salary):
        self.name=name #public variable
        self._age=age #protected variable
        self.__salary=salary #private variable
    def display(self):
        print(self.__salary)
        print(self._age)
e1=Employee("john",25,50000)
e1.display()
print(e1._age)