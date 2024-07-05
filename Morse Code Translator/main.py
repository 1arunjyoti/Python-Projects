import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Style
from ttkbootstrap import Style, ttk

#this program is not complete

morse_code_dict= {'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 
                  'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
                  'I':'..', 'J':'.---', 'K':'-.-','L':'.-..', 
                  'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 
                  'Q':'--.-','R':'.-.', 'S':'...', 'T':'-', 
                  'U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 
                  'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', 
                  '3':'...--', '4':'....-', '5':'.....', '6':'-....',
                  '7':'--...', '8':'---..', '9':'----.', '0':'-----', 
                  ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', 
                  '-':'-....-', '(':'-.--.', ')':'-.--.-'
}

reverse_morse_code_dict = {v: k for k, v in morse_code_dict.items()}

def show_text_to_morse():
    home_frame.pack_forget()
    translation_frame.pack()
    translation_label.config(text="Input Morse Code:")
    translation_label.config(text="Translate to Morse Code:")
    translation_button.config(command=text_to_morse_code)

def show_morse_to_text():
    home_frame.pack_forget()
    translation_frame.pack()
    translation_label.config(text="Input Morse Code:")
    translation_label.config(text="Translate to Morse Code:")
    translation_button.config(command=morse_code_to_text)


def show_home_screen():
    translation_frame.pack_forget()
    home_frame.pack()
    input_text.delete("1.0", "end")
    output_text.delete("1.0", "end")

def text_to_morse_code():
    text= input_text.get("1.0", "end").strip().upper()
    if not text:
        messagebox.showwarning("Error", "Please enter text to translate")
        return
    """ for char in text:
        if char in morse_code_dict.values():
            messagebox.showwarning("Error", "Please input Morse code")
            return """
    morse_code= ""
    for char in text:
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + " "
        else:
            messagebox.showwarning("Error", "Please input valid text")
            return
            """ morse_code +=char """
    output_text.delete("1.0", "char")
    output_text.insert("1.0", morse_code)

def morse_code_to_text():
    morse_code= input_text.get("1.0", "end").strip().split(" ")
    if not morse_code:
        messagebox.showwarning("Error", "Please enter Morse Code")
        return
    
    """ for code in morse_code:
        if code.isalpha():
            messagebox.showwarning("Error", "cannor input letters in this option")
            return """

    text= ""
    for code in morse_code:
        if code in morse_code_dict:
            text += morse_code_dict[code]
        else:
            messagebox.showwarning("Error", "Please input valid Morse code")
            return
            """ text += code """
    output_text.delete("1.0", "end")
    output_text.insert("1.0", text)

def clear_text():
    input_text.delete("1.0", "end")
    output_text.delete("1.0", "end")
    show_home_screen()

window= tk.Tk()
window.title = ("Morse Code Translator")
window.geometry("500x500")
style = Style(theme="darkly")


home_frame= ttk.Frame(window, padding="20")
home_frame.pack()

home_label = ttk.Label(home_frame, text="Select Translation Type:")
home_label.pack(pady=10)


text_to_morse_code_btn= ttk.Button(home_frame, text="Text to Morse Code", command=show_text_to_morse)
text_to_morse_code_btn.pack(pady=5)

morse_to_text_code_btn= ttk.Button(home_frame, text="Morse to Text Code", command=show_morse_to_text)
morse_to_text_code_btn.pack(pady=5)

translation_frame= ttk.Frame(window, padding="20")

translation_label= ttk.Label(translation_frame, text="Input text:", font=('tk.DefaultFont', 30))
translation_label.pack(pady=10)

input_text= tk.Text(translation_frame, height=5)
input_text.pack()

output_text_label= ttk.Label(translation_frame, text="Output Text", font=('tk.DefaultFont', 30))
output_text_label.pack()

output_text= tk.Text(translation_frame, height=5)
output_text.pack()

translation_button= ttk.Button(translation_frame, text="Translate", command=None)
translation_button.pack(pady=10)

back_button= ttk.Button(translation_frame, text="Back", command=show_home_screen)
back_button.pack(pady=10)

translation_frame.pack_forget()

window.mainloop()