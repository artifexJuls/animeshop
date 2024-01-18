import sqlite3

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

# Products
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Clothes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price TEXT NOT NULL,
        description TEXT NOT NULL,
        tags TEXT NOT NULL,
        amount INTEGER
    )
""")

cursor.execute("""
    INSERT INTO Clothes(name, price, description, tags, amount) VALUES
    ("OverSize Naruto Hoodie", "550", "Тепле оверсайз худі з Наруто", "naruto", "3"),
    ("Gojo Satoru Eye", "1200", "Худі з відомим магом - Годжо Сатору", 'jjk', "15")
""")
connection.commit()

# Customers
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        second_name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone INTEGER NOT NULL,
        birthday TEXT NOT NULL,
        shopCard INTEGER NOT NULL
    )
""")

cursor.execute("""
    INSERT INTO Customers(first_name, second_name, email, phone, birthday, shopCard) VALUES
    ('Julia', 'Kovalenko', 'julia@gmail.com', '380501234567', '2000-10-10', '1')
""")
connection.commit()

# ShopCard
cursor.execute("""
    CREATE TABLE IF NOT EXISTS ShopCard (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        product_price INTEGER NOT NULL,
        product_amount INTEGER NOT NULL,
        customer_id INTEGER NOT NULL REFERENCES Customers(id)
    )
""")

cursor.execute("""
    INSERT INTO ShopCard(product_name, product_price, product_amount, customer_id) VALUES
    ('OverSize Naruto Hoodie', '550', '1', '1')
""")
connection.commit()

# Orders
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        shopCard INTEGER NOT NULL REFERENCES ShopCard(id),
        product_name TEXT NOT NULL,
        amount INTEGER NOT NULL,
        id_customer INTEGER NOT NULL REFERENCES Customers(id),
        customer_name TEXT NOT NULL,
        customer_second_name TEXT NOT NULL,
        phone INTEGER NOT NULL,
        address TEXT NOT NULL,
        price INTEGER NOT NULL,
        date TEXT NOT NULL,
        status TEXT NOT NULL
    )
""")

cursor.execute("""
    INSERT INTO Orders(shopCard, product_name, amount, id_customer, customer_name, customer_second_name, phone, address, price, date, status) VALUES
    ('1', 'OverSize Naruto Hoodie', '1', '1', 'Julia', 'Kovalenko', '380501234567', 'Lviv Ivana-Franka Poshtomat 45 Nova Poshta', '550', '2022-10-10', 'In progress')
""")
connection.commit()

connection.close()
