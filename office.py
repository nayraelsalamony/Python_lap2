import MySQLdb
from employee import Employee
class Office:
    db = MySQLdb.connect("localhost", "root", "nayra", "python")
    cursor = db.cursor()

    def __init__(self, name, employees):
        self.name = name
        self.employees = employees
    
    def get_all_employees():
        Office.cursor.execute("SELECT * FROM python.employee")
        data = Office.cursor.fetchall()
        for emp in data :
            print(emp[0])
            print(emp[1])

    
    def get_employee(empId):
        Office.cursor.execute(f'SELECT * FROM python.employee where idemployee="{empId}"')
        data = Office.cursor.fetchone()
        print(data)


    
    def Hire(Employee):
        Office.cursor.execute(f'insert into employee (idemployee,name,email,is_manager) values ("{Employee.ID}","{Employee.full_name}" , "{Employee.email}" , "{Employee.is_manager}")')
        Office.db.commit()
        print("inserted")

    
    def Fire(empId):
        Office.cursor.execute(f'delete from employee where idemployee= "{empId}"')
        Office.db.commit()
        print("deleted ")