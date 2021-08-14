from tkinter import *
import webbrowser

frame3=Tk()
frame3.title('Start Investing!')
frame3.config(background='#DCDCDC')
frame3.geometry('480x270')
windowWidth = 160*3
windowHeight = 90*3
position_x = int(frame3.winfo_screenwidth()/2 - windowWidth/2)
position_y = int(frame3.winfo_screenheight()/2 - windowHeight/2)
frame3.geometry("+{}+{}".format(position_x, position_y))


def f1():
    link1 = "https://youtu.be/VuJURlJ-S24"
    webbrowser.open(link1)

def f2():
    link1 = "https://itrade.angelbroking.com/"
    webbrowser.open(link1)


def changeOnHover(button, colorOnHover = 'gray', colorOnLeave = 'white'):
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover, cursor="hand2"))

    # background color on leaving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

b1 = Button(frame3, text='Watch Video\nTutorial', font=('', 15), fg='red', bg='white', borderwidth=5,
            command=f1)
b1.place(x=50, y=50)
b2 = Button(frame3, text='Open a\nTrading Account', font=('', 15), fg='red', bg='white', borderwidth=5, command=f2)
b2.place(x=250, y=50)

changeOnHover(b1)
changeOnHover(b2)

back_button = Button(frame3, text = 'BACK', command = frame3.destroy, font=('',12), bd=-2, bg='white', borderwidth=5)
back_button.place(x=30,y=200)
changeOnHover(back_button)

frame3.mainloop()