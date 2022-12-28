# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 21:35:30 2022

@author: Ankan Datta
"""

from tkinter import * 
root = Tk()

root.title("Ascii")
root.geometry("400x400")

root.configure(background='light blue')

enter_word = Entry(root)
enter_word.place(relx = 0.5, rely = 0.4, anchor = CENTER)

label_1 = Label(root, text="Name In ASCII : ", bg = "light yellow", fg = "black")
label_2 = Label(root, text="Encrypted name : ", bg = "pink", fg = "black")

def asciiConverter():
    
    input_word = enter_word.get
    
    for letter in input_word():
        label_1["text"] += str(ord(letter)) + " "
        ascii = int(ord(letter))
        encrypted = ascii - 1
        label_2["text"] += str(chr(encrypted))
        
btn = Button(root, text = "Show ASCII value & Encrypted-Name ", command=asciiConverter, bg="gold", fg="black")
btn.place(relx = 0.5, rely = 0.5, anchor=CENTER)

label_1.place(relx = 0.5, rely = 0.6, anchor=CENTER)
label_2.place(relx = 0.5, rely = 0.7, anchor=CENTER)

root.mainloop()