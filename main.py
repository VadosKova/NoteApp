from NoteOperations import NoteOperations

operations = NoteOperations()

while True:
    print("\n---NoteApp---")
    print("1. Add note")
    print("2. Delete note")
    print("3. Show note by ID")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        id = input("Enter ID: ")
        title = input("Enter title: ")
        content = input("Enter content: ")
        operations.add_note(id, title, content)

    elif choice == "2":
        id = input("Enter the ID to delete note: ")
        operations.delete_note_by_id(id)

    elif choice == "3":
        operations.show_note_by_id()

    elif choice == "4":
        print("End")
        break

    else:
        print("Error")