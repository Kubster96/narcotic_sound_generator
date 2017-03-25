"""from miditime.miditime import MIDITime
from Note import Note

# Instantiate the class with a tempo (120bpm is the default) and an output file destination.
myMidi = MIDITime(120, 'myFile.mid')

# [time, pitch, velocity, duration]
midiNotes = []

print(midiNotes)

# Add a track with those notes
myMidi.add_track(midiNotes)

# Output the .mid file
myMidi.save_midi()"""

import argparse

parser = argparse.ArgumentParser(description='Give some options!')
parser.add_argument('tempo', help="Give the tempo of the song!", type=int)
parser.add_argument('key', help="Give the key of the song!", type=int)
parser.add_argument('scale', help="Give the scale of the song!", type=int)
parser.add_argument('tactNumber', help="Give the tact number!", type=int)

args = parser.parse_args()

tempo = args.tempo
key = args.key
scale = args.scale
tactNumber = args.tactNumber

print(tempo)
print(key)
print(scale)
print(tactNumber)
