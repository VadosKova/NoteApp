import pyodbc
from Notes import Note
from NoteSaving import NoteSaving

class NoteOperations:
    def __init__(self):
        self.notes = []
        self.file_operations = NoteSaving()
        self.connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=Lesson;Trusted_Connection=yes'
        self.conn = pyodbc.connect(self.connection_string)
        self.cursor = self.conn.cursor()

    def add_note(self, id, title, content):
        self.cursor.execute("SELECT 1 FROM Notes WHERE ID = ?", (id,))
        result = self.cursor.fetchone()

        if result:
            print("Заметка с таким ID уже есть")
            return

        self.cursor.execute("INSERT INTO Notes (ID, Title, Content) VALUES (?, ?, ?)", (id, title, content))
        self.conn.commit()
        print("Note was added to database")


    def delete_note_by_id(self, id):
        note_to_delete = None
        for note in self.notes:
            if note.get_id() == id:
                note_to_delete = note
                break

        if note_to_delete:
            self.notes.remove(note_to_delete)
            print("Note was deleted")
        else:
            print("Error")

    def show_note_by_id(self):
        note_id = input("Enter the note ID: ")

        self.cursor.execute("SELECT * FROM Notes WHERE ID = ?", (note_id,))
        row = self.cursor.fetchone()

        if row:
            note = Note(row[0], row[1], row[2])
            print(f"\nResult:\n{note}")
        else:
            print("Error")

    def save_notes(self):
        self.file_operations.save_notes_to_file(self.notes)

    def load_notes(self):
        self.cursor.execute("SELECT * FROM Notes")
        rows = self.cursor.fetchall()

        if not rows:
            print("Error")
        else:
            for row in rows:
                note = Note(row[0], row[1], row[2])
                print(note)