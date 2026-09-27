import time
import sys
from threading import Thread, Lock
import json

lock = Lock()
def animate_text(text:str, speed:float):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        print()

def load_lyrics(filename:str):
    with open(filename, "r") as f:
        lyrics = json.load(f)

    return lyrics

def sing_lyric(text:str, delay:float, speed:float):
    time.sleep(delay)
    animate_text(text, speed)

def sing_song(lyrics:list):
    """"Expected format of lyrics data
    lyrics = [(n_line:str, speed:float, delay:float)...]
    """
    threads = []
    for line in lyrics:
        text, speed, delay = line
        t = Thread(target=sing_lyric, args=(text, delay, speed))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    lyrics = [
        ("\nDon't listen to them", 0.07, 0.3),
        ("Cause what do they know", 0.05, 3.2),
        ("We need each other", 0.07, 5.8),
        ("to have, to hold", 0.07, 8.3),
        ("They'll see in time", 0.08, 10.6),
        ("I know\n", 0.07, 15.5),
        ("When destiny calls you", 0.07, 20.8),
        ("you must be strong", 0.07, 23.4),
        ("I may not be with you", 0.07, 26.0),
        ("But you've got to hold on", 0.07, 28.5),
        ("They'll see in time", 0.08, 31.2),
        ("I know", 0.07, 36.0),
    ]
    #delays = [0.3, 3.2, 5.8, 8.3, 10.6, 15.5, 20.8, 23.4, 26.0, 28.5, 31.2, 36.0]
    song = load_lyrics("intoyouxbye.json")
    sing_song(song)
    #sing_song(lyrics)
    

