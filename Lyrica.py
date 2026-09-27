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
    #delays = [0.3, 3.2, 5.8, 8.3, 10.6, 15.5, 20.8, 23.4, 26.0, 28.5, 31.2, 36.0]
    song = load_lyrics("intoyouxbye.json")
    sing_song(song)
    #sing_song(lyrics)
    

