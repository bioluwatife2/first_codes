def read_notes():
   seen_notes = {}
   notes = open("Note1.txt", "r").readlines()
   if len(notes) > 0:
      for note in notes:
         title= note.split(": ")[0]
         body = note.split(": ")[1]
         seen_notes[title] = body
   else:
      print("No notes found here")
   return seen_notes
   
def create_note(title, body):
   notes = {}
   note_file = open("Note1.txt", "a")
   notes[title] = body
   for title,body in notes.items():
      note_file.write(title+": " + body+"\n")

def delete_note(title_id):
   """
   Delete a note in the note text using the title_id
   @param title
   """
   # Create a new dictionary to add updated items
   updated_notes = {}
   try:
      # Read available notes
      notes = read_notes()
      # Open file to rewrite contents
      note_file = open("Note1.txt", "w")
      # Loop throught the notes dictionary
      for title, body in notes.items():
         # Rewrite all the contents
         # Don't add the title and body if it was specified
         if title != title_id:
            # Update the updated_notes dictionary
            updated_notes[title] = body
      # Loop through the update_notes dict to get the title & body items
      for updated_title, updated_body in updated_notes.items():
         # Write each updated_title and updated_body to note_file
         note_file.write(updated_title+": "+updated_body)


         # if title.strip("\n") and body.strip("\n") != title and body:
            # note_file.write(note)
   except:
      print("Note not found")
   

def update_note(title, body):
    """
    Update note
    """
    updated_notes = {}
    try:
        notes = read_notes()
        if title not in notes.keys():
            print("Note does not exist")
        note_file = open("Note1.txt","w")
        for t, b in notes.items():
            updated_notes[t] = body
        for updated_note_title, updated_note_body in updated_notes.items():
            note_file.write(updated_note_title+": "+updated_note_body)
    except:
        print("Note not found")


if __name__ == "__main__":
    print("Please import this module")