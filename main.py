## 📦 Class: ATM
class Atm:
### 🧾 Attributes:  
    __initial_balance = 5000
    __pin = 1234

    @staticmethod
    def check_pin(input_pin:int):
        if int(input_pin)==Atm.__pin :
            return True
        else :
            return False 
## 🛠 Methods:      
    def check_balance(self):
        print(f"💰 Your current balance is:  ({Atm.__initial_balance})")

    def deposit_money(self,amount:int):  
        if amount >= 1:
            Atm.__initial_balance += amount  
            print(f"✅ Deposit successful. New balance: ({Atm.__initial_balance}) rupees")
        else: 
            print("❌ Invalid amount. Must be positive.")   
          

    def withdraw_money(self,amount:int) :
        if amount <= self.__initial_balance:
            Atm.__initial_balance -= amount  
            print(f"You withdraw {amount} rupees")
            print(f"✅ Withdrawal successful. Remaining balance: ({Atm.__initial_balance}) rupees")
        else: 
            print("❌ Insufficient balance.")  
    def exit(self):
        print("👋 Thank you for using our ATM. Goodbye!")         

### 🧭 Menu-Based System:

def display_menu():
    print("\n📋 Select an option:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

print("~~"*15)    
print("✨ Welcome to Shurem ATM CLI ✨")
print("~~"*15) 
user_input=input("🔑 Enter your PIN: ")
if Atm.check_pin(int(user_input)):
    while True:
        try:
            pin=Atm()
            display_menu()
            choice=input("👉 Enter your choice (1-4): ")
            if choice == "1":
                pin.check_balance()
            elif choice == "2":
                amount= int(input("💵 Enter amount to deposit: "))
                pin.deposit_money(amount)
            elif choice == "3":
                amount= int(input("🏧 Enter amount to withdraw: "))
                pin.withdraw_money(amount)
            elif choice == "4":
                pin.exit()
                break
            else :
                raise ValueError("Invalid Choice")
        except Exception as e :
            print(e)   
            break              
else :
    print("🔐 Please enter correct PIN first.")            