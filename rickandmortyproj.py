import tkinter as tk
import random
from PIL import Image, ImageTk
import json
import ssl
import urllib
import requests
import io
import sys
import os

random_char = random.randint(1, 494)
print(random_char)
base_url = "https://rickandmortyapi.com/api/"
character_url = base_url + "character/"
ssl._create_default_https_context = ssl._create_unverified_context
is_clicked = False


class Character():

    def get_all():
        return requests.get(character_url).json()

    def get(id=None):
        if id == None:
            print("You need to pass id of character to get output.")
            print("To get list of all characters, use getall() method.")
            return
        return requests.get(character_url + str(id)).json()

    def new_char(id=random_char):
        if id == None:
            print("You need to pass id of character to get output.")
            print("To get list of all characters, use getall() method.")
            return
        return  requests.get(character_url + str(id)).json()


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)


mainWindow = tk.Tk()

data = Character.get(random_char)
url_link = data['image']
names = data['name']
raw_data = urllib.request.urlopen(url_link).read()
im = Image.open(io.BytesIO(raw_data))
char_image = ImageTk.PhotoImage(im)



# color
bg_label = _from_rgb((191, 121, 22))
bg_title = _from_rgb((64, 40, 7))
bg_canvas_desc= _from_rgb((191, 121, 22))
bg_main = _from_rgb((255, 162, 29))
fg_title = _from_rgb((0, 0, 0))


mainWindow.geometry("640x480")
mainWindow.title("Rick and Morty")
mainWindow.config(bg=bg_main)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=1)
mainWindow.rowconfigure(2, weight=1)

# canvas for api photo 300 x 300
photo_canvas = tk.Canvas(mainWindow, background='blue', width=300, height=300)
photo_canvas.grid(row=1, column=1)
photo_canvas.config(bg=bg_canvas_desc)


# canvas for API text
description_char = tk.Canvas(mainWindow, background='blue', width=300, height=300, relief="flat",
                             borderwidth=0, highlightthickness=0)
description_char.grid(row=0, column=0, rowspan=3)
description_char.config(bg=bg_canvas_desc)
description_char.rowconfigure(0, weight=1)
description_char.rowconfigure(1, weight=1)
description_char.rowconfigure(2, weight=1)
description_char.rowconfigure(3, weight=1)
description_char.rowconfigure(4, weight=1)
description_char.rowconfigure(5, weight=1)

button_canvas = tk.Canvas(description_char, width=30, height=30,  relief='sunken')
button_canvas.grid(row=4, column=0)


# title
main_title = tk.Label(mainWindow, text="RICK AND MORTY RANDOMISER",
                      font=('Helvetica', 18, 'bold'), bg=bg_main, fg=fg_title)
main_title.grid(row=0, column=1)

# Character details from API
character_name = tk.Label(description_char, text=f"NAME: {data['name']}", bg=bg_label)
character_name.grid(row=0, column=0, sticky='w')

character_species = tk.Label(description_char, text=f"SPECIES: {data['species']}", bg=bg_label)
character_species.grid(row=1, column=0, sticky='w')

character_gender = tk.Label(description_char, text=f"GENDER: {data['gender']}", bg=bg_label)
character_gender.grid(row=2, column=0, sticky='w')

character_location = tk.Label(description_char, text=f"LOCATION: {data['location']['name']}", bg=bg_label)
character_location.grid(row=3, column=0, sticky='w')

# randomise button for api
"""Need to find a better way to randomise the char instead of restarting window"""
random_char_button = tk.Button(button_canvas, text="Random Character!", command=restart_program)
random_char_button.grid(row=4, column=0, sticky='s')

label1 = tk.Label(photo_canvas, image=char_image, borderwidth=0, highlightthickness=0)
label1.grid(row=1, column=1)


mainWindow.mainloop()


