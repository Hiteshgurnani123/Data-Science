## Bank Management System

import json
import random 
import string
from pathlib import Path
class Bank:

    database = Path('python\OOPS\data.json')
    data = []

    try:
        if Path(database).exists:
            with open(database, 'r') as fs:
                data = json.loads(fs.read())

        else:
            print('No such files exist')

    except Exception as err:
        print(f'An exception occured as {err}')

    @staticmethod
    def __update():
        with open(Bank.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    @staticmethod
    

    def create_account(self):
        info = {
            "name": input("Enter Your Name : "),
            "age": int(input("Enter Your Age : ")),
            "email": input("Enter Your email : "),
            "pin": int(input("Enter Your 4 Number PIN : ")),
            "accountNo." : 1234,
            "balance": 0
        }

        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print('Sorry You Cannot Create Account')
        else:
            print('Your Account has been create successfully')
            for i in info:
                print(f'{i} : {info[i]}')
            print('Please note down your account number')
            
            Bank.data.append(info)

            Bank.__update()


user = Bank()

print('Press 1 for creating an account')
print('Press 2 for Depositing money in the bank')
print('Press 3 for withdrawing money from the bank')
print('Press 4 for Details of the account')
print('Press 5 for updating the Details of the account')
print('Press 6 for deleting the account')

check = int(input("Enter your choice: "))

if check == 1:
    user.create_account()
