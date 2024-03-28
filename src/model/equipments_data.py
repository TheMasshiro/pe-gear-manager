import sqlite3
from pathlib import Path

file_dir = Path(__file__).parent.absolute()
database_file = file_dir / "data" / "equipments.db"


def create_table():
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS Equipments
            (
                id TEXT PRIMARY KEY,
                name TEXT,
                quantity TEXT
                )

            """
    )
    conn.commit()
    conn.close()


def fetch_equipments():
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Equipments")
    equipments = cursor.fetchall()
    conn.close()
    return equipments


def insert_equipment(id, name, quantity):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Equipments (id, name, quantity) VALUES (?, ?, ?)",
        (id, name, quantity),
    )
    conn.commit()
    conn.close()


def update_equipment(new_name, new_quantity):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Equipments SET name = ?, quantity = ? WHERE id = ?",
        (new_name, new_quantity),
    )
    conn.commit()
    conn.close()


def delete_equipment(id):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Equipments WHERE id = ?", (id,))
    conn.commit()
    conn.close()


def equipment_id_exists(id):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Equipments WHERE id = ?", (id,))
    conn.commit()
    conn.close()


def equipment_name_exists(name):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Equipments WHERE name = ?", (name,))
    conn.commit()
    conn.close()


create_table()
