from tkinter import *
import os
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import webbrowser

######################## Window
frame3=Tk()
frame3.title('Real Estate Investment')
frame3.config(background='#DCDCDC')
frame3.geometry('1058x595')
windowWidth = 1058
windowHeight = 595
position_x = int(frame3.winfo_screenwidth()/2 - windowWidth/2)
position_y = int(frame3.winfo_screenheight()/2 - windowHeight/2)
frame3.geometry("+{}+{}".format(position_x, position_y))
########################
######################## Function Definitions


land_years = []
land_prices = []

def reasons_to_invest():
    link1 = "https://drive.google.com/file/d/188ua43YM3ltr8co5TCGAnFdAYE4Usxk6/view?usp=sharing"
    webbrowser.open(link1)

def land_graph():
    global land_years
    global land_prices
    x = land_years
    x = [str(i) for i in x]
    y = land_prices
    y = [round(i, 2) for i in y] 
    plt.xlabel("Years")
    plt.ylabel("Price (in Lacs)")
    plt.title("Estimated Land Prices based on Input Prices")
    plt.bar(x, y)
    plt.xticks(rotation = 45)

    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha="center", va="bottom")
    
    plt.show()

def changeOnHover(button, colorOnHover = 'gray', colorOnLeave = 'white'):
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover, cursor="hand2"))

    # background color on leaving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

def reset_frame2():
    entry_current_price.delete(0, END)
    user_year.delete(0, END)

def suggest2():
    current_price = entry_current_price.get()
    year = user_year.get()
    zone = zone_type.get()
    str1 = ""
    
    if current_price=="" or year=="":
        str1 += "Dear User,\nPlease enter valid value(s)!\nPress RESET to reset fields..."

    elif not 2021<int(year)<=2050:
        str1 += "Please enter the year between\n 2022 and 2050.\nPress RESET to reset fields..."

    else:
        difference = int(year) - 2021
        estimated_price_1 = float(current_price) * (1.08 ** difference)
        estimated_price_1 = round(estimated_price_1,2)
        estimated_price_2 = float(current_price) * (1.10 ** difference)
        estimated_price_2 = round(estimated_price_2,2)
        str1 += ">> The estimated price for this Land is:\nbetween "+str(estimated_price_1)+" Lacs and "+str(estimated_price_2)+" Lacs"

        if zone == "Red Zone":
            str1 += "\n\n>> As the zone is Red,\nPlease DO NOT have any plans for yourself.\nThis area is reserved for public use."
        elif zone == "Green Zone":
            str1 += "\n\n>> As the zone is Green,\nYou may need to put extra efforts to convert\nthe land for constructing plot.\nThough, you may use it for agriculture, nursery, etc."
        elif zone == "Dark Yellow":
            str1 += "\n\n>> As the zone is Dark Yellow,\nYou may use this to construct residential buildings.\nIn the future, this might be useful for commercial\nactivities such as groceries, pharmacies, \neateries, etc."
        elif zone == "Light Yellow":
            str1 += "\n\n>> As the zone is Light Yellow,\nThis land can only be used for residential\nconstruction.\nThis might not be useful if you wish to use it for\ncommercial activities."
    
    text1=Text(frame3, height=10, width=40, bg='#DCDCDC',fg='green', font=('',16), bd=-2)
    text1.insert(5.0, str1)
    text1.config(state='disabled')
    text1.place(x=550, y=380)


def whats_this():
    os.system("python land_zones.py")

def reset_frame():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)

def suggest():
    y1 = (entry1.get())
    y2 = (entry2.get())
    y3 = (entry3.get())
    y4 = (entry4.get())
    y5 = (entry5.get())
    str1 = ""
    flag = 0

    if not y1 or not y2 or not y3 or not y4 or not y5:
        str1 += "Please enter valid values.\n(For all the fields!)"

    else:
        y1 = float(y1)
        y2 = float(y2)
        y3 = float(y3)
        y4 = float(y4)
        y5 = float(y5)
        if y5 - y1 > 0:             # profit
            str1 += ">> This land can give you profits in the longer run.\n>> This is good for Long Term Investment\n      with Low Risk.\n>> We have plotted the estimated values\n      according to your input values."

            prices = [y1,y2,y3,y4,y5]
            years = [2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030]

            prices1 = prices
            years1 = years[:5]

            x = np.array(years1).reshape((-1, 1))
            y = np.array(prices1)

            model = LinearRegression()
            model.fit(x, y)
            model = LinearRegression().fit(x, y)

            # r_sq = model.score(x, y)
            # print('coefficient of determination:', r_sq)
            # print('intercept:', model.intercept_)
            # print('slope:', model.coef_)

            new_model = LinearRegression().fit(x, y.reshape((-1, 1)))
            next_years = years[5:]
            test_data = np.array(next_years).reshape((-1, 1))
            y_pred = model.predict(test_data)
            # print('predicted response:', y_pred, sep='\n')
            # print(list(y_pred))

            x_to_plot = years
            y_to_plot = prices
            y_to_plot.extend(list(y_pred))

            # print("Graph data")
            # print(x_to_plot)
            # print(y_to_plot)

            global land_years
            global land_prices
            land_years = x_to_plot
            land_prices = y_to_plot

            flag = 1

        else:
            str1 += ">> You may not consider investing your money\n      in this land.\n>> Please do some research on other lands.\n>> We are suggesting this based on your\n      input Land Prices."

    text1=Text(frame3, height=10, width=40, bg='#DCDCDC',fg='green', font=('',16), bd=-2)
    text1.insert(5.0, str1)
    text1.config(state='disabled')
    text1.place(x=550, y=380)

    if flag == 1:
        see_graph = Button(frame3, text = 'Visualize Estimated Prices', font=('',18), fg='red', bg='white', borderwidth=5, command=land_graph)
        see_graph.place(x=600,y=530)
        changeOnHover(see_graph)


text1=Text(frame3, height=1, width=22, bg='#DCDCDC',fg='red', font=('',26), bd=-2)
text1.insert(5.0, "Real Estate Investment")
text1.config(state='disabled')
text1.place(x=330, y=10)

label1 = Label(frame3, text='Price in 2016 (in Lacs)', font=('',15), bg='#DCDCDC')
label1.place(x=30,y=100)
entry1=Entry(frame3)
entry1.place(x=270,y=100,height=30)

label1 = Label(frame3, text='Price in 2017 (in Lacs)', font=('',15), bg='#DCDCDC')
label1.place(x=30,y=150)
entry2=Entry(frame3)
entry2.place(x=270,y=150,height=30)

label1 = Label(frame3, text='Price in 2018 (in Lacs)', font=('',15), bg='#DCDCDC')
label1.place(x=30,y=200)
entry3=Entry(frame3)
entry3.place(x=270,y=200,height=30)

label1 = Label(frame3, text='Price in 2019 (in Lacs)', font=('',15), bg='#DCDCDC')
label1.place(x=30,y=250)
entry4=Entry(frame3)
entry4.place(x=270,y=250,height=30)

label1 = Label(frame3, text='Price in 2020 (in Lacs)', font=('',15), bg='#DCDCDC')
label1.place(x=30,y=300)
entry5=Entry(frame3)
entry5.place(x=270,y=300,height=30)






submit_button=Button(frame3, text = 'SUBMIT', font=('',18), fg='red', bg='white', borderwidth=5, command=suggest)
submit_button.place(x=80,y=400)
changeOnHover(submit_button)
reset_button=Button(frame3, text = 'RESET', font=('',18), bg='white', borderwidth=5, command=reset_frame)
reset_button.place(x=250,y=400)
changeOnHover(reset_button)
reasons_to_invest_button = Button(frame3, text = 'Why Should I Invest?', font=('',15), fg='red', bg='#7CFC00', borderwidth=5, command=reasons_to_invest)
reasons_to_invest_button.place(x=110,y=470)
changeOnHover(reasons_to_invest_button, 'gray', '#7CFC00')
back_button = Button(frame3, text = 'BACK', command = frame3.destroy, font=('',12), bd=-2, bg='white', borderwidth=5)
back_button.place(x=30,y=540)
changeOnHover(back_button)

text1=Text(frame3, height=1, width=30, bg='#DCDCDC',fg='red', font=('',26), bd=-2)
text1.insert(5.0, "OR")
text1.config(state='disabled')
text1.place(x=440, y=160)




# Column 2
label1 = Label(frame3, text='Current Price (in Lacs)', font=('',15), bg='#DCDCDC')
label1.place(x=550,y=100)
entry_current_price=Entry(frame3)
entry_current_price.place(x=800,y=100,height=30)


zone_type=StringVar()
zone_type.set('Red Zone')
label1 = Label(frame3, text='Type of Zone', font=('',15), bg='#DCDCDC')
label1.place(x=550,y=150)
entry_zone = OptionMenu(frame3,zone_type,'Red Zone','Green Zone','Dark Yellow','Light Yellow')
entry_zone.place(x=800,y=150,height=30,width=100)
whatsthis=Button(frame3, text = "What's This?", font=('',10), fg='red', bg='#7CFC00', borderwidth=5, command=whats_this)
whatsthis.place(x=920,y=145)
changeOnHover(whatsthis, 'gray', '#7CFC00')

label1 = Label(frame3, text='Year (for which you\nwant to predict price)', font=('',15), bg='#DCDCDC')
label1.place(x=530,y=200)
user_year=Entry(frame3)
user_year.place(x=800,y=200,height=30)

estimate_button=Button(frame3, text = 'ESTIMATE PRICE', font=('',18), fg='red', bg='white', borderwidth=5, command=suggest2)
estimate_button.place(x=560,y=260)
changeOnHover(estimate_button)
reset_button=Button(frame3, text = 'RESET', font=('',18), bg='white', borderwidth=5, command=reset_frame2)
reset_button.place(x=820,y=260)
changeOnHover(reset_button)

frame3.mainloop()