import cli_box
import pyfiglet
from colorama import Fore

def banner():
    ascii_art = pyfiglet.Figlet()
    info =  f"\n\n{Fore.MAGENTA}"\
    f"{Fore.RESET}{'-'*20}"
    
    author = "Author: Caostic\nDate: 04/05/2023\nVersion: v1.0"
    print(Fore.MAGENTA + ascii_art.renderText("Morse Code Conversor") + Fore.RESET + author + info)
    print(cli_box.box(f"{'Choose':^}\n{'[1] - For text to morse ':^} \n{'[2] - For morse to text':^} ",corners=('+','+','+','+'), sides=('|','-')))

# function to convert plain text into morse code
def text_conversor(plane_text):
    for char in plane_text:
        text_converted = dictionary.get(char)
        print(text_converted, end='/')

# function to convert plain text into morse code
def morse_conversor(morse_text):
    inverse = {v: k for k, v in dictionary.items()}
    for char in morse_text:
        morse_converted= inverse.get(char)
        print(morse_converted, end='')

<<<<<<< HEAD
# main code
def main():
    try:
        banner()
        option=int(input("\nChoose the option: "))
        if option not in [1,2]:
            raise ValueError("Invalid option. Choose 1 or 2.") 
        if option == 1:
            plane_text = input("\nPut your text to turn into morse: ").upper()
            text_conversor(plane_text)
            


        if option == 2:
            morse_text = input("Put your morse to turn into text: ").split()
            morse_conversor(morse_text)

    except ValueError as error:
        print(f"Error: {error}")

#dictionary with letters and their respective morsecode symbols
=======

>>>>>>> main
dictionary = {'{':'{','}': '}',' ': ' ', 'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....',
'I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.',
'S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..','.':'.-.-.-',',':'--..--',
'?':'..--..',"'":'.----.','!':'-.-.--','/':'-..-.','(': '-.--.',')':'-.--.-','&':'.-...',':':'---...',';':'-.-.-.',
'=':'-...-','-':'-....-','_': '..--.-','"':'.-...','$':'...-..-','@':'.--.-.',
'1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.', '0':'-----'}


if __name__ == ('__main__'):
    main()