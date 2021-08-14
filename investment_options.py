from tkinter import *
import os

######################## Basic Structure
frame2 = Tk()
frame2.geometry('1058x595')
windowWidth = 1058
windowHeight = 595
position_x = int(frame2.winfo_screenwidth() / 2 - windowWidth / 2)
position_y = int(frame2.winfo_screenheight() / 2 - windowHeight / 2)
frame2.geometry("+{}+{}".format(position_x, position_y))
frame2.title('Investment Options')


########################

######################## Functions
def changeOnHover(button, colorOnHover="gray", colorOnLeave='#252525'):
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover, cursor="hand2"))

    # background color on leaving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))


def f1():
    os.system('python stock_market.py')


def f2():
    os.system('python mutual_funds.py')


def f3():
    os.system('python gold_investment.py')


def f4():
    os.system('python real_estate.py')


########################

######################## Images
image1 = PhotoImage(file='bg2.gif')
background = Label(frame2, image=image1)
background.place(x=0, y=0)
########################

######################## Text Box
text = Text(frame2, height=1, width=16, bg='#252525', fg='red', font=('', 34), bd=-2)
text.insert(5.0, "Investment Options")
text.config(state='disabled')
text.place(x=340, y=70)
########################

######################## Buttons
back_button = Button(frame2, text='BACK', command=frame2.destroy, font=('', 25), bd=-2, fg='red', bg='#252525',
                     borderwidth=5)
back_button.place(x=470, y=450)
########################
b1 = Button(frame2, text='Stock\nMarket', font=('', 27), width=10, fg='red', bg='#252525', borderwidth=5,
            command=f1)
b1.place(x=50, y=250)
b2 = Button(frame2, text='Mutual\nFunds', font=('', 27), width=10, fg='red', bg='#252525', borderwidth=5, command=f2)
b2.place(x=300, y=250)
b3 = Button(frame2, text='Gold\nInvestment', font=('', 27), width=10, fg='red', bg='#252525', borderwidth=5, command=f3)
b3.place(x=550, y=250)
b4 = Button(frame2, text='Real\nEstate', font=('', 27), width=10, fg='red', bg='#252525', borderwidth=5, command=f4)
b4.place(x=800, y=250)

changeOnHover(b1)
changeOnHover(b2)
changeOnHover(b3)
changeOnHover(b4)
changeOnHover(back_button)

frame2.mainloop()
