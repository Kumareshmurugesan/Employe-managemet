from branch import *
from emp import *

while True:
    print("1.Insert Employee Data :")
    print("2.View View Data")
    print("3.Delete Employee Data")
    print("4.Insert Branch Data")
    print("5.View Branch Data ")
    print("6.Delete Branch Data")
    print("7.Emp details")
    print("8.Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        emp_id = input("Enter Emp_id :")
        ename = input("Enter Emp_name: ")
        job = input("Enter your Emp_Job: ")
        salary = input("Enter Emp_salary: ")
        insert_emp(ename,job,salary,emp_id)
    elif choice == 2:
        get_all_emp()
    elif choice == 3:
        emp_id = input("Enter the id to delete: ")
        delete_emp(emp_id)
    elif choice == 4:
        br_id = input("Enter Branch_id :")
        br_name = input("Enter Branch name : ")
        address = input("Enter address :")
        insert_branch(br_id, br_name,address)
    elif choice == 5:

        get_all_branch()
    elif choice == 6:
        br_id = input("Enter branch_id: ")
        delete_branch(br_id)
    elif choice == 7:
        branch_id = input("enter emp_id :")
        get_emp_details(branch_id)

    elif choice == 8:
        quit()
    else:
        print("Invalid Selection. Please try again")