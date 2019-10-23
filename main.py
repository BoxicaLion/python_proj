from employe import Employee
import pickle
import os

def main():
    obj = Employee()

    exists = os.path.isfile('employee.dat')

    if exists:
        the_file = open('employee.dat', 'rb')
        the_employye_list = {}
        the_employye_list = obj.load(the_file)

        the_file.close()

    else:
        the_employye_list = {}


    decision = True

    while decision:

        print("\n\t\t\t<-- Menu -->")
        print("<-- Please type the menu number -->\n")

        print(" -> 1:   Add an Employee \n"
                              " -> 2:   Find an Employee (By Name)\n"
                              " -> 3:   Find an Employee (By EID)\n"
                              " -> 4:   Delete an Employee\n"
                              " -> 5:   Display Statistics\n"
                              " -> 6:   Display All Employees\n"
                              " -> 7:   Exit\n")
        menu_decision = input()

        if menu_decision == "1":
            decision_2 = True
            while decision_2:
                the_employye_list.update(obj.add_new_employye())

                quiestion = input("Would u like to ad another Entry?: Y/N\n")

                if quiestion.lower() == "n":
                    decision_2 = False


        if menu_decision == "2":
            decision3 = True
            while decision3:
                by_name = input("What name u looking for?: ")
                obj.find_employee_by_name(by_name)

                quiestion2 = input("Would u like to ad another search?: Y/N\n")

                if quiestion2.lower() == "n":
                    decision3 = False


        if menu_decision == "3":
            decision3 = True
            while decision3:
                by_ID = input("What ID u looking for?: ")
                obj.find_employee_by_ID(by_ID)
                quiestion2 = input("Would u like to ad another search?: Y/N\n")
                if quiestion2.lower() == "n":
                    decision3 = False

        if menu_decision == "4":
            delete_name = input("What name u would like to delete?: ")
            obj.del_entry_in_list(delete_name)

        if menu_decision == "5":
            obj.get_department_employye()
            obj.display_statictic()

        if menu_decision == "6":
            obj.display_the_list(the_employye_list)
            none = input("Next-->")
            del none

        if menu_decision == "7":
            decision = False
            pickle.dump(the_employye_list, open("employee.dat", "wb"))
            print("****The file is saved on HD****")


main()