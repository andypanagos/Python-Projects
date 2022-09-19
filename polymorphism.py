

class Employee:
    name = 'Andy'
    email = 'andy@gmail.com'
    password = 'abc123'

    def logIn(self):
        login_name = input("Enter Name: ")
        login_email = input("Enter Email: ")
        login_password = input("Enter Password: ")
        if (login_email == self.email and login_password == self.password):
            print("Welcome back, {}!".format (login_name))
        else:
            print(" password or email is incorrect.")

class CEO(Employee):
    master_pin = 1212
    security_answer = 'ontario'

    def logIn(self):
        login_name = ("Provide Your Name: ")
        login_pin = ("Please Enter Master Pin: ")
        login_security = ("What is your security question answer: ")
        if (login_pin == self.master_pin and login_security == self.security_answer):
            print("Hello CEO, {}!".format (login_name))
        else:
            print(" you are not the CEO. ")



employee = Employee()
employee.logIn()

ceo = CEO()
ceo.logIn()

if __name__ == '__main__':
    
