Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#Program asks the user for a list of their monthly expenses as well as amount.  #Then analyze the expenses and display the total, highest and lowest expense.

from functools import reduce

#Function prompts user for expense type as well as amount.
def get_expenses():
    expenses = []
    print('Enter your monthly expenses. Type "done" when finished')

...     #Ask for type of expense,and stop when the response is empty.
...     while True:
...         expense_type = input('Enter expense type: ')
...         if expense_type.lower() == 'done':
...             break
...         try:
...             amount = float(input(f'Enter amount for {expense_type}: $'))
...             expenses.append((expense_type, amount))
...         except ValueError:
...             print('Please enter a valid number for the amount.')
... 
... 
... 
...     return expenses
... 
... #Main function calls out other function and process inputs and display the total.
... def main():
...     expenses = get_expenses()
... 
...     if not expenses:
...         print('No expenses entered.')
...         return
... 
...     #Total expense using reduce.
...     total = reduce(lambda acc, item: acc + item[1], expenses, 0)
... 
...     #Highest expense using reduce.
...     highest = reduce(lambda x, y: x if x[1] > y[1] else y, expenses)
... 
...     #Lowest expense using reduce.
...     lowest = reduce(lambda x, y: x if x[1] < y[1] else y, expenses)
... 
...     #Display outcome!
...     print('\n--- Monthly Expense Report ---')
...     print(f'Total Expense: ${total:.2f}')
...     print(f'Highest Expense: {highest[0]} (${highest[1]:.2f})')
...     print(f'Lowest Expense: {lowest[0]} (${lowest[1]:.2f})')
... 
