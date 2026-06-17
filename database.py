import sqlite3

connection = sqlite3.connect("railway.db")
cursor = connection.cursor()

# Таблица поездов
cursor.execute("""
CREATE TABLE IF NOT EXISTS trains (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number TEXT,
    destination TEXT,
    departure_time TEXT
)
""")

# Таблица билетов
cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    train_id INTEGER,
    passenger TEXT,
    seat TEXT
)
""")

connection.commit()


# Добавление поезда
def add_train(number, destination, departure_time):
    cursor.execute(
        "INSERT INTO trains(number, destination, departure_time) VALUES (?, ?, ?)",
        (number, destination, departure_time)
    )
    connection.commit()


# Получение всех поездов
def show_trains():
    cursor.execute("SELECT * FROM trains")
    return cursor.fetchall()


# Продажа билета
def add_ticket(train_id, passenger, seat):
    cursor.execute(
        "INSERT INTO tickets(train_id, passenger, seat) VALUES (?, ?, ?)",
        (train_id, passenger, seat)
    )
    connection.commit()


# Получение всех билетов
def show_tickets():
    cursor.execute("SELECT * FROM tickets")
    return cursor.fetchall()


# Поиск по пункту назначения
def search_train(destination):
    cursor.execute(
        "SELECT * FROM trains WHERE destination = ?",
        (destination,)
    )
    return cursor.fetchall()