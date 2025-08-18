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
    def __accountno_generator():
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices('!@#$%^&*', k=3)
        id = alpha + num + spchar
        random.shuffle(id)
        return ''.join(id)
    

    def create_account(self):
        info = {
            "name": input("Enter Your Name : "),
            "age": int(input("Enter Your Age : ")),
            "email": input("Enter Your email : "),
            "pin": int(input("Enter Your 4 Number PIN : ")),
            "accountNo." : Bank.__accountno_generator(),
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

    def deposite_money(self):
        accnumber = input("Enter your account number : ")
        pin = int(input("Enter your 4 digit pin : "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print('Account Not Found')

        else:
            amount = int(input("Enter the amount you want to deposit : "))
            if amount > 10000 or amount < 0:
                print('You cannot deposit more than 10000 or less than 0')
                
            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print('Your balance has been deposited successfully')

    def withdraw_money(self):
        accnumber = input("Enter your account number : ")
        pin = int(input("Enter your 4 digit pin : "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print('Account Not Found')

        else:
            amount = int(input("Enter the amount you want to withdraw : "))
            if userdata[0]['balance'] < amount:
                print('You do not have sufficient balance to withdraw this amount')
                    
            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                print('Your balance has been withdrawn successfully')

    def show_details(self):
        accnumber = input("Enter your account number : ")
        pin = int(input("Enter your 4 digit pin : "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print('Account Not Found')

        else:
            print('Here are your account details:')
            for i in userdata[0]:
                print(f'{i}: {userdata[0][i]}')

    def update_details(self):
        accnumber = input("Enter your account number : ")
        pin = int(input("Enter your 4 digit pin : "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print('Account Not Found')

        else:
            print('Fill the details you want to update or press enter to skip:')

            newdata = {
                'name' : input('Enter your new name or press enter to skip: '),
                'email' : input('Enter your new email or press enter to skip: '),
                'pin' : input('Enter your new pin or press enter to skip: '),
            }

            if newdata['name'] == '':
                newdata['name'] = userdata[0]['name']
            if newdata['email'] == '':
                newdata['email'] = userdata[0]['email']
            if newdata['pin'] == '':
                newdata['pin'] = userdata[0]['pin']

            newdata['age'] = userdata[0]['age']
            newdata['accountNo.'] = userdata[0]['accountNo.']
            newdata['balance'] = userdata[0]['balance']

            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]

            Bank.__update()
            print('Your details have been updated successfully')

    def delete_account(self):
        accnumber = input("Enter your account number : ")
        pin = int(input("Enter your 4 digit pin : "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print('Account Not Found')

        else:
            res = input("Are you sure you want to delete your account? (yes/no): ").lower()
            if res == 'yes':
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                Bank.__update()
                print('Your account has been deleted successfully')
            
            else:
                print('Your account has not been deleted')


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

if check == 2:
    user.deposite_money()

if check == 3:
    user.withdraw_money()

if check == 4:
    user.show_details()

if check == 5:
    user.update_details()

if check == 6:
    user.delete_account()