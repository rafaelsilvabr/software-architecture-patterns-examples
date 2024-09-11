# Exemplos Camadas/Layers

Para implementar exemplos de uma aplicação de abertura de conta bancária usando SQLite para persistência, vamos criar duas abordagens: uma usando camadas por entidade e outra usando metaparâmetro. Isso permitirá armazenar e manipular dados de Account, Customer, e Transaction.

## Exemplo 1: Camadas por Entidade

Neste exemplo, cada entidade tem suas próprias camadas de dados e de negócio. Usaremos SQLite para persistência.

```python
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
        CREATE TABLE IF NOT EXISTS Transaction (
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
        cursor.execute('INSERT INTO Transaction (description) VALUES (?)', (description,))
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
```

## Exemplo 2: Camadas por Metaparâmetro

Neste exemplo, usamos um metaparâmetro para definir qual entidade está sendo manipulada, tornando o código mais genérico.

```python
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
        CREATE TABLE IF NOT EXISTS Transaction (
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
            cursor.execute('INSERT INTO Transaction (description) VALUES (?)', (data,))
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
```

## Explicação

Camadas por Entidade: Cada entidade (Account, Customer, Transaction) tem suas próprias camadas de dados e de negócio. Isso facilita a manutenção e evolução de cada entidade de forma isolada, mas pode levar a código duplicado.

Camadas por Metaparâmetro: Utiliza um método genérico que recebe um parâmetro para definir qual entidade está sendo manipulada. Isso reduz a duplicação de código, mas pode ser mais difícil de entender, pois a lógica é mais genérica.

Esses exemplos mostram como estruturar uma aplicação usando diferentes abordagens de camadas, cada uma com suas vantagens e desvantagens, e como persistir dados usando SQLite.
