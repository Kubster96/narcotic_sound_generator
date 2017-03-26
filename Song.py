from Tact import Tact


class Song:

    song = []
    scale = []
    numberOfTacts = 0
    key = 0
    time = 0
    metrum = 0
    octaves = 0

    def generate_song(self):
        while self.numberOfTacts > 0:
            tact = Tact()
            tact.scale = self.scale
            tact.key = self.key
            tact.time = self.time
            tact.length = self.metrum
            tact.octaves = self.octaves
            tact.generate_tact()

            self.song = self.song + tact.notes
            self.time += self.metrum
            self.numberOfTacts -= 1


