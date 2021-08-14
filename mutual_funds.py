from tkinter import *
import webbrowser
import os

######################## Window
frame3=Tk()
frame3.title('Mutual Funds Investment')
frame3.config(background='#DCDCDC')
frame3.geometry('1058x595')
windowWidth = 1058
windowHeight = 595
position_x = int(frame3.winfo_screenwidth()/2 - windowWidth/2)
position_y = int(frame3.winfo_screenheight()/2 - windowHeight/2)
frame3.geometry("+{}+{}".format(position_x, position_y))
########################

def changeOnHover(button, colorOnHover = 'gray', colorOnLeave = 'white'):
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover, cursor="hand2"))

    # background color on leaving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))


def f1():
    link1 = "https://drive.google.com/file/d/1sJrPQjdiq-hbDPI0PPaRFJ7jokPJ8WUv/view?usp=sharing"
    webbrowser.open(link1)


def f4():
    link1 = "https://groww.in/mutual-funds"
    webbrowser.open(link1)
    

def basics_of_mutual_funds():
    link1 = "https://drive.google.com/file/d/1xg3SCbHmwyF0xdHA5aI7iEfW5yjMKC8X/view?usp=sharing"
    webbrowser.open(link1)

def why_mutual_funds():
    link1 = "https://drive.google.com/file/d/1ynBIN5dC2WMJ4BN6bKZNrhNkb26xftUK/view?usp=sharing"
    webbrowser.open(link1)


######################## Text Box
text = Text(frame3, height=1, bg='#DCDCDC', fg='red', font=('', 34), bd=-2)
text.insert(5.0, "Mutual Funds Investment")
text.config(state='disabled')
text.place(x=280, y=70)
########################

######################## Buttons
b1 = Button(frame3, text='Some Pupular\nMutual Funds', font=('', 18), fg='red', bg='white', borderwidth=5,
            command=f1)
b1.place(x=300, y=220)


b4 = Button(frame3, text='Start\nInvesting', font=('', 18), fg='red', bg='white', borderwidth=5, command=f4)
b4.place(x=600, y=220)

basics_of_mutual_funds_button = Button(frame3, text = 'Know the Basics of Mutual Funds', command = basics_of_mutual_funds, font=('',18), bd=-2, bg='yellow', borderwidth=5)
basics_of_mutual_funds_button.place(x=350,y=400)
changeOnHover(basics_of_mutual_funds_button, "green", "yellow")

why_to_invest_button = Button(frame3, text = 'Why should I Invest in Mutual Funds?', command = why_mutual_funds, font=('',18), bd=-2, bg='yellow', borderwidth=5)
why_to_invest_button.place(x=330,y=470)
changeOnHover(why_to_invest_button, "green", "yellow")

changeOnHover(b1)
changeOnHover(b4)



back_button = Button(frame3, text = 'BACK', command = frame3.destroy, font=('',12), bd=-2, bg='white', borderwidth=5)
back_button.place(x=30,y=540)
changeOnHover(back_button)

frame3.mainloop()