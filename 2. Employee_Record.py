# Data Model For Employee
class Employee:
    def __init__(self, emp_name, emp_id, age, department, position, manager_id=None):
        self.Name = emp_name
        self.Id = emp_id
        self.Age = age
        self.Department = department
        self.Position = position
        self.Manager = manager_id

# Data Management System
class EmployeeManagement:
    def __init__(self):
        self.employees = {}
    
    def show(self):
        print("\n Employee Details :")
        for id, emp in self.employees.items():
            print(f"\nEmployee ID: {id}")
            print(f"Name: {emp.Name}")
            print(f"Age: {emp.Age}")
            print(f"Department: {emp.Department}")
            print(f"Position: {emp.Position}")
            print(f"Manager ID: {emp.Manager}")
            print("--------------------")
 
    def add_employee(self, name, id, age, dep, pos, man_id=None):
        if id in self.employees:
            print(f"Employee ID {id} already exists.")
        elif man_id and self.check_circular_reference(id):
            print("Circular reference detected. Cannot add employee.")
        else:
            self.employees[id] = Employee(name, id, age, dep, pos, man_id)
            print(f"Employee {name} added successfully.")



    def update_employee(self, id):
        if id not in self.employees:
            print("Employee with the given ID does not exist.")
            return
        
        print("Enter new details:")
        name = input("Name: ")
        age = int(input("Age: "))
        dep = input("Department: ")
        pos = input("Position: ")
        man_id = input("Manager ID: ")
        
        self.employees[id] = Employee(name, id, age, dep, pos, man_id)

    def delete_employees(self, id):
        if id in self.employees:
            print(f"Employee {self.employees[id].Name}, Position {self.employees[id].Position} is Deleted.")
            del self.employees[id]
            
        else:
            print("Employee with the given ID does not Exist.")
    
    # - Implement search functionality based on different criteria (name, department, etc.).
    def search(self, **kwargs):
        result = []
        for id, emp in self.employees.items():
            for key, val in kwargs.items():
                if getattr(emp, key) == val:
                    result.append(emp)
                    break 
        return result
    
    # - Display reporting hierarchy of employees.
    def hierarchy(self, emp_id, level=0):
        if emp_id not in self.employees:
            print("No Employee found with Given Employee ID")
            return
        emp = self.employees[emp_id]
        print("    " * level, f"{emp.Name} ({emp.Position})")

        sub = [i for i in self.employees.values() if i.Manager == emp_id]
        for s in sub:
            self.hierarchy(s.Id, level+1)

# - Handle edge cases such as circular references in the reporting structure.
    def check_circular_reference(self,emp_id):
        visited = set()
        current = emp_id
        while current:
            if current in visited:
                return True
            visited.add(current)
            current = self.employees.get(current)
            if current:
                current = current.Manager
            else:
                break
        return False


emp = EmployeeManagement()
proceed = True

while proceed:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Update Employee")
    print("3. Delete Employee")
    print("4. Show All Employees")
    print("5. Search Employee")
    print("6. Display Hierarchy")
    print("7. Exit\n")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter employee name: ")
        id = input("Enter employee ID: ")
        age = input("Enter employee age: ")
        dep = input("Enter employee department: ")
        pos = input("Enter employee position: ")
        man_id = input("Enter manager ID: ")
        
        emp.add_employee(name, id, age, dep, pos, man_id)
    
    elif choice == '2':
        id = input("Enter employee ID to update: ")
        emp.update_employee(id)
    
    elif choice == '3':
        id = input("Enter Employee ID to Delete: ")
        emp.delete_employees(id)

    elif choice == '4':
        emp.show()
    
    elif choice == '5':
        criteria={}
        print(": Enter Search Criteria (Leave Blank To Skip) : ")
        name = input("Name : ")
        if name:
            criteria['Name'] = name
        id = input("Emp_ID : ")
        if id:
            criteria["Id"] = id
        age = input("Age : ")
        if age:
            criteria["Age"] = age
        dep = input("Department : ")
        if dep:
            criteria["Department"] = dep
        pos = input("Position : ")
        if pos:
            criteria["Position"] = pos
        manager = input("Manager : ")
        if manager:
            criteria["Manager"] = manager

        results = emp.search(**criteria)
        if not results:
            print("No Employee Matched")

        print("\nEmployees Found :")
        for employee in results:
            print(f"NAME : {employee.Name}, ID : {employee.Id}, AGE : {employee.Age}, DEPARTMENT : {employee.Department}, POSITION : {employee.Position}, Manager = {employee.Manager}")


    elif choice == '6':
        id = input("Enter a Employee ID to show Hierarchy")
        emp.hierarchy(id)

    elif choice == '7':
        proceed = False

    else :
        print("Wrong input! Choose a Valid Option.\n")
# emp.add_employee("MD", 'BOSS', '22', "MANAGEMENT", 'CEO')
# emp.add_employee("Dhanasekaran", '01', '22', "Data", 'Data Scientist','BOSS')
# emp.add_employee("Annamalai", '02', '21', "analyst", 'Social Media', 'EMP-03')
# emp.add_employee("kutty", 'EMP-01', '21', "Data", 'Data Scientist', '01')
# emp.add_employee("alpha", 'EMP-02', '22', "Data", 'Data Scientist', '01')
# emp.add_employee("xs", 'EMP-01', 22, "Data", 'Data Scientist', 'BOSS')
# emp.add_employee("Romi", 'EMP-03', 25, 'CG', 'VFX Artist', 'BOSS')
# emp.add_employee('bot', '2', '22', 'dt', 'Developer', '3')
# emp.add_employee('circular', '1', '22', 'dt', 'Developer', '2')
# emp.add_employee('circular 2', '3', '22', 'dt', 'Developer', '1')
# emp.hierarchy('BOSS')