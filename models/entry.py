class Entry():

    def __init__(self, id, date, subject, entry, mood_id):
        self.id = id
        self.date = date
        self.subject = subject
        self.entry = entry
        self.mood_id = mood_id 
        self.mood = None
