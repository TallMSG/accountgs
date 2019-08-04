from application import *

def main():
    while True:
        user_input = input('Введите команду (1 - считать зарплату или 2 - учёт сотрудников): ')
        if user_input == '1':
            application.salary.calculate_salary()
        elif user_input == '2':
            application.db.people.get_employees()
        else:
            print('Такой команды не существует')
        break

if __name__ == '__main__':
    main()