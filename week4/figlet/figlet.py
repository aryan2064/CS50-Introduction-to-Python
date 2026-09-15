from sys import argv, exit
from pyfiglet import Figlet
from random import choice

figlet = Figlet()

fonts = figlet.getFonts()

if len(argv) == 1:
    figlet.setFont(font=choice(fonts))

elif len(argv) == 3 and argv[1] in ("-f", "--font") and argv[2] in fonts:
    figlet.setFont(font=argv[2])

else:
    exit("Invalid usage")

s = input("Input: ")

print(f"Output: {figlet.renderText(s)}")
