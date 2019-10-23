import pickle
from os import path

class Employee:

    def __init__(self):
        self.__name ='Name'
        self.__employeeID = 'Employee ID'
        self.__department = 'Department'
        self.__title = 'Title'
        self.__salary = 'Salary'

        self.__the_employye_list = {}


#load and save data

    def save_the_list(self, file, dict):

        pickle.dump(dict, open("employee.dat", "wb"))
        print("****The file is saved on HD****")

    def load(self, file):

        endOfTheFile = False

        while not endOfTheFile:
            try:

                self.__the_employye_list = pickle.load(file)
            except EOFError:

                endOfTheFile = True

        file.close()

        return self.__the_employye_list

#functions for setting up the employee data

    def set_name_employye(self, anEmployye_name):
         self.__name = anEmployye_name

    def set_id_employye(self, anEmployye_id):
        self.__employeeID = anEmployye_id

    def set_department_employye(self, an_employye_dept):
        self.__department= an_employye_dept

    def set_title_employye(self, an_employye_title):
        self.__title = an_employye_title

    def set_salary_employye(self, an_employye_salary):
        self.__salary = an_employye_salary

#functions for getting the employee data

    def get_name_employye(self):
         return self.__name

    def get_id_employye(self):
        return  self.__employeeID

    def get_department_employye(self):
        return self.__department

    def get_title_employye(self):
        return self.__title

    def get_salary_employye(self):
        return self.__salary

#adding new Entry in the list and delet it=

    def add_new_employye(self):
        an_name1 = input("Enter the name of an Employee:    ")
        employeeID = input("Enter the Employee ID:  ")
        department = input("Enter the Departemnt:   ")
        title = input("Enter the title of Employee: ")
        salary = input("Enter the Employee salary:  ")

        self.set_name_employye(an_name1)
        self.set_id_employye(employeeID)
        self.set_department_employye(department)
        self.set_title_employye(title)
        self.set_salary_employye(salary)

        while_deciosion = True

        while while_deciosion:
            if an_name1 in self.__the_employye_list:
                print("\n\t****The entry exist in the Database!****\n")
                while_deciosion = False

            else:
                self.__the_employye_list.update({self.get_name_employye(): [self.get_id_employye(),self.get_department_employye(),self.get_title_employye(),self.get_salary_employye()]})
                while_deciosion = False

        return self.__the_employye_list



    def del_entry_in_list(self, an_name):

        if an_name in self.__the_employye_list:
            self.__the_employye_list.pop(an_name)
            print("\n\t\t\t***Done***")
            return True

        else:
            print("\n\t****Name not in the Database!****\n")
            return False


#lookng for Entry in list


    def find_employee_by_name(self, the_name):
        if the_name  in self.__the_employye_list.keys():
            print(self.__the_employye_list[the_name])

        else:
            print("****Not Exist****")
            return False


    def find_employee_by_ID(self, the_employee_ID):
        result = []
        for keywords in self.__the_employye_list.keys():
            if the_employee_ID in self.__the_employye_list[keywords]:
                result.append(keywords)  # This part, we are making list of results
                check = True

                while check :
                    for res in result:  # We are now printing the results
                        print("Founded ID is realated to", res)
                        check = False
                        return
        else:
            print("****Employer not found****")

#display all entryes in the database

    def display_the_list(self,list):
        for name in list:
            print(name, list[name])

    def display_statictic(self):

        key_max = max(self.__the_employye_list.keys(), key=(lambda k: self.__the_employye_list[k]))
        key_min = min(self.__the_employye_list.keys(), key=(lambda k: self.__the_employye_list[k]))

        print('Maximum Value: ', self.__the_employye_list[key_max])
        print('Minimum Value: ', self.__the_employye_list[key_min])
        count = int
        self.__temp_dict = {}

        count = len(self.__the_employye_list.keys())

        self.__temp_dict.update({'\nTotal Employee': count})
        for name in self.__temp_dict:
            print(name, self.__temp_dict[name])





#exiting app
    def exit_app(self):

        exit()