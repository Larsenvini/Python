import pyfiglet
import sys
import random

def main():
    available_fonts = pyfiglet.FigletFont.getFonts()

    if len(sys.argv) == 1:
        font = random.choice(available_fonts)

    elif len(sys.argv) == 3:
        if a


