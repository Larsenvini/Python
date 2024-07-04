import pyfiglet
import sys
import random

def main():
    available_fonts = pyfiglet.FigletFont.getFonts()

    if len(sys.argv) == 1:
        font = random.choice(available_fonts)

    elif len(sys.argv) == 3:
        if sys.argv[1] in ['-f', '--font'] and sys.argv[2] in available_fonts:
            font = sys.argv[2]
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Usage: figlet.py [-f FONT_NAME]")

    text = input("Input: ")

    figlet = pyfiglet.Figlet(font=font)

    print(figlet.renderText(text))

if __name__ == '__main__':
        main()

