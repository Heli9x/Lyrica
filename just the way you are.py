import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\n""The way you are", 0.16),
        ("The way you are", 0.19),
        ("Girl you're amazing", 0.11),
        ("Just the way you are", 0.14),
        ("When i see your face""\n", 0.15),
        ("There's not a thing", 0.09),
        ("That i would change", 0.12),
        ("'Cause you're amazing", 0.10),
        ("Just the way", 0.15),
    ]
    
    delays = [0.3, 4.3, 9.6, 12.5, 18.0, 22.8, 25.0, 27.6, 30.3]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()