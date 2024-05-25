from database.query import WalletQueries

WalletQueries.create_tables()

# WalletQueries.insert_basic()

WalletQueries.get_balance()

def trans_params():
    title = input("Write transaction name: ")
    cost = int(input("Write how much it: "))
    category = input("Write your category: profit, food, clothes, fun, health, transport, other: ")

    WalletQueries.insert_trans(title, cost, category)

#trans_params()
WalletQueries.get_all_trans()
# WalletQueries.delete_trans(2)