import sqlite3
import json
from models import Entry

def get_all_entries():
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # SQL query
        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.subject,
            e.entry,
            e.mood_id
        FROM entry e
        """)

        # Initialize empty list to hold entry representations
        entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:
            entry = Entry(row['id'], row['date'], row['subject'],
                            row['entry'], row['mood_id'])
            
            entries.append(entry.__dict__)

    return json.dumps(entries)

def get_entry_by_id(id):

    with sqlite3.connect("./dailyjournal.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # SQL query
        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.subject,
            e.entry,
            e.mood_id
        FROM entry e
        WHERE e.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an entry instance from the current row
        entry = Entry(data['id'], data['date'], data['subject'],
                            data['entry'], data['mood_id'])

        return json.dumps(entry.__dict__)

def delete_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM entry
        WHERE id = ?
        """, (id, ))

def search_entry(searchTerm):
    with sqlite3.connect("./dailyjournal.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.subject,
            e.entry,
            e.mood_id
        FROM entry e
        WHERE e.entry LIKE ?
        """, ("%"+ searchTerm + "%", ))

        entries = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['id'], row['date'], row['subject'],
                            row['entry'], row['mood_id'])
            entries.append(entry.__dict__)
    
    return json.dumps(entries)