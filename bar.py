from note import Note


class Bar:
    notes = []
    scale = []
    key = 0
    time = 0
    length = 0
    octaves_range = 0

    def __init__(self, scale, key, time, meter, octaves_range):
        self.scale = scale
        self.key = key
        self.time = time
        self.length = meter
        self.octaves_range = octaves_range

    def generate_tact(self):
        while self.length > 0:
            note = Note(self.length, self.scale, self.time, self.key, self.octaves_range)

            note.generate_note()
            new_note = list(note.note)
            self.notes.append(new_note)

            self.time += note.duration
            self.length -= note.duration



