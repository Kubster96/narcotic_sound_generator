from Note import Note


class Tact:

    notes = []
    scale = []
    key = 0
    time = 0
    length = 0
    octaves = 0

    def generate_tact(self):

        while self.length > 0:
            note = Note()
            note.maxLenght = self.length
            note.scale = self.scale
            note.time = self.time
            note.key = self.key
            note.octaves = self.octaves

            note.generate_note()
            newNote = list(note.note)
            self.notes.append(newNote)

            self.time += note.duration
            self.length -= note.duration



