# Alarm Clock
# A simple clock where it plays a sound after X number of
# minutes/seconds or at a particular time.

import pygame
import time

pygame.init()

def play_sound():
    sound_wav = pygame.mixer.Sound("gameover.wav")
    channel = sound_wav.play()
    while channel.get_busy():
        pygame.time.delay(100)

sound_wav = pygame.mixer.Sound("gameover.wav")

def main():
    print """
    1. Play sound after x seconds
    2. Play sound after y minutes
    try:
        wait_seconds = int(raw_input("Wait how many seconds? "))

        if wait_seconds < 0:
            print "Must be greater or equal than 0"
            exit()

        start = time.time()
        end = time.time()

        while (end - start) < wait_seconds:
            end = time.time()

        play_sound()
    except ValueError:
        print "Invalid input."


if __name__ == "__main__":
    main()
