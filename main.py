import pyglet
import os
import pygame
import time
import webbrowser

pygame.init()
pygame.mixer.music.load("beep1.mp3")
pygame.mixer.music.play()
time.sleep(1)

print("Hi master, I am R2D2, an astro-droid from Naboo.")
print("Type some cammands and I will execute them.")

def prompt():
    cmd = raw_input("R2D2: ")

    if cmd == "Play message":
        webbrowser.open("https://www.youtube.com/watch?v=5cc_h5Ghuj4") 
	prompt()

    if cmd == "Hi":
	pygame.init()
	pygame.mixer.music.load("beepsml.mp3")
	pygame.mixer.music.play()
        time.sleep(1)

	prompt()

    if cmd == "Thanks R2":
	print("BYE")

prompt()
