import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.executescript("""
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
);

INSERT INTO items (name, description) VALUES
('Item 1', 'Description 1'),
('Item 2', 'Description 2'),
('Item 3', 'Description 3');
""")
conn.commit()
conn.close()
print("Database initialized.")
