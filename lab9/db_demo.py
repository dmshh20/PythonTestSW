"""
DB demo: sqlite3 examples for Lab9

How to run:
  cd d:\pythonTestSW\PythonTestSW\lab9
  python db_demo.py

This script will create 'lab9_demo.db' in the same folder and print query outputs.
"""
import sqlite3
import csv
from pathlib import Path

DB_FILE = Path(__file__).parent / "lab9_demo.db"

SAMPLE_STUDENTS = [
    ("Bohdan", "Ivanov"),
    ("Marta", "Petrenko"),
    ("Olena", "Kovalenko"),
]

def create_connection(db_path: str):
    return sqlite3.connect(db_path)

def init_db(conn: sqlite3.Connection):
    with conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS students (
                empid INTEGER PRIMARY KEY AUTOINCREMENT,
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL
            )
            """
        )

def insert_students(conn: sqlite3.Connection, students):
    with conn:
        conn.executemany(
            "INSERT INTO students (firstname, lastname) VALUES (?, ?)",
            students
        )

def fetch_all_students(conn: sqlite3.Connection):
    cur = conn.cursor()
    cur.execute("SELECT empid, firstname, lastname FROM students")
    return cur.fetchall()

def update_student_lastname(conn: sqlite3.Connection, empid: int, new_lastname: str):
    with conn:
        conn.execute(
            "UPDATE students SET lastname = ? WHERE empid = ?",
            (new_lastname, empid)
        )

def delete_student(conn: sqlite3.Connection, empid: int):
    with conn:
        conn.execute("DELETE FROM students WHERE empid = ?", (empid,))

def param_query(conn: sqlite3.Connection, firstname: str):
    cur = conn.cursor()
    cur.execute("SELECT empid, firstname, lastname FROM students WHERE firstname = ?", (firstname,))
    return cur.fetchall()

def export_to_csv(conn: sqlite3.Connection, csv_path: str):
    rows = fetch_all_students(conn)
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["empid", "firstname", "lastname"])
        writer.writerows(rows)

def show_table_info(conn: sqlite3.Connection, table: str = "students"):
    cur = conn.cursor()
    cur.execute(f"PRAGMA table_info({table})")
    return cur.fetchall()

def main():
    print("DB demo — SQLite (lab9_demo.db)")
    conn = create_connection(str(DB_FILE))
    try:
        init_db(conn)
        print("Table 'students' ensured.")
        # Clean table for demo (safe for lab environment)
        conn.execute("DELETE FROM students")
        conn.commit()

        print("\nInserting sample students...")
        insert_students(conn, SAMPLE_STUDENTS)
        rows = fetch_all_students(conn)
        print("Students after insert:")
        for r in rows:
            print(r)

        # Parameterized query
        print("\nParameterized query (firstname='Marta'):")
        print(param_query(conn, "Marta"))

        # Update a record
        if rows:
            empid_to_update = rows[0][0]
            print(f"\nUpdating empid={empid_to_update} lastname -> 'UpdatedName'")
            update_student_lastname(conn, empid_to_update, "UpdatedName")
            print("After update:", fetch_all_students(conn))

        # Demonstrate delete
        if rows and len(rows) > 1:
            empid_to_delete = rows[1][0]
            print(f"\nDeleting empid={empid_to_delete}")
            delete_student(conn, empid_to_delete)
            print("After delete:", fetch_all_students(conn))

        # Show schema info
        print("\nTable info (PRAGMA table_info):")
        for info in show_table_info(conn):
            print(info)

        # Export to CSV
        csv_path = Path(__file__).parent / "students_export.csv"
        export_to_csv(conn, str(csv_path))
        print(f"\nExported students to {csv_path}")

    finally:
        conn.close()
        print("\nConnection closed.")

if __name__ == "__main__":
    main()
