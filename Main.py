import argparse
from Song import Song
from miditime.miditime import MIDITime
import sys

parser = argparse.ArgumentParser(description='Give some options!')
parser.add_argument('tempo', help="Give the tempo of the song!", type=int)
parser.add_argument('key', help="Give the key of the song!", type=int)
parser.add_argument('scale', help="Give the scale of the song!", type=int)
parser.add_argument('tactNumber', help="Give the tact number!", type=int)
parser.add_argument('metrum', help="Give the metrum!", type=int)
parser.add_argument('octaves', help="Give the range", type=int)
parser.add_argument('songName', help="Give song name", type=str)
args = parser.parse_args()

tempo = args.tempo
key = args.key
scale = args.scale
tactNumber = args.tactNumber
metrum = args.metrum
octaves = args.octaves
songName = args.songName

with open('scales.txt', 'r') as f:
    x = f.readlines()


# here we deal with scale there are many scales in scales.txt we can choose any

if scale > len(x):
    print("Scale number is out of range")
    sys.exit()


# here we deal with key

if key > 11 or key < 0:
    print("Key number should be between 0 - 11")
    sys.exit()


# here we deal with metrum

if metrum < 1 or metrum > 7:
    print("Metrum should be between 1 - 7")
    sys.exit()


# here we deal with tempo

if tempo < 1 or tempo > 300:
    print("Tempo should be between 1 - 300")
    sys.exit()


# here we deal with tact Number

if tactNumber < 1 or tactNumber > 50:
    print("Tact should be between 1 - 50")
    sys.exit()

# here we deal with octaves number

if octaves < 1 or octaves > 3:
    print("Number of octaves should be between 1 - 3")
    sys.exit()


scaleList = x[scale-1].replace('\n', '')
scaleList = scaleList.split(", ")


tempo *= 4
metrum *= 4
song = Song()
song.numberOfTacts = tactNumber
song.scale = scaleList
song.tempo = tempo
song.key = key
song.metrum = metrum
song.octaves = octaves

songName += ".mid"
song.generate_song()
myMidi = MIDITime(tempo, songName)
midiNotes = song.song
myMidi.add_track(midiNotes)
myMidi.save_midi()
