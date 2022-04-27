from logging import raiseExceptions
import re
from person import Person
class Employee(Person):
    id=0
    def __init__(self, ID,full_name, money, sleepmood, healthRate, email, workmood, salary, is_manager):
        super().__init__(full_name, money, sleepmood, healthRate)

        ptrn = r'^[a-zA-z0-9]+@[a-z]+\.[a-z]{2,4}$'
        result = re.match(ptrn, email)

        if salary < 1000:
            raise ValueError("salary should greater than 999 !")
        elif 0 > healthRate < 99:
            raise ValueError(" healthRate should between 0 and 100")
        elif not result:
            raise ValueError(" email is wrong")
        else:
            self.ID=ID
            self.email = email
            self.workmood = workmood
            self.salary = salary
            self.is_manager = is_manager

    @staticmethod
    def sendEmail(to, subject, body, reciver):
        ptrn = r'^[a-zA-z0-9]+@[a-z]+\.[a-z]{2,4}$'
        result = re.match(ptrn, to)
        if result:
            MyEmail = open("Email.txt", "a")
            MyEmail.write("to: " + to + "\n")
            MyEmail.write("Subject: " + subject + "\n")
            MyEmail.write("Body: " + body + "\n")
            MyEmail.write("Reciver: " + reciver + "\n")
            MyEmail.write("================================= " + "\n")
            MyEmail.close()
        else:
            raiseExceptions("Sorry invalid email")

    def work(self, hours):
        if hours == 8:
            self.sleepmood = "happy"
        elif hours < 8:
            self.sleepmood = "Lazy"
        else:
            self.sleepmood = "tired"


nayra = Employee(2,"nayra" , 500 , "tired", 50 , "nayra@gmail.com" , "tired" , 20000 , 0)
