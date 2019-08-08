#!/usr/bin/env python3

from math import floor
from PIL import Image
import shutil
import sys

def get_output_size(x_dim, y_dim, aspect_ratio):
    if aspect_ratio == 1:
        return (y_dim, y_dim)
    elif aspect_ratio > 1:
        return (x_dim, floor(x_dim / aspect_ratio))
    else:
        return (floor(y_dim * aspect_ratio), y_dim)

def pixel(red, green, blue):
    sys.stdout.write(f"\x1b[38;2;{red};{green};{blue}m██\x1b[0m")

if __name__ == "__main__":
    version_string = '.'.join([str(x) for x in list(sys.version_info)[:3]])

    print(sys.argv[0] + ": Running in Python " + version_string  + " @ " + sys.executable)

    x_dim, y_dim = list(shutil.get_terminal_size())

    print(sys.argv[0] + ": Terminal size is " + str(x_dim) + " by " + str(y_dim))

    im = Image.open("bun.jpg")
    
    width, height = im.size
    aspect_ratio = width / height

    print(sys.argv[0] + ": image size is " + str(width) + " by " + str(height) + " with ratio " + str(aspect_ratio))

    x_dim, y_dim = get_output_size(floor(x_dim / 2), y_dim - 1, aspect_ratio)

    print(sys.argv[0] + ": output size is " + str(x_dim) + " by " + str(y_dim))

    im = im.resize((x_dim, y_dim))

    for y in range(0, y_dim):
        for x in range(0, x_dim):
            r, g, b = im.getpixel((x, y))
            pixel(r, g, b)
        sys.stdout.write("\n")

