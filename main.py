from PIL import Image
import numpy as np
import math
import random
from tkinter import colorchooser
import os


def choose_color():
    rgb = []
    color = colorchooser.askcolor()
    for value in color[0]:
        rgb.append(math.floor(value))

    return rgb


def change_color(data, color):
    red, green, blue, alpha = data.T

    purple_areas = (red == 190) & (green == 61) & (blue == 237)
    data[..., :-1][purple_areas.T] = color


def random_color():
    if not os.path.exists("random_skins"):
        os.mkdir("random_skins")

    save_dir = os.path.curdir + "/random_skins/"

    amount = int(input("Enter number of random skins to make: "))

    img = Image.open("base.png")
    img = img.convert("RGBA")

    for i in range(amount):
        rgb = [random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)]

        name = rgb2hex(rgb[0], rgb[1], rgb[2])

        data = np.array(img)
        change_color(data, rgb)

        img2 = Image.fromarray(data)
        img2.save(save_dir + name + ".png")
        print("Saved as {}.png".format(name))


def rgb2hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


def custom_color():
    print("Choose a color in the dialog")
    rgb = choose_color()

    print("Got color: {}".format(rgb))

    name = input("Enter file name to save (will be saved as png): ")

    img = Image.open("base.png")
    img = img.convert("RGBA")

    data = np.array(img)
    change_color(data, rgb)

    img2 = Image.fromarray(data)
    img2.save(name + ".png")

    print("Saved as {}.png".format(name))


def main():
    while True:
        print("1. Choose your own color")
        print("2. Generate random colors")
        option = input("Enter selection: ")

        if option == "1":
            custom_color()
            break
        elif option == "2":
            random_color()
            break


main()
