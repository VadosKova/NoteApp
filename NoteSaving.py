from Notes import Note
import os

class NoteSaving:
    def __init__(self, file="notes.txt"):
        self.file = file
        if not os.path.exists(self.file):
            with open(self.file, 'w') as file:
                print("Файл не найден. Создан новый")

    def save_notes_to_file(self, notes):
        try:
            with open(self.file, 'w') as file:
                for note in notes:
                    file.write(f"ID: {note.get_id()}, Title: {note.title}, Content: {note.content};\n")
            print(f"Notes saved to {self.file}")
        except Exception:
            print(f"Error")

    def load_notes_from_file(self):
        notes = []
        try:
            with open(self.file, 'r') as file:
                content = file.read().strip().split("\n")
                for note_data in content:
                    note_data = note_data.strip().strip(";")
                    note_lines = [line.split(":")[1].strip() for line in note_data.split(",")]

                    if len(note_lines) == 3:
                        id, title, content = note_lines
                        notes.append(Note(id, title, content))
        except FileNotFoundError:
            print("Empty")

        except Exception:
            print("Error")

        return notes