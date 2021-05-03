import math
from random import randint


class Note:
    note = [0, 0, 0, 0]

    max_length = 0
    scale = []
    time = 0
    key = 0
    octaves_range = 0

    def __init__(self, length, scale, time, key, octaves_range):
        self.max_length = length
        self.scale = scale
        self.time = time
        self.key = key
        self.octaves_range = octaves_range

    def generate_note(self):
        durations = []
        i = 0
        while 2**i <= self.max_length:
            durations += [2**i]
            i += 1

        duration = durations[randint(0, len(durations)-1)]

        pitches = []

        if self.octaves_range == 3:
            for i in range(0, len(self.scale)-1):
                pitches += [int(self.scale[i])-12]
        if self.octaves_range >= 2:
            for i in range(0, len(self.scale) - 1):
                pitches += [int(self.scale[i])+12]
        if self.octaves_range >= 1:
            for i in range(0, len(self.scale) - 1):
                pitches += [int(self.scale[i])]

        pitch = 60 + self.key + pitches[randint(0, len(pitches)-1)]
        velocity = 127

        self.note[0] = self.time
        self.note[1] = pitch
        self.note[2] = velocity
        self.note[3] = duration







