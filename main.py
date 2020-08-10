from PIL import Image
import numpy as np
import math
from tkinter import colorchooser


def choose_color():
    rgb = []
    color = colorchooser.askcolor()
    for value in color[0]:
        rgb.append(math.floor(value))

    return rgb


def main():
    print("Choose a color in the dialog")
    rgb = choose_color()

    print("Got color: {}".format(rgb))

    name = input("Enter file name to save (will be saved as png): ")

    img = Image.open("base.png")
    img = img.convert("RGBA")

    data = np.array(img)
    red, green, blue, alpha = data.T

    purple_areas = (red == 190) & (green == 61) & (blue == 237)
    data[..., :-1][purple_areas.T] = rgb

    img2 = Image.fromarray(data)
    img2.save(name + ".png")


main()
