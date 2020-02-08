# Make sure to import specific functions to use in the module
# from practice import *

from practice import create_note, read_notes, delete_note, update_note

def create():
    title = input("Title: ")
    body = input("Body: ")
    create_note(title,body)

def read():
    notes = read_notes()
    for t, b in notes.items():
        print("Title: "+t+" Body: "+b)
        # print()
    return notes
    

# def remove(title, body):
    # delete_note(title)

def remove(title):
    delete_note(title)

def update(title, body):
    update_note(title, body)

def main():
    print("Welcome to Note Taker!\n")
    notes = read_notes()
    # Check if length of notes is less than 1
    # Only check for note length, the rest of the methods
    # Should be outside to avoid infinite loop
    if len(notes) < 1:
        print("First Time!\n Create new Note")
        # To save time, just call the create() function
        create()
        # title = input("Title: ")
        # body = input("Body: ")
        # create_note(title,body)
    user = input('What do you want to do? Create New Task(create)\nRead Tasks(read)\nUpdate Task(pathc)\nDelete Task(delete)\n: ').lower()
    if user == 'create':
        create()
    elif user == 'read':
        read()
    elif user == 'delete':
        read()
        note_id = input('Please input the note to be deleted: ')
        remove(note_id)
    elif user == 'patch':
        read()
        print("Update note id and body by changing the title and or body")
        title = input("Title(must exist): ")
        body = input("Body: ")
        update(title, body)
    else:
        print('No command received')

while True:
    # print(read_notes())
    read()
    main()
