import argparse
from song import Song
from miditime.miditime import MIDITime
import sys


def main():
    parser = argparse.ArgumentParser(description='Provide parameters!')
    parser.add_argument('tempo', help="Provide tempo of the song!", type=int)
    parser.add_argument('key', help="Provide key of the song!", type=int)
    parser.add_argument('scale', help="Provide scale of the song!", type=int)
    parser.add_argument('number_of_bars', help="Provide number of bars!", type=int)
    parser.add_argument('meter', help="Provide the meter of the song!", type=int)
    parser.add_argument('octaves_range', help="Provide the range of octaves", type=int)
    parser.add_argument('song_name', help="Provide song name", type=str)
    args = parser.parse_args()

    tempo = args.tempo
    key = args.key
    scale = args.scale
    number_of_bars = args.number_of_bars
    meter = args.meter
    octaves_range = args.octaves_range
    song_name = "resources/" + args.song_name + ".mid"

    with open('resources/scales.txt', 'r') as f:
        x = f.readlines()

        # scales are in scales.txt file
        if scale > len(x):
            print("Scale number is out of range")
            sys.exit()

    if key > 11 or key < 0:
        print("Key number should be between 0 - 11")
        sys.exit()

    if meter < 1 or meter > 7:
        print("Meter should be between 1 - 7")
        sys.exit()

    if tempo < 1 or tempo > 300:
        print("Tempo should be between 1 - 300")
        sys.exit()

    if number_of_bars < 1 or number_of_bars > 50:
        print("Number of bars should be between 1 - 50")
        sys.exit()

    if octaves_range < 1 or octaves_range > 3:
        print("Number of octaves should be between 1 - 3")
        sys.exit()

    scale_list = x[scale-1].replace('\n', '')
    scale_list = scale_list.split(", ")

    tempo *= 4
    meter *= 4
    song = Song(number_of_bars, scale_list, tempo, key, meter, octaves_range)

    song.generate_song()

    midi = MIDITime(tempo, song_name)
    song_notes = song.notes
    midi.add_track(song_notes)
    midi.save_midi()


if __name__ == "__main__":
    main()
