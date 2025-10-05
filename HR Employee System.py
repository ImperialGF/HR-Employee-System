import re
import random

class Employee:
    def __init__(self, id_empl, fio, post, salary, age):
        self.id = id_empl
        self.fio = fio
        self.post = post
        self.salary = salary
        self.age = age

    def __str__(self):
        return f"{self.id}. {self.fio}, возраст: {self.age}, должность: {self.post}, зарплата: {self.salary} рублей"


class HRSystem:
    def __init__(self):
        self.system = []

    def add(self, employee):
        self.system.append(employee)

    def delete(self, id_empl):
        for employee in self.system:
            if employee.id == id_empl:
                self.system.remove(employee)

    def find(self, string):
        i = 0
        for employee in self.system:
            if employee.fio == string or employee.post == string:
                i += 1
                print(f"{employee}")
        if i == 0:
            print("Сотрудник не найден")

    def all_empl(self):
        k = 0
        while k != -1:
            k = 0
            for i in range(1, len(self.system)):
                if self.system[i].salary > self.system[i-1].salary:
                    v = self.system[i]
                    self.system[i] = self.system[i-1]
                    self.system[i-1] = v
                    k += 1
            if k == 0:
                k = -1
        for employee in self.system:
            print(f"{employee}")

    def statistic(self):
        av_salary = 0
        av_age = 0
        max_salary = 0
        min_salary = 99999999
        count = 0
        for employee in self.system:
            av_salary = av_salary + employee.salary
            av_age = av_age + employee.age
            count += 1
            if employee.salary > max_salary:
                max_salary = employee.salary
            if employee.salary < min_salary:
                min_salary = employee.salary
        print(f"Средняя зарплата: {av_salary/count}; Максимальная зарплата: {max_salary}; Минимальная зарплата: {min_salary}; Средний возраст: {av_age/count}")

    def id_gen(self, id_empl):
        count = 0
        for employee in self.system:
            if employee.id == id_empl:
                count = 1
        if count == 1:
            return True
        else:
            return False

    def exit(self):
        string = ''
        for employee in self.system:
            string = string + f"{employee.id};{employee.fio};{employee.post};{employee.salary};{employee.age}\n"
        return string



system = HRSystem()
with open("employees.txt", "r", encoding="utf-8") as f:
    for line in f:
        sp = re.split(r";", line.strip())
        system.add(Employee(int(sp[0]), sp[1], sp[2], int(sp[3]), int(sp[4])))


exit = False
while exit == False:
    print("~Центр управления действиями~")
    print("============================")
    print("1. Добавить нового сотрудника")
    print("2. Удалить сотрудника по id")
    print("3. Поиск по ФИО\Должности")
    print("4. Показать всех сотрудников")
    print("5. Статистика")
    print("0. Выход\n")

    choise = input("Введите номер действия: ")

    if choise == "1":
        id_empl = random.randint(100000, 999999)
        while system.id_gen(id_empl):
            id_empl = random.randint(100000, 999999)    
        fio = input("Введите ФИО: ")
        post = input("Введите должность: ")
        salary = int(input("Введите зарплату: "))
        age = int(input("Введите возраст: "))
        system.add(Employee(id_empl, fio, post, salary, age))
        print("Сотрудник успешно добавлен в систему")
        print("\n")
        
    elif choise == "2":
        id_empl = int(input("Введите id для удаления: "))
        system.delete(id_empl)
        print("Сотрудник успешно удален из системы")
        print("\n")
        
    elif choise == "3":
        string = input("Введите ФИО или должность для поиска: ")
        system.find(string)
        print("\n")

    elif choise == "4":
        system.all_empl()
        print("\n")

    elif choise == "5":
        system.statistic()
        print("\n")

    elif choise == "0":
        print("Завершение работы системы")
        with open("employees.txt", "w", encoding="utf-8") as f:
            f.write(system.exit())
        exit = True
    else:
        print("Некорректный ввод, попытайтесь снова")
        print("\n")



        
