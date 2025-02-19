from Notes import Note

class NoteOperations:
    def __init__(self):
        self.notes = []

    def add_note(self, id, title, content):
        if any(note.get_id() == id for note in self.notes):
            print("Заметка с таким ID уже есть")
            return

        note = Note(id, title, content)
        self.notes.append(note)
        print(f"Note with ID '{id}' added")

