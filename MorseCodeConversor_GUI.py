from tkinter import *
import tkinter.messagebox as messagebox

# Function to convert plain text into Morse code
def text_conversor(plane_text):
    text_converted = ""
    for char in plane_text:
        text_converted += dictionary.get(char, "") + "/"
    conversor_show["text"] = text_converted[:-1] 

# Function to convert Morse code into plain text
def morse_conversor(morse_text):
    morse_converted = ""
    inverse = {v: k for k, v in dictionary.items()}
    for code in morse_text.split("/"):
        morse_converted += inverse.get(code, "")
    mconversor_show["text"] = morse_converted

# Function to clear the example text when the user starts typing
def clear_placeholder(event):
    if entry.get() == "Type the text to be converted":
        entry.delete(0, END)

# Function to clear the example text when the user starts typing
def clear_placeholder_morse(event):
    if mentry.get() == "Morse example > /.../---/...":
        mentry.delete(0, END)

# Function to adjust the Entry size based on the text size
def adjust_entry_size():
    entry.config(width=len(entry.get()))
    mentry.config(width=len(entry.get()))

# Function to copy the text displayed in a widget
def copy_text(widget):
    text = widget["text"]
    window.clipboard_clear()
    window.clipboard_append(text)
    messagebox.showinfo("Copied", "The text has been copied to the clipboard.")

# Dictionary with letters and their respective Morse code symbols
dictionary = {
    '{': '{', '}': '}', ' ': ' ', 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
    'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '-': '-....-', '_': '..--.-', '"': '.-...', '$': '...-..-', '@': '.--.-.', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}

window = Tk()
window.title("MorseCodeConversor")

width = 500
height = 200

# System resolution
width_screen = window.winfo_screenwidth()
height_screen = window.winfo_screenheight()

# Window position
posx = width_screen // 2 - width // 2
posy = height_screen // 2 - height // 2

# Set the window geometry
window.geometry("%dx%d+%d+%d" % (width, height, posx, posy))

# Change icon
window.iconbitmap("Images\icon.ico")

# Base text
orientation_text = Label(window, text='Welcome to the Morse Code Converter, it is easy to use and practical, I hope you enjoy it.', padx=10, pady=10)
orientation_text.grid(column=0, row=0)

# Buttons
conversor = Button(window, text="Converter", command=lambda: text_conversor(entry.get().upper()))
conversor.grid(column=1, row=1)
conversor_show = Label(window, text='')
conversor_show.grid(column=0, row=4)

mconversor = Button(window, text="Converter", command=lambda: morse_conversor(mentry.get()))
mconversor.grid(column=1, row=5)
mconversor_show = Label(window, text='')
mconversor_show.grid(column=0, row=7)

# Buttons to copy the converter result
copy_button = Button(window, text="Copy", command=lambda: copy_text(conversor_show))
copy_button.grid(column=0, row=2)
mcopy_button = Button(window, text="Copy", command=lambda: copy_text(mconversor_show))
mcopy_button.grid(column=0, row=6)

# Input
entry = Entry(window)
entry.grid(column=0, row=1)
entry.insert(0, "Type the text to be converted")  # Sets the example text

mentry = Entry(window)
mentry.grid(column=0, row=5)
mentry.insert(0, "Morse example > /.../---/...")  # Sets the example text

# Calls the adjust_entry_size function to adjust the width initially
adjust_entry_size()

# Links the clear_placeholder function to the click event in the input
entry.bind("<Button-1>", clear_placeholder)
mentry.bind("<Button-1>", clear_placeholder_morse)

window.mainloop()