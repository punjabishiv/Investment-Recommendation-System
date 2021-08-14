from tkinter import *
import webbrowser

frame3=Tk()
frame3.title('Current Market Module')
frame3.config(background='#DCDCDC')
frame3.geometry('1058x595')
windowWidth = 1058
windowHeight = 595
position_x = int(frame3.winfo_screenwidth()/2 - windowWidth/2)
position_y = int(frame3.winfo_screenheight()/2 - windowHeight/2)
frame3.geometry("+{}+{}".format(position_x, position_y))

def search():
    symbol = entry1.get()
    link1 = "https://finance.yahoo.com/quote/"+symbol+"?p="+symbol
    webbrowser.open(link1)
    
def overall_market():
    link1 = "https://trade.angelbroking.com/"
    webbrowser.open(link1)

def changeOnHover(button, colorOnHover = 'gray', colorOnLeave = 'white'):
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover, cursor="hand2"))

    # background color on leaving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

# GUI
text1=Text(frame3, height=1, width=25, bg='#DCDCDC',fg='red', font=('',26), bd=-2)
text1.insert(5.0, "Current Market Module")
text1.config(state='disabled')
text1.place(x=330, y=10)

label1 = Label(frame3, text='Enter Stock Symbol', font=('',15), bg='#DCDCDC')
label1.place(x=300,y=150)
entry1=Entry(frame3)
entry1.place(x=500,y=150,height=30,width=180)

go_button = Button(frame3, text = 'Search', command = search, font=('',12), bd=-2, bg='yellow', borderwidth=5)
go_button.place(x=700,y=150)
changeOnHover(go_button, "green", "yellow")


text1=Text(frame3, height=2, bg='#DCDCDC',fg='red', font=('',18), bd=-2)
text1.insert(5.0, "Don't wish to search for\na Particular Stock Symbol?")
text1.config(state='disabled')
text1.place(x=380, y=300)

overall_market_button = Button(frame3, text = 'See the\nOverall Market', command = overall_market, font=('',12), bd=-2, bg='yellow', borderwidth=5)
overall_market_button.place(x=450,y=370)
changeOnHover(overall_market_button, "green", "yellow")


back_button = Button(frame3, text = 'BACK', command = frame3.destroy, font=('',12), bd=-2, bg='white', borderwidth=5)
back_button.place(x=30,y=540)
changeOnHover(back_button)



frame3.mainloop()