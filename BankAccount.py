# BankAccount.py
# Author: Vince Jones
# Date: December 15, 2022

#import Transaction class
from Transaction import *

def main():
    """Display main menu and class functions based on the selected action"""

    print ('Welcome to Bank Account Application')
    print ()

    done = False

    # Create an empty list of transactions
    list_of_transactions = []

    #Loop as long as done is False
    while (not done):
        #Display menu
        print ('===================================')
        print ('A - Read data from the file')
        print ('B - Display list of transactions')
        print ('C - Add a new transaction')
        print ('D - Calculate current balance')
        print ('E - Save data to a file')
        print ('Q - Quit')
        print ('===================================')
        print ('Please select an action by typing A, B, C, D, E, or Q')
        action = input ('? ')

        if (action == 'A' or action == 'a'):
            read_data (list_of_transactions)
        elif (action == 'B' or action == 'b'):
            display_list (list_of_transactions)
        elif (action == 'C' or action == 'c'):
            add_transaction (list_of_transactions)
        elif (action == 'D' or action == 'd'):
            calculate_balance (list_of_transactions)
        elif (action == 'E' or action == 'e'):
            save_data (list_of_transactions)
        elif (action == 'Q' or action == 'q'):
            done = True
        else:
            print ('Incorrect action type. Please try again')

        print ()

    print ('Thank you for using Bank Account Application')

def read_data(list_of_transactions):
    """Read data from the input file, create transaction object and add it to
       the list of transactions"""

    # Ask user for name of the input file
    file_name = input("Enter the name of the input file: ")

    try:
        # Open the file and read each line of data
        with open(file_name, "r") as f:
            for line in f:
                # Split line using colon (:) as delimiter
                data = line.split(":")

                # Create a Transaction object using the data
                transaction = Transaction(data[0], data[1], data[2])

                # Add the transaction to the list of transactions
                list_of_transactions.append(transaction)
    except FileNotFoundError:
        # If the input file is not found, display an error message
        print("Error: Input file not found")
        
    print ('Read Data Function')

def display_list(list_of_transactions):
    # Sort the list of transactions by date
    sorted_list = sorted(list_of_transactions, key=lambda x: x.date)

    # Display the list of transactions in the form of a table
    print('Date\tType\tAmount')
    print('==========================')
    for transaction in sorted_list:  
        print("{0}\t{1:12}\t${2:.2f}".format(transaction.date, transaction.transaction_type, float(transaction.amount)))

def add_transaction(list_of_transactions):
    # Ask user for date, type, and amount of transaction
    date = input('Enter the date of the transaction (YYYYMMDD): ')
    transaction_type = input('Enter the type of the transaction (deposit, withdraw, bank charge, interest): ')
    amount = input('Enter the amount of the transaction: ')

    try:
        # Convert the amount to a float
        amount = float(amount)

        # Validate the transaction type and the amount
        if transaction_type not in ['deposit', 'withdraw', 'bank charge', 'interest']:
            raise ValueError('Invalid transaction type')
        if amount < 0:
            raise ValueError('Invalid amount')

        # Create a transaction object and append it to the list of transactions
        transaction = Transaction(date, transaction_type, amount)
        list_of_transactions.append(transaction)
    except ValueError as e:
        # Display an error message if the transaction type or amount is invalid
        print('Error: {}'.format(e))

def calculate_balance(list_of_transactions):
    balance = 0
    for transaction in list_of_transactions:
        if transaction.transaction_type == 'deposit' or transaction.transaction_type == 'interest':
            balance += float(transaction.amount)
        elif transaction.transaction_type == 'withdraw' or transaction.transaction_type == 'bank charge':
            balance -= float(transaction.amount)
    print("Current balance is ${:.2f}".format(balance))

def save_data(list_of_transactions):
    print('Save Data Function')
    filename = input('Enter the name of the output file: ')
    sorted_transactions = sorted(list_of_transactions, key=lambda x: x.date)
    with open(filename, 'w') as f:
        for transaction in sorted_transactions:
            f.write(f"{transaction.date}:{transaction.transaction_type}:{transaction.amount}\n")
    print(f"Data saved to {filename}")
        
main()
