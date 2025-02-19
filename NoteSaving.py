import os

class NoteSaving:
    def __init__(self, file="notes.txt"):
        self.file = file
        if not os.path.exists(self.file):
            with open(self.file, 'w') as file:
                print("Файл не найден. Создан новый")