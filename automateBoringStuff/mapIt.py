#! python3
# mapIt.py - launches a map in the browser using an address from cli or clipboard
import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # get address from cli
    address = ' '.join(sys.argv[1:])
else:
    # get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
