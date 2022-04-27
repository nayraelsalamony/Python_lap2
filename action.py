from employee import Employee
from office import Office
while exit != "q":
    check = input("enter '1' to add  and '2' to show all employee  enter '3' to see one user enter delete '4' to delete user  ").lower()
    if check == '1':
       id =int (input("ID: "))
       name = input("Name: ")
       email = input("Email: ")
       empX = Employee(id,name,5000,"Happy",50,email,"tired" , 50000 , 0)
       Office.Hire(empX)     
    elif check == "2":
        Office.get_all_employees()

    elif check == "3":
        empId = input("enter the user id : ")
        Office.get_employee(empId)

    elif check == "4":
        empId = input("enter the user id : ")
        Office.Fire(empId)   
    
    exit= input("enter “q” to quit  ").lower()