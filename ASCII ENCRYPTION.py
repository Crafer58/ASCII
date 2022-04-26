from tkinter import *
root = Tk()
root.geometry("300x400")
root.configure(background = 'cyan')

user_text = Entry(root)
user_text.place(relx = 0.5, rely = 0.4 , anchor = CENTER)

label = Label(root, text = "Name in ASCII: ", bg = 'red', fg = 'black')
label.place(relx = 0.5, rely = 0.6, anchor = CENTER)

label2 = Label(root, text = "Encrypted Name: ", bg = 'yellow', fg = 'black')
label2.place(relx = 0.5, rely = 0.7, anchor = CENTER)

def convert():
    
    user_input = user_text.get()
    for letter in user_input:
        label["text"] += str(ord(letter)) + " "
        
        ascii = int(ord(letter))
        encrypted_value = ascii - 1
        label2["text"] += str(chr(encrypted_value))
        

btn = Button(root, text = "Show ASCII Code and Encrypted Value", bg = 'gold', command = convert)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()
