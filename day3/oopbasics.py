# let's start with oop basics


class User: 
    company = "Microslop"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, I am {self.name}"

    def __str__(self):
        return f"User(name={self.name}, age={self.age})"


u1 = User("Amit", 25)
u2 = User("Ravi", 35)

print(u1)
print(u2)

# Inheritence


class Employee(User):
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self.emp_id = emp_id
