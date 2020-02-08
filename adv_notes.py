
def read_notes():
    seen_notes = {}
    notes = open("note.txt", "r").readlines()
    # return notes
    if len(notes) > 0:
        for note in notes:
            title = note.split(": ")[0]
            body = note.split(": ")[1]
            seen_notes[title] = body
    else:
        print("No notes found")
    return seen_notes

def create_note(title,body):
    notes = {}
    note_file = open("note.txt","a")
    notes[title] = body
    for title, body in notes.items():
        note_file.write(title+": "+body+"\n")


def delete_note():
    pass

def main():
    print("Welcome to Note Taker!\n")
    notes = read_notes()
    if len(notes) == 0:
        print("First Time!\nCreate New Note")
        title = input("Title: ")
        body = input("Body: ")
        create_note(title,body)
    print("\nCreate New Note")
    title = input("Title: ")
    body = input("Body: ")
    create_note(title,body)

if __name__ == "__main__":
    while True:
        print(read_notes())
        main()
