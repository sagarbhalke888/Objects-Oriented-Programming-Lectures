from numpy.random import randint


class FastPay:
    def __init__(self,name,age,balance,gender):
        self.name = name
        self.age = age
        self.account = randint(10000000,99999999)
        self.balance = balance
        self.gender = gender

    def checkBalance(self):
        statement = self.name + " with account number as : "+str(self.account)+" has balance of Rs : " + str(self.balance)
        print(statement)
        return statement

    def send(self,money):
        self.balance = self.balance - money


    def recieve(self,money):
        self.balance = self.balance + money

while True:

    option = input("Do you want to create a new account or you have account Y or N")

    if option == "Y":

        name = input("Please Enter the name: ")
        age = int(input("Please Enter the age: "))
        balance = int(input("Please Enter the balance: "))
        gender = input("Please Enter the gender: ")

        user = FastPay(name,age,balance,gender)

    else:
        option = input("1 - Check balance \n 2- Send Money \n 3- Recieve \n")
        if option ==  "1":
            user.checkBalance()
        elif option == "2":
            money = int(input("How much money want to send: "))
            user.send(money)

        elif option == "3":
            money = int(input("How much money want to recieve: "))
            user.recieve(money)
        else:
            print("Invalid option")