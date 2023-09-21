#defining Bankaccount class and deposit and withdarwal and balance checking methods
class bankaccount:

  def __init__(self, account_number, holder_name, balance):
    self._account_number = account_number
    self._holder_name = holder_name
    self._balance = balance
    print("WELCOME")
    print("Account Number:{}   Account Holdername:{} \n Account balance:{}".
          format(self._account_number, self._holder_name, self._balance))

  def deposit(self, amount):
    if amount > 0:
      self._balance += amount
      print("\n\nDeposited:")
      print("Account Number:{}   Deposited amount:{} \nAccount Balance:{}".
            format(self._account_number, amount, self._balance))
    else:
      print("Invalid deposit amount was entered")

  def withdarwal(self, amount):
    if amount > 0 and amount < self._balance:
      self._balance -= amount
      print("\n\nWithdarwal:")
      print("withdarwal amount:", amount)
      print("The account balance:", self._balance)
    else:
      print("Your account balance was insufficent for withdarwal")
      print("Your account balance :", self._balance)

  def check_balance(self):
    print("\nBalance")
    print(
        "The account number:{}The account holder name:{}The account balance:{}"
        .format(self._account_number, self._holder_name, self._balance))


#creating instance for class
s = bankaccount(123456789, "Vignesh", 0.0)

s.deposit(2000)
s.withdarwal(1500)
s.check_balance()
