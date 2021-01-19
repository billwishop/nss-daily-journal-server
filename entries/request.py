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