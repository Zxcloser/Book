import sqlite3

# Создание связи с бд, если ещё не существет
conn = sqlite3.connect('book_db.sqlite')
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''CREATE TABLE IF NOT EXISTS Books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                genres TEXT,
                release_date TEXT)
                ''')

# Инфа в бд
books_data = [
    (1, 'Руслан и Людмила', 'Пушкин', 'поэма', '1820'),
    (2, 'Преступление и наказание', 'Федор Достоевский', 'роман, криминальный жанр', '1866'),
    (3, 'Записки из подполья', 'Федор Достоевский', 'роман, новелла', '1864'),
    (4, 'Герой нашего времени', 'Михаил Лермонтов', 'роман', '1840')
]

cursor.executemany('INSERT INTO Books (id, title, author, genres, release_date) VALUES (?, ?, ?, ?, ?)', books_data)
conn.commit()

# сортирование по дате создания
cursor.execute('SELECT * FROM Books ORDER BY release_date')

# Вывод в консоль
print("Books:")
print("ID", "Title", "Author", "Genres", "Release Date")
for row in cursor.fetchall():
    book_id, title, author, genres, release_date = row
    print(book_id, title, author, genres, release_date)


cursor.close()
conn.close()