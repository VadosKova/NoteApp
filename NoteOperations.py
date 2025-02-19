from Notes import Note
from NoteSaving import NoteSaving

class NoteOperations:
    def __init__(self):
        self.notes = []
        self.file_operations = NoteSaving()

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

    def show_note_by_id(self):
        note_id = input("Enter the note ID: ")
        note_found = None

        for note in self.notes:
            if note.get_id() == note_id:
                note_found = note
                break

        if note_found:
            print("\nResult:\n", note_found)
        else:
            print("Error")

    def save_notes(self):
        self.file_operations.save_notes_to_file(self.notes)

    def load_notes(self):
        self.notes = self.file_operations.load_notes_from_file()
        if not self.notes:
            print("No notes")
        else:
            for note in self.notes:
                print(note)