#ATM PROJECT
print("welcome to ABC bank!!")
print("Insert your card")
pin = 1234
amount = 2000
chances = 3
amount_start = 0
while chances!=0:
     user_pin = int(input("Enter the pin number:"))
     if user_pin != pin:
       chances -= 1
       print("Wrong pin number")
       print("Number of chances left:",chances)

     elif user_pin == pin:
        print("Enter the pin number: success")
        print("1:Deposit\n 2:Withdrawal\n 3:BalanceEnquiry")
        ch = int(input("Enter your choice"))

        if ch == 1:
            damount=int(input("Enter the deposit amount"))
            amount = amount+damount
            print("Your available balance:",amount)

        elif ch == 2:
            wamount = int(input("enter the withdrawal amount:"))
            amount=amount-wamount
            while amount_start <= wamount:
              print("ATM,ok done", amount_start)
              default_cash= 500
              amount_start+= default_cash
            if amount_start-default_cash == wamount:
              print("please collect your cash:",wamount)

        else:
           print("Your available balance:", amount)


     else:
        print("Both pin and ATM card is wrong")
        print("Your transaction is declined /n please collect your card")
     user_exit = input("Would you like to exit? :")
     if user_exit == "Yes":
         print("Thank You for choosing ABC bank!!")
         break
     else:
         continue

amount_start = 0

