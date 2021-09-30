class Employee:
    # Create holders for total employees and combined salaries
    num_employ = 0
    total_salary = 0
    # Constructor that takes in values and adjusts the employ# and total salary
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department  
        Employee.num_employ += 1
        Employee.total_salary += self.salary
    # Returns the avg salary of all workers
    def avg_salary():
        return Employee.total_salary / Employee.num_employ
        
# Subclass that enherits all attributes from employees
class Full_Time(Employee):
    pass

# Create instances of both Employee and Full time
jim = Employee("Chris", "Munns", 50000, 5)
jam = Employee("Alex", "Smith", 20000, 5)
ram = Full_Time("Rachel", "Doctor", 60000, 4)
sam = Full_Time("Samantha", "Nori", 100000, 2)


# Print results
print(Employee.num_employ)
print(Employee.total_salary)
print(Employee.avg_salary())
