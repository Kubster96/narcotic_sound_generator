import math
from random import randint


class Note:

    note = [0, 0, 0, 0]
    scale = []
    key = 0
    octaves = 0

    maxLenght = 0

    time = 0
    pitch = 0
    velocity = 0
    duration = 0

    def generate_note(self):

        durations = []
        i = 0
        while 2**i <= self.maxLenght:
            durations += [2**i]
            i += 1

        self.duration = durations[randint(0, len(durations)-1)]

        pitches = []
        print(self.scale)
        if self.octaves == 3:
            for i in range(0, len(self.scale)-1):
                pitches += [int(self.scale[i])-12]
        if self.octaves == 2:
            for i in range(0, len(self.scale) - 1):
                pitches += [int(self.scale[i])+12]
        if self.octaves == 1:
            for i in range(0, len(self.scale) - 1):
                pitches += [int(self.scale[i])]

        self.pitch = 60 + self.key + pitches[randint(0, len(pitches)-1)]
        self.velocity = 127
        self.note[0] = self.time
        self.note[1] = self.pitch
        self.note[2] = self.velocity
        self.note[3] = self.duration







