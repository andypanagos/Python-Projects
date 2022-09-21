class User:
    name = "Andy"
    email = "andypanagos@gmail"
    password = "abc123"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

class Employee(User):
    base_pay = 12.00
    department = "Fragrance"
    pin_number = "2002"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")
            
class Supplier(User):
    base_pay = 12.95
    entry_phonenumber = "617-935-2756"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_phonenumber = input("Enter your phone number: ")
        entry_password = input("Enter your password: ")
        if (entry_phonenumber == self.phonenumber and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or phone number is incorrect.")
        
    

customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()
        
