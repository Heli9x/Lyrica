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
        ("\n""Looking in your eyes I", 0.09),
        ("See a paradise", 0.09),
        ("This world that I've found", 0.07),
        ("Is too good to be true", 0.09),
        ("Standing here beside you", 0.10),
        ("Want so much to give you", 0.10),
        ("This love in my heart", 0.10),
        ("That I'm feeling for you", 0.10),
    ]
    
    delays = [0.3, 3.3, 5.4, 8.0, 10.5, 12.4, 15.4, 17.0]
    
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