## 📦 Class: ATM
class Atm:
### 🧾 Attributes:  
    __initial_balance:int=1000
    __pin:int=1234

    @staticmethod
    def check_pin(input_pin:int):
        if int(input_pin)==Atm.__pin:
            return True
        else :
            return False 
## 🛠 Methods:      
    def check_balance(self):
        print(f"Your initial balance is ({Atm.__initial_balance}) rupees")

    def deposit_money(self,amount:int):  
        if amount >= 1:
            Atm.__initial_balance += amount  
            print(f"Your current balance is ({Atm.__initial_balance})")
        else: 
            print("Amount must be positive")   
          

    def withdraw_money(self,amount:int) :
        if amount <= Atm.__initial_balance:
            Atm.__initial_balance -= amount  
            print(f"You withdraw {amount} rupees")
            print(f"Your current balance is ({Atm.__initial_balance})")
        else: 
            print("Insufficient balance")   

### 🧭 Menu-Based System:

def display_menu():
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

print("~~"*15)    
print("Welcome to Shurem ATM CLI!")
print("~~"*15) 
user_input=input("Enter your PIN: ")
if Atm.check_pin(int(user_input)):
    while True:
        try:
            pin=Atm()
            display_menu()
            choice=input("Enter your choice (1,2,3,4): ")
            if choice == "1":
                pin.check_balance()
            elif choice == "2":
                amount= int(input("Enter your deposite amount: "))
                pin.deposit_money(amount)
            elif choice == "3":
                amount= int(input("Enter your withdraw amount: "))
                pin.withdraw_money(amount)
            elif choice == "4":
                print("Thank you for using over ATM machine!")
                break
            else :
                raise ValueError("Invalid Choice")
        except Exception as e :
            print(e)   
            break              
else :
    print("Please enter the correct pin")            