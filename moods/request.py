import sqlite3
import json
from models import Mood

def get_all_moods():
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # SQL Query
        db_cursor.execute("""
        SELECT
            m.id,
            m.mood
        FROM mood m
        """)

        # Initialize empty list to hold entry representations
        moods = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:
            mood = Mood(row['id'], row['mood'])

            moods.append(mood.__dict__)

    return json.dumps(moods)