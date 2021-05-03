from bar import Bar


class Song:
    notes = []
    scale = []
    number_of_bars = 0
    key = 0
    time = 0
    meter = 0
    octaves_range = 0

    def __init__(self, number_of_bars, scale_list, tempo, key, meter, octaves_range):
        self.number_of_bars = number_of_bars
        self.scale = scale_list
        self.tempo = tempo
        self.key = key
        self.meter = meter
        self.octaves_range = octaves_range

    def generate_song(self):
        while self.number_of_bars > 0:
            bar = Bar(self.scale, self.key, self.time, self.meter, self.octaves_range)
            bar.generate_tact()

            self.notes = self.notes + bar.notes
            self.time += self.meter
            self.number_of_bars -= 1


