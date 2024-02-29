import customtkinter 
import tkinter as tk
from tkinter import messagebox

# Dictionary with letters and their respective Morse code symbols
dictionary = {
    '{': '{', '}': '}', ' ': ' ', 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
    'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '-': '-....-', '_': '..--.-', '"': '.-...', '$': '...-..-', '@': '.--.-.', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}

# Function to convert plain text into Morse code
def text_conversor():
    plane_text = text_morse.get().upper()
    text_converted = ""
    for char in plane_text:
        text_converted += dictionary.get(char, "") + "/"
    conversor_show.configure(text=text_converted[:-1]) 


# Function to convert Morse code into plain text
def morse_conversor():
    morse_text = morse_entry.get()
    morse_converted = ""
    inverse = {v: k for k, v in dictionary.items()}
    for code in morse_text.split("/"):
        morse_converted += inverse.get(code, "")
    mconversor_show.configure(text=morse_converted)
   

def copy_result():
    result = conversor_show.cget("text")
    window.clipboard_clear()
    window.clipboard_append(result)
    messagebox.showinfo("Copied", "Result copied to clipboard!")

def copy_result_morse():
    result = mconversor_show.cget("text")
    window.clipboard_clear()
    window.clipboard_append(result)
    messagebox.showinfo("Copied", "Result copied to clipboard!")
#appearance

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#spawn Window
window = customtkinter.CTk()
window.geometry("700x500")
window.title("MorseCodeConversor")
window.iconbitmap(".\Images\icon.ico")

text = customtkinter.CTkLabel(window, text='Welcome to the Morse Code Converter, it is easy to use and practical, I hope you enjoy it.')
text.pack(padx=10,pady=10)

text_morse = customtkinter.CTkEntry(window,placeholder_text="Text to be converted")
text_morse.pack(padx=10,pady=10)

button_frame = customtkinter.CTkFrame(window,fg_color=  "transparent")
button_frame.pack(padx=10,pady=10)

button = customtkinter.CTkButton(button_frame,text="Convert",command=text_conversor)
button.grid(row=0, column=0)

copy_button = customtkinter.CTkButton(button_frame,text="Copy",command=copy_result)
copy_button.grid(row=0, column=1, padx=10)

conversor_show = customtkinter.CTkLabel(window, text='')
conversor_show.pack(padx=10,pady=10)

morse_entry = customtkinter.CTkEntry(window,placeholder_text="Example > /.../---/...")
morse_entry.pack(padx=10,pady=10)

button_frame1 = customtkinter.CTkFrame(window,fg_color= "transparent")
button_frame1.pack(padx=10,pady=10)

button1 = customtkinter.CTkButton(button_frame1,text="Convert",command=morse_conversor)
button1.grid(row=0, column=0)
copy_button1 = customtkinter.CTkButton(button_frame1,text="Copy",command=copy_result_morse)
copy_button1.grid(row=0, column=1, padx=10)

mconversor_show = customtkinter.CTkLabel(window, text='')
mconversor_show.pack(padx=10,pady=10)

window.mainloop()