from pygame import mixer
from datetime import datetime
from time import time

def musicwater(musicname,stopper):
    mixer.init()
    mixer.music.load(musicname)
    mixer.music.play()

    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break


def log_water(msg):
    with open("waterlog","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

def log_eye(msg):
    with open("eyelog","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

def log_physical(msg):
    with open("physicalactivitylog","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    # musicwater('Shape of You.mp3', 'stop')
    init_water = time()
    init_eye = time()
    init_physical = time()
    watersec = 5
    eyesec = 20
    physicalsec = 60
    while True:
        if time() - init_water > watersec:
            print("water Drinking Time.Enter 'stop' to stop the alarm")
            musicwater('Shape of You.mp3', 'stop')
            init_water = time()
            log_water("Drank water at")

        if time() - init_eye > eyesec:
            print("Eye Excercies Time.Enter 'stop' to stop the alarm")
            musicwater('Buzz.mp3', 'stop')
            init_eye = time()
            log_eye("Eye Excercies at")


        if time() - init_physical > physicalsec:
            print("Physical Excercies Time.Enter 'stop' to stop the alarm")
            musicwater('Tera Yaar Hoon Main.mp3', 'stop')
            init_physical = time()
            log_physical("Physical Excercies at")


