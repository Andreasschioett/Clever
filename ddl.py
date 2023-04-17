import sqlite3


create_kunde_table = """
CREATE TABLE IF NOT EXISTS kunde (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    navn TEXT,
    email TEXT,
    password TEXT,
    adresse TEXT
);
"""

create_oplader_table = """
CREATE TABLE IF NOT EXISTS oplader (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    strømkapacitet INTEGER,
    solcelle INTEGER
);
"""
create_bil_table = """
CREATE TABLE IF NOT EXISTS område (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    strømkapacitet INTEGER,
); 
"""



with sqlite3.connect('Clever.db') as conn:
    c = conn.cursor()
    c.execute(create_kunde_table)
    c.execute(create_oplader_table)
    c.execute("INSERT INTO oplader (strømkapacitet, solcelle) VALUES (100, 0)")

