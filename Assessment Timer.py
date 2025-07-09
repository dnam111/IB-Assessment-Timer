from tkinter import *
from tkinter import messagebox
import time

root = Tk()
root.geometry("700x700")
root.title("Assessment Timer")
root.configure(bg="white")

frame1 = LabelFrame(root, highlightbackground="black", highlightthickness=5, bg="white")
frame1.pack(padx=20, pady=20)

hourString = StringVar()
hour_box = Entry(root, textvariable=hourString, width=10)
hour_box.place(x=80, y=300)
labelhour = Label(font='Arial, 12 bold', text="Hour:", fg="black", bg="white")
labelhour.place(x=80, y=275)
minutesString = StringVar()
minute_box = Entry(root, textvariable=minutesString, width=10)
minute_box.place(x=300, y=300)
labelminutes = Label(font='Arial, 12 bold',text="Minutes:", fg="black", bg="white")
labelminutes.place(x=300, y=275)
secondsString = StringVar()
second_box = Entry(root, textvariable=secondsString, width=10)
second_box.place(x=520, y=300)
labelseconds = Label(font='Arial, 12 bold',text="Seconds:", fg="black", bg="white")
labelseconds.place(x=520, y=275)

hourstartString = StringVar()
hourstart_box = Entry(root, textvariable=hourstartString, width=10)
labelhourstart = Label(font='Arial, 12 bold', text="Test Starts at: ", fg="black", bg="white")
hourstart_box.place(x=200, y=400)
labelhourstart.place(x=200, y=370)
minutesstartString = StringVar()
minutesstart_box = Entry(root, textvariable=minutesstartString, width=10)
minutesstart_box.place(x=400, y=400)
colon = Label(font = 'Arial, 24 bold', text=":", fg="black", bg="white")
colon.place(x=350, y=400)


hoursendString = StringVar()
hoursend_box = Entry(root, textvariable=hoursendString, width=10)
labelhoursend = Label(font = 'Arial, 12 bold', text="Test Ends at:", fg="black", bg="white")
hoursend_box.place(x=200, y=550)
labelhoursend.place(x=200, y=520)
minutesendString = StringVar()
minutesend_box = Entry(root, textvariable=minutesendString, width=10)
minutesend_box.place(x=400, y=550)
colon2 = Label(font = 'Arial, 24 bold', text=":", fg="black", bg="white")
colon2.place(x=350, y=550)

remainingtext = StringVar()
remainingbox = Entry(root, textvariable=remainingtext, width=20)
remainingbox.place(x=470, y=200)
remaining = Label(font="Arial, 12 bold", text="Warning:", fg="black", bg="white")
remaining.place(x=470, y=170)

warningmessage = StringVar()
warningbox = Entry(root,textvariable=warningmessage, width=5)
warningbox.place(x=50, y=100)
warningmessage2 = StringVar()
warningbox2 = Entry(root, textvariable=warningmessage2, width=5)
warningbox2.place(x=150, y=100)
warning = Label(font="Arial, 10", text="The 5 Minutes Warning Message would be given at:", fg="black", bg="white")
warning.place(x=5, y=70)
colon3 = Label(font="Arial, 24 bold", text=":",fg="black", bg="white")
colon3.place(x=125, y=100)

warningmessagefor10mins = StringVar()
warning10box = Entry(root, textvariable=warningmessagefor10mins, width=5)
warning10box.place(x=50, y=200)
warningmessagefor10mins2 = StringVar()
warning10box2 = Entry(root, textvariable=warningmessagefor10mins2, width=5)
warning10box2.place(x=150, y=200)
warning2 = Label(font="Arial, 10", text="The 10 Minutes Warning Message would be given at:", fg="black", bg="white")
warning2.place(x=5, y=170)
colon4= Label(font="Arial, 24 bold", text = ":",fg="black", bg="white")
colon4.place(x=125, y=200)


def worldclock():
    current = time.localtime()
    current_time = time.strftime("%H:%M:%S", current)
    label.after(1000, worldclock)
    label.config(text=current_time, fg="black", bg="white")


def timer():
    if len(hourString.get()) == 0:
        hourString.set("0")
    if len(minutesString.get()) == 0:
        minutesString.set("0")
    if len(secondsString.get()) == 0:
        secondsString.set("0")
        #Error
    if (len(secondsString.get()) == 0) and (len(minutesString.get()) == 0) and (len(hourString.get()) == 0):
        messagebox.showinfo("Please Enter the Correct Values")
    if len(minutesstartString.get()) == 0:
        minutesstartString.set("00")
    t = (3600 * int(hourString.get())) + (60 * int(minutesString.get())) + int(secondsString.get())
    s = (3600 * int(hourstartString.get())) + (60 * int(minutesstartString.get()))
    st = (3600 * int(hourString.get())) + (60 * int(minutesString.get())) + int(secondsString.get())
    shours, ssecs = divmod(st + s, 3600)
    smins, ssecs = divmod((st + s) % 3600, 60)
    hoursendString.set("{0:2d}".format(shours))
    minutesendString.set("{0:2d}".format(smins))

    whours, wsecs = divmod(st + s - 300, 3600)
    wmins, wsecs = divmod((st + s - 300) % 3600, 60)
    warningmessage.set("{0:2d}".format(whours))
    warningmessage2.set("{0:2d}".format(wmins))
    if wmins == 0:
        warningmessage2.set("00")
    thours, tsecs = divmod(st + s - 600, 3600)
    tmins, tsecs = divmod((st + s - 600) % 3600, 60)
    warningmessagefor10mins.set("{0:2d}".format(thours))
    warningmessagefor10mins2.set("{0:2d}".format(tmins))
    if t<600:
        warningmessagefor10mins.set("none")
        warningmessagefor10mins2.set("none")
    while t > -1:
        hours, secs = divmod(t, 3600)
        mins, secs = divmod(t%3600, 60)
        hourString.set("{0:2d}".format(hours))
        minutesString.set("{0:2d}".format(mins))
        secondsString.set("{0:2d}".format(secs))
        root.update()
        time.sleep(1)

        if t == 300:
            remainingtext.set("5 minutes remaining")
        if t == 290:
            remainingtext.set("")
        if t == 600:
            remainingtext.set("10 minutes remaining")
        if t == 590:
            remainingtext.set("")

        if t == 0:
            root.update()
            messagebox.showinfo("","Time Elapsed")
        t -= 1


Intro = Label(frame1, text="The Current Time is:", font='Arial, 12 bold', fg="black", bg="white")
Intro.pack(padx=10, pady=10)
label = Label(frame1, font='Arial, 12 bold', fg="white")
label.pack(padx=10, pady=10)
worldclock()
button1 = Button(root, text="Start Timer",font="Arial, 12 bold", width = 15, height=5, fg="black",command=timer)
button1.pack(padx=10,pady=20)
button1.pack()

root.mainloop()
