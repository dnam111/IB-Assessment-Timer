from tkinter import *
#library (import * = import all of the functions of the tkinter)
root = Tk()
#create the "root" window
root.geometry("500x500")
# manage screen size
root.title("Timer")
# edit title

label = Label(root, text="welcome", font='Arial, 12')
#Adding Text/Labeling
label.pack(padx=100, pady=100)
#Presentation Placement (can also be used with .place rather than .pack)

#textbox
textbox = Text(root, height=3)
#Placement
textbox.pack(padx=10, pady=10)


#another type of box (similar to password box)
entrybox = Entry(root)
entrybox.pack()
#Button
button = Button(root)
button.pack()


root.mainloop()

