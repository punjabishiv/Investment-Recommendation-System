from tkinter import *
import os

frame1 = Tk()


def changeOnHover(button, colorOnHover, colorOnLeave):
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover, cursor="hand2"))

    # background color on leaving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))


def frame2():
    os.system('python frame2.py')


######################## Images
image1 = PhotoImage(file='bg1_1058x595.png')
background = Label(frame1, image=image1)
background.place(x=0, y=0)
########################

######################## Window
frame1.title('Investment Recommendation System')
frame1.geometry('1058x595')
windowWidth = 1058
windowHeight = 595
position_x = int(frame1.winfo_screenwidth() / 2 - windowWidth / 2)
position_y = int(frame1.winfo_screenheight() / 2 - windowHeight / 2)
frame1.geometry("+{}+{}".format(position_x, position_y))
icon = Image('photo', file='icon1.png')
frame1.tk.call('wm', 'iconphoto', frame1._w, icon)
########################


######################## Buttons
exit_button = Button(frame1, text='EXIT', width=6, command=frame1.destroy, fg='red', bg='#252525', font=('', 20), bd=-2)
exit_button.place(x=50, y=500)

continue_button = Button(frame1, text='CONTINUE', width=12, height=1, bg='#7CFC00', fg='red', font=('', 20),
                         borderwidth=5, command=frame2)
continue_button.place(x=300, y=500)

changeOnHover(exit_button, "gray", '#252525')
changeOnHover(continue_button, "green", '#7CFC00')
########################

frame1.mainloop()
