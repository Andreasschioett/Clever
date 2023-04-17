import sqlite3


create_kunde_table = """
CREATE TABLE IF NOT EXISTS kunde (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
"""

create_bil_table = """
CREATE TABLE IF NOT EXISTS område (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    strømkapacitet INTEGER,
); 
"""

create_chop_table = """
CREATE TABLE IF NOT EXISTS chip (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

); 
""" 

create_bud_table = """
CREATE TABLE IF NOT EXISTS bud (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    restaurant_id INTEGER, 
    ordre_id INTEGER,
    område_id INTEGER,
    FOREIGN KEY (restaurant_id) REFERENCES restaurant (id),
    FOREIGN KEY (ordre_id) REFERENCES ordre (id),
    FOREIGN KEY (område_id) REFERENCES område (id) 
 
); 
"""
create_restaurant_table = """
CREATE TABLE IF NOT EXISTS restaurant (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    adresse TEXT,
    restaurantnavn TEXT,
    kunde_id INTEGER,  
    ordre_id INTEGER,
    bud_id INTEGER,
    område_id INTEGER, 
    FOREIGN KEY (kunde_id) REFERENCES kunde (id),
    FOREIGN KEY (område_id) REFERENCES område (id),
    FOREIGN KEY (ordre_id) REFERENCES ordre (id),
    FOREIGN KEY (bud_id) REFERENCES bud (id) 
); 
"""

with sqlite3.connect('OrderYOYO.db') as conn:
    c = conn.cursor()
    c.execute(create_bud_table)
    c.execute(create_kunde_table)
    c.execute(create_ordre_table)
    c.execute(create_område_table)
    c.execute(create_restaurant_table)
