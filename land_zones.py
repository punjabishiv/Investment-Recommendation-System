from tkinter import *
import webbrowser

frame1 = Tk()

frame1.title('Information about Land Zones')
frame1.geometry('960x540')
windowWidth = 960
windowHeight = 540
position_x = int(frame1.winfo_screenwidth() / 2 - windowWidth / 2)
position_y = int(frame1.winfo_screenheight() / 2 - windowHeight / 2)
frame1.geometry("+{}+{}".format(position_x, position_y))

def open_page():
    link1 = "https://www.99acres.com/ask-what-is-yellow-zone-green-zone-red-zone-56302.html"
    webbrowser.open(link1)

def changeOnHover(button, colorOnHover, colorOnLeave):
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover, cursor="hand2"))

    # background color on leaving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))


image1 = PhotoImage(file='land_zones.png')
background = Label(frame1, image=image1)
background.place(x=0, y=0)

exit_button = Button(frame1, text='Back', width=6, command=frame1.destroy, fg='yellow', bg='#252525', font=('', 20), bd=-2)
exit_button.place(x=250, y=470)
changeOnHover(exit_button, "gray", '#252525')

know_button = Button(frame1, text='Know More', width=10, command=open_page, fg='yellow', bg='#252525', font=('', 20), bd=-2)
know_button.place(x=500, y=470)
changeOnHover(know_button, "gray", '#252525')

frame1.mainloop()