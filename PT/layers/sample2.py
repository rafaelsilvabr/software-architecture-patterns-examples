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

# Camada de Dados Genérica
class DataLayer:
    def save(self, entity_type, data):
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()
        if entity_type == "Account":
            cursor.execute('INSERT INTO Account (account_number) VALUES (?)', (data,))
        elif entity_type == "Customer":
            cursor.execute('INSERT INTO Customer (name) VALUES (?)', (data,))
        elif entity_type == "Transaction":
            cursor.execute('INSERT INTO "Transaction" (description) VALUES (?)', (data,))
        conn.commit()
        conn.close()
        print(f"{entity_type} {data} saved.")

# Camada de Negócio Genérica
class BusinessLayer:
    def __init__(self):
        self.data_layer = DataLayer()

    def create(self, entity_type, data):
        self.data_layer.save(entity_type, data)

# Configurar o banco de dados
setup_database()

# Uso da camada de negócio com metaparámetro
business_layer = BusinessLayer()
business_layer.create("Account", "12345")
business_layer.create("Customer", "John Doe")
business_layer.create("Transaction", "Deposit $100")