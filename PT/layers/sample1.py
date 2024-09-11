import sqlite3

# Configuração inicial do banco de dados SQLite
def setup_database():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Account (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_number TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "Transaction" (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Camada de Dados para a entidade Account
class AccountDataLayer:
    def save_account(self, account_number):
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Account (account_number) VALUES (?)', (account_number,))
        conn.commit()
        conn.close()
        print(f"Account {account_number} saved.")

# Camada de Negócio para a entidade Account
class AccountBusinessLayer:
    def __init__(self):
        self.data_layer = AccountDataLayer()

    def create_account(self, account_number):
        self.data_layer.save_account(account_number)

# Camada de Dados para a entidade Customer
class CustomerDataLayer:
    def save_customer(self, name):
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Customer (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()
        print(f"Customer {name} saved.")

# Camada de Negócio para a entidade Customer
class CustomerBusinessLayer:
    def __init__(self):
        self.data_layer = CustomerDataLayer()

    def create_customer(self, name):
        self.data_layer.save_customer(name)

# Camada de Dados para a entidade Transaction
class TransactionDataLayer:
    def save_transaction(self, description):
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO "Transaction" (description) VALUES (?)', (description,))
        conn.commit()
        conn.close()
        print(f"Transaction {description} saved.")

# Camada de Negócio para a entidade Transaction
class TransactionBusinessLayer:
    def __init__(self):
        self.data_layer = TransactionDataLayer()

    def create_transaction(self, description):
        self.data_layer.save_transaction(description)

# Configurar o banco de dados
setup_database()

# Uso das camadas de negócio
account_business = AccountBusinessLayer()
account_business.create_account("12345")

customer_business = CustomerBusinessLayer()
customer_business.create_customer("John Doe")

transaction_business = TransactionBusinessLayer()
transaction_business.create_transaction("Deposit $100")