#!/usr/bin/env python3

# Snail Race - Who's going to win?

import random
import time

# Info that pops at the start of the script

def info():
        print('''
        -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-
        |                                   |
        |  VEM VINNER OCH VEM FÖRSVINNER?!  |
        |   Här tävlar din snigel mot en    |
        |   vältränad racersnigel. Skriv    |
        |  in vad din snigel har för namn   |
        |        och starta tävlingen!      |
        |                                   |
         -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.- \n''')

# Reads the name of the snail
def read_name():
        name = input("Name your racing snail: ")
        return name

# Simulates the race between the snails
def race():
        snailtrack1 = 0
        snailtrack2 = 0
        print("\n Ready... Steady.. GO!!\n")
        while snailtrack1 < DISTANCE and snailtrack2 < DISTANCE:
                snailtrack1 += random.randrange(5)
                snailtrack2 += random.randrange(5)
        return snailtrack1, snailtrack2

# Showing the race, lenght and name of the snails
def print_track(snailname, lenght):
        print(snailname.rjust(12) + ":", end=" ")
        for i in range(1,lenght):
                print("-.", end=" ")
        print("_@ノ")

# Showing the winner of the race
def winner(lenght1, lenght2, name1, name2="Racing-Snail"):
        print("\n")
        if lenght1 >= DISTANCE and lenght2 >= DISTANCE:
                print("\n OMG both snails on first place! \n")
        else:
                if lenght1 >= DISTANCE:
                        print("n OMG the newbie is on fire!", name1, "is the winner!")
                else:
                        print("\n", name2, 'is the winner and', name1, 'didnt have a chance!')

#Head program
def headprogram():
        info()
        your_snail_name = read_name()
        snailtrack1, snailtrack2 = race()
        print_track(your_snail_name, snailtrack1)
        print_track("Racing-Snail", snailtrack2)
        winner(snailtrack1, snailtrack2, your_snail_name, "Racing-Snail")

DISTANCE = 60
headprogram()
