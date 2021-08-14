from tkinter import *
import webbrowser
import os

######################## Window
frame3=Tk()
frame3.title('Stock Market Investment')
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
    os.system('python stock_market_recommendation.py')


def f2():
    link1 = "https://colab.research.google.com/drive/1QIwJ0-jQXwELscxyggUtm2shMhmG6kvr?usp=sharing"
    webbrowser.open(link1)

def f3():
    os.system('python current_market_module.py')


def f4():
    os.system('python start_investing.py')

def basics_of_stock_market():
    link1 = "https://drive.google.com/file/d/1mJyZwj77t8A1TBeoSaJ3Hg9QWHfNo2cP/view?usp=sharing"
    webbrowser.open(link1)

def afraid_to_invest():
    link1 = "https://drive.google.com/file/d/1V-dZWTxAhAQxo8d28tq2MzRUmZRLr0J3/view?usp=sharing"
    webbrowser.open(link1)


######################## Text Box
text = Text(frame3, height=1, bg='#DCDCDC', fg='red', font=('', 34), bd=-2)
text.insert(5.0, "Stock Market Investment")
text.config(state='disabled')
text.place(x=280, y=70)
########################

######################## Buttons
b1 = Button(frame3, text='Our\nRecommendations', font=('', 18), fg='red', bg='white', borderwidth=5,
            command=f1, width=15)
b1.place(x=50, y=220)
b2 = Button(frame3, width=15, text='Our\nPredictions', font=('', 18), fg='red', bg='white', borderwidth=5, command=f2)
b2.place(x=300, y=220)
b3 = Button(frame3, width=15, text='Check\nCurrent Market', font=('', 18), fg='red', bg='white', borderwidth=5, command=f3)
b3.place(x=550, y=220)
b4 = Button(frame3, width=15, text='Start\nInvesting', font=('', 18), fg='red', bg='white', borderwidth=5, command=f4)
b4.place(x=800, y=220)

basics_of_stock_market_button = Button(frame3, text = 'Know the Basics of Stock Market', command = basics_of_stock_market, font=('',18), bd=-2, bg='yellow', borderwidth=5)
basics_of_stock_market_button.place(x=350,y=400)
changeOnHover(basics_of_stock_market_button, "green", "yellow")

afraid_to_invest_button = Button(frame3, text = 'I am Afraid to Invest? Help Me..!!', command = afraid_to_invest, font=('',18), bd=-2, bg='yellow', borderwidth=5)
afraid_to_invest_button.place(x=350,y=470)
changeOnHover(afraid_to_invest_button, "green", "yellow")

changeOnHover(b1)
changeOnHover(b2)
changeOnHover(b3)
changeOnHover(b4)



back_button = Button(frame3, text = 'BACK', command = frame3.destroy, font=('',12), bd=-2, bg='white', borderwidth=5)
back_button.place(x=30,y=540)
changeOnHover(back_button)

frame3.mainloop()