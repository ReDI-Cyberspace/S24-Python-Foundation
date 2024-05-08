"""
We will create a program to track our monthly expenses.


The git will be used as a "database". For example, we will update the salary, take the output from console 
and save it in the same file.
After each function execution, manually update the value in file, commit and push to github.

Future improvement:
1) Use classes and objects. How the globle variable will be used in the class?
2) Once we learn file i/o or some api or database, we will replace the manual steps
"""
from datetime import datetime, timedelta
import calendar

bank_balance = 8000
salary = 4000
bonus=200
expenses_s = 2000  
salary_drawn_count = 1
expenses = [
    "rent",
    "food",
    "clothes",
    "travel",
    "other"
]

# write a function to add salary to bank balance only if it's first of the month. also update salaris drawn count
def salary_arrived():
    global bank_balance, salary_drawn_count
    today = datetime.now()
    if today.day == 1:  # Check if it's the first day of the month
        bank_balance += salary
        salary_drawn_count += 1
    print("bank balance:", bank_balance)
salary_arrived()


# write a function to add bonus to the bank balance. take the ammount from user. can you think of any edge case?
def add_bonus():
    global bank_balance
    bank_balance += bonus
    print("Bank balance after bonus:", bank_balance)
    
add_bonus()


# write a function to add expenses. ask user for each type of expense and update bank balance
def add_expenses():
   global bank_balance
   bank_balance -= expenses_s
   print("bank balance after expenses: ", bank_balance)

add_expenses()


# write a function to tell me how much i can spend per day this month
def daily_limit():
    global bank_balance
    today = datetime.now()
    days_in_month = calendar.monthrange(today.year, today.month)[1]
    remaining_days = days_in_month - today.day + 1
    spending_limit = bank_balance / remaining_days
    print("You can spend approximately {:.2f} per day this month.".format(spending_limit))

daily_limit()


# write a function to increae the salary by certain percentage. see how input is different from add bonus
def salary_increase(increment_percentage: float):
    global salary
    if increment_percentage < 0:
        print("Percentage increase should be greater than or equal to zero.")
        return
    increase_amount = salary * increment_percentage / 100
    salary += increase_amount
    print("Salary after increase:", salary)

    print("new salary: ", salary)
salary_increase(10)


# write a funtion to add new type of expense.
def add_new_expense():
    global bank_balance, expenses
    new_expense_type = "health insurance"  # Specify the new expense type
    expense_amount = 1000  # Specify the amount for health insurance
    
    if expense_amount < 0:
        print("Expense amount should be greater than or equal to zero.")
        return
    
    bank_balance -= expense_amount
    expenses.append(new_expense_type)
    print("Bank balance after adding new expense:", bank_balance)

add_new_expense()


# imrovment on the add expense function. we don't want use over and over. 
def add_expense_without_user_promt(expenses: dict):
    # your code here

    print(f"Expanse list: {expenses}")

add_expense_without_user_promt({
    "rent": 1000,
})

add_expense_without_user_promt({
    "clothes": 200,
    "food": 300.0
})


# write code to ask user which operation he wants to perform and then call only that function
