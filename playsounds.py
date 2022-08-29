#!/usr/bin/python3

from playsound import playsound
number_of_processes = 4


def play_bang():
    playsound("sounds/heavy-thud.wav")


def multi_bang(count):
    for i in range(count):
        play_bang()


def growl():
    playsound("sounds/cthulhu-growl.wav")


def creepy():
    playsound("sounds/creepy.wav")


if __name__ == "__main__":
    multi_bang(number_of_processes)
