from application.people import get_employees
from application.salary import calculate_salary
from datetime import datetime


def main():
    while True:
        x = int(input('input 1 for get_employees, input 2 for calculate_salary, 3 for exit: '))
        if x == 1:
            get_employees()
            print(datetime.now().date())
        elif x == 2:
            calculate_salary()
            print(datetime.now().date())
        elif x == 3:
            print('Goodbye!')
            break


if __name__ == '__main__':
    main()
