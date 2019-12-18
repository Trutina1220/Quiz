data = open("Data.txt",'rt',encoding="utf-8").read()
split_data = data.split('.\n')
employees = []
for line in split_data:
    employees.append(line.split(','))
the_sorted_employee =sorted(employees)
# print(employee[0][0]) #accesing the precise data
# def data():
#     for employee in the_sorted_employee:
#         print(employee)
# data()

class ManagingApplication:
    def __init__(self,id:str='',name:str='',position='',salary:int=0):
        self.id = id
        self.name=name
        self.position=position
        self.salary = salary
    def data():
        for employee in the_sorted_employee:
            print(employee)
    def input_choice():
        print("1.New Staff")
        print("2.Delete Staff")
        print("3.Summary Data\n4.Save&Exit")
        the_input = input(str("Input Choice:"))
        # while the_input != "4":
        #     the_input = input(str("Input Choice:"))
        if the_input == "1":
            id = input(str("Input ID[SXXXX]:"))
            name = input(str("Input Name[0...20]:"))
            position = input(str("Input Position[Staff,Officer,Manager]:"))
            salary = int(input("Input Salary for "+position+":"))
            new_employee =[]
            new_employee.append(id)
            new_employee.append(name)
            new_employee.append(position)
            new_employee.append(salary)
            the_sorted_employee.append(new_employee)
            ManagingApplication.data()
        if the_input == "2":








ManagingApplication.data()
ManagingApplication.input_choice()
