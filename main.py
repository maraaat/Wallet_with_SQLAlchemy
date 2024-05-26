from database.query import WalletQueries

# WalletQueries.create_tables() # Use it to delete all tables and make new

i = 1
while i != 5:
    i = int(input("""What do you want to do? 
    1 - get balance
    2 - add new transaction
    3 - get all transactions
    4 - delete transaction by id
    5 - exit
    Select: """))
    if i == 1:
        WalletQueries.get_balance()

    elif i == 2:
        WalletQueries.trans_params()

    elif i == 3:
        WalletQueries.get_all_trans()

    elif i == 4:
        WalletQueries.delete_trans(int(input("Write transaction id: ")))
