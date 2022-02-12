#!/usr/bin/env python
# Import Modules
import os
import pygame as pg

if not pg.font:
    print("Warning, fonts disabled")
if not pg.mixer:
    print("Warning, sound disabled")

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")


# functions to create our resources
def load_image(name, colorkey=None, scale=1):
    fullname = os.path.join(data_dir, name)
    image = pg.image.load(fullname)
    
    
    return image, image.get_rect()

def load_sound(name):
    class NoneSound:
        def play(self):
            pass

    if not pg.mixer or not pg.mixer.get_init():
        return NoneSound()

    fullname = os.path.join(data_dir, name)
    sound = pg.mixer.Sound(fullname)

    return sound

# classes for our game objects
class Fist(pg.sprite.Sprite):
    """moves a clenched fist on the screen, following the mouse"""
    
    
class Football(pg.sprite.Sprite):
    """moves a football critter across the screen. it can spin the
    football when it is punched."""
    

def main():
    """this function is called when the program starts. it initializes everything it needs, then runs in
    a loop until the function returns."""
    # Initialize Everything
    pg.init()


    pg.quit()


# Game Over

# this calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()