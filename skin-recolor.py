from PIL import Image
from PIL import ImageColor
import numpy as np
import math
import random
from tkinter import colorchooser
import os


class Skin:
    def __init__(self, data, color):
        self.data = data
        self.color = color


def choose_color():
    rgb = []
    color = colorchooser.askcolor()
    for value in color[0]:
        rgb.append(math.floor(value))

    return rgb


def recolor_skin(data, color):
    red, green, blue, alpha = data.T

    color_as_rgb = color_to_rgb(color)

    purple_areas = (red == 190) & (green == 61) & (blue == 237)
    data[..., :-1][purple_areas.T] = color_as_rgb


def save_skin_data_to_file(skin: Skin, file_name=None):
    if not os.path.exists("saved_skins"):
        os.mkdir("saved_skins")

    save_dir = os.path.curdir + "/saved_skins/"

    if file_name is None:
        file_name = hex_string(skin.color) + ".png"

    img = Image.fromarray(skin.data)
    img.save(save_dir + file_name)


def get_random_recolored_skin_data():
    color = random.randrange(0, 2**24)

    return get_recolored_skin_data(color)


def get_recolored_skin_data(color):
    """
    Gets the data of a recolored skin of the specified color

    :param color: Color represented as a number
    :return: numpy array representing the colored skin
    """
    img = Image.open("base.png")
    img = img.convert("RGBA")

    imgarray = np.array(img)
    recolor_skin(imgarray, color)

    return Skin(imgarray, color)


def hex_string(color):
    hex_color = hex(color)
    return f"#{hex_color[2:]}"


def color_to_rgb(color):
    hex_str = hex_string(color)
    return ImageColor.getcolor(hex_str, "RGB")


def rgb2hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


# This method is very likely broken
def _custom_color():
    print("Choose a color in the dialog")
    rgb = choose_color()

    print("Got color: {}".format(rgb))

    name = input("Enter file name to save (will be saved as png): ")

    img = Image.open("base.png")
    img = img.convert("RGBA")

    data = np.array(img)
    recolor_skin(data, rgb)

    img2 = Image.fromarray(data)
    img2.save(name + ".png")

    print("Saved as {}.png".format(name))


if __name__ == "__main__":
    while True:
        print("1. Choose your own color")
        print("2. Generate random colors")
        option = input("Enter selection: ")

        if option == "1":
            _custom_color()
            break
        elif option == "2":
            amount = int(input("Enter number of random skins to make: "))
            for i in range(amount):
                skin = get_random_recolored_skin_data()
                save_skin_data_to_file(skin)

            break
