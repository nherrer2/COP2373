Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#The program sells tickets to users. No more than 20 tickets can be sold!, and
#each person is only allowed to buy up to 4 tickets. 
#Main func which will call out other functions.

def main():
    total_tickets = 20
    buyers = 0

...     #While loop that will show the remaining tickets after each transaction.
...     while total_tickets > 0:
...         tickets_requested = get_tickets()
... 
...         #If statement that will show how many tickets was bought or if there's
...         #not enough tickets.
...         if tickets_requested <= total_tickets:
...             total_tickets -= tickets_requested
...             buyers += 1
...             print(f"You bought {tickets_requested} ticket(s).")
...             print(f'Tickets remaining: {total_tickets}')
...         else:
...             print("Not enough tickets left. Please selected a smaller amount.")
... 
...     print("\nAll tickets sold!")
...     print(f"Number or buyers: {buyers}")
... 
... #The func will prompt the users for how many tickets they would like to buy
... def get_tickets():
... 
...     #While loop and if statement are used to prompt the user to enter #
...     #of tickets they would like to buy.
...     while True:
...         try:
...             quantity = int(input('\nEnter the number of tickets you would '
...                                  'like to'
...                                  ' buy (up to 4 tickets per person):'))
... 
...                 #Enter # of tickets.
...             if 1 <= quantity <= 4:
...                 return quantity
... 
...             #ValueError in case number picked is invalid.
...             else:
...               print('Invalid. You can only buy 1 to 4 tickets.')
...         except ValueError:
...             print('Enter a valid number.')
... 
... #Call main func.
