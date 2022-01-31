import os
import json
import glob
import time
from pygame import mixer


def playSong(mp3):
    mixer.init()
    mixer.music.load(mp3)
    #mixer.music.set_volume(0.7)
    mixer.music.play()
    time.sleep(mixer.Sound(mp3).get_length())
    mixer.music.stop()


def labelSong(song, label):
    if label.lower() == "c":
        song["label"] = "Clean"
    elif label.lower() == "n":
        song["label"] = "Noisy"
    else:
        print("Invalid input!")


mp3_files = glob.iglob("**/*.mp3", recursive=True)
songs = []

for mp3 in mp3_files:
    name = os.path.basename(mp3)
    print("Playing {}...".format(name))
    playSong(mp3)
    song = {
        "song": name,
        "label": ""
    }
    label = input("Was this song Clean or Noisy? (c/n) ")
    labelSong(song, label)
    songs.append(song)

with open("song_labels.json", "w") as outfile:
    json.dump({"songs": songs}, outfile)