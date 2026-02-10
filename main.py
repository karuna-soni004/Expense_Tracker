# Expense Tracker Project
expensesList = [] #List of all expenses in form of dictionary
print("Welcome to Expense Tracker")

while True:
    print("=====MENU=====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice = int(input("Please Enter Your Choice : "))

#Add expense
    if(choice ==1):
        date = input("Enter date?:")
        category = input("Enter category (Food, Travel, Cosmetic, Stationary):")
        description= input("Add detail:")
        amount = float(input("Enter amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print("\n Expenses add successfully")

# 2. View all expenses
    elif(choice == 2):
        if(len(expensesList)==0):
            print("No Expenses Added")
        else:
            print("===== YOUR EXPENSES =====")
            count = 1
            for eachExpense in expensesList:
                print(f"number of expense{count} -> {eachExpense["date"]},{eachExpense["category"]}, {eachExpense["description"]}, {eachExpense["amount"]}")
                count = count+1

# 3. View total spending
    elif(choice == 3):
        total = 0
        for eachExpense in expensesList:
            total = total + eachExpense["amount"]
        
        print("\n Total expense = ", total)

# 4. EXIT
    elif(choice == 4):
        print("Thankyou for using this tracker")
        break
    else:
        print("Invalid choice. Try again.")



