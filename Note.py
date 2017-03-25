class Note:

    note = [0, 0, 0, 0]

    def set_time(self, time):
        self.note[0] = time

    def set_duration(self, duration):
        self.note[3] = duration

    def set_pitch(self, pitch):
        self.note[1] = pitch

    def get_note(self):
        return self.note

