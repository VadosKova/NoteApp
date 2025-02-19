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
        print(f"Note was added")


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

