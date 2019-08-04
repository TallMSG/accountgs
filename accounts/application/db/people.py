class Employee:

    def __init__(self, name, employee_id, department, title):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.title = title

    def __str__(self):
        return '{} , id={}, is in {} and is a {}.'.format(self.name, self.employee_id, self.department, self.title)


def get_employees():

    # Create three employee objects
    emp1 = Employee(name='Susan Meyers', employee_id='47899', department='Accounting', title='Vice President')
    emp2 = Employee(name='Mark Jones', employee_id='39119', department='IT', title='Programmer')
    emp3 = Employee(name='Joy Rogersr', employee_id='81774', department='Manufacturing', title='Engineer')

    print(emp1, sep='/n/n')
    print(emp2, sep='/n/n')
    print(emp3, sep='/n/n')

if __name__ == '__main__':
    get_employees()