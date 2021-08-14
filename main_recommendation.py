from tkinter import *
import os
import webbrowser
from tkinter import scrolledtext


######################## Window
frame3=Tk()
frame3.title('Investment Recommendation Window')
frame3.config(background='#DCDCDC')
frame3.geometry('1058x595')
windowWidth = 1058
windowHeight = 595
position_x = int(frame3.winfo_screenwidth()/2 - windowWidth/2)
position_y = int(frame3.winfo_screenheight()/2 - windowHeight/2)
frame3.geometry("+{}+{}".format(position_x, position_y))
########################

def future_value(invested_monthly, yrs, annual_roi = 12):
    compounded_roi = annual_roi/100/12
    fv = float(invested_monthly) * ((1+compounded_roi)**(yrs*12)-1) * (1+compounded_roi)/compounded_roi 
    fv = round(fv, 0)
    return fv

def total_invested(invested_monthly, yrs):
    total_money = invested_monthly * 12 * yrs
    total_money = round(total_money, 0)
    return total_money

def check_investment_options():
    os.system("python investment_options.py")

def get_help_online():
    link1 = "https://economictimes.indiatimes.com/wealth/invest"
    webbrowser.open(link1)

def changeOnHover(button, colorOnHover = 'gray', colorOnLeave = 'white'):
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover, cursor="hand2"))

    # background color on leaving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def reset_frame():
    entry1.delete(0, END)
    entry2.delete(0, END)
    

def suggest():
    amount = (entry1.get())
    age = (entry2.get())
    occupation = (occupation_selection.get())
    str1 = ''
    
    if not amount or not age:
        str1 += "Dear User,\nPlease fill all the fields.\n\nYou may press RESET to reset fields."

    elif not isfloat(amount) or not isfloat(age):
        str1 += "Dear User,\nPlease enter appropriate values for amount and age.\n\n\t>> Income    =>    Integer or Float\n\t>> Age         =>    Preferably an Integer"

    elif float(amount) < 0 or int(age) <= 0:
        str1 += "Dear User,\nPlease enter a positive value for amount and age.\n\nYou may press RESET to reset fields."

    else:
        age = int(age)
        amount = float(amount)
        per50 = float(amount)*0.5
        per40 = float(amount)*0.4
        per30 = float(amount)*0.3
        per20 = float(amount)*0.2
        
        per50 = str(round(per50, 0))
        per40 = str(round(per40, 0))
        per30 = str(round(per30, 0))
        per20 = str(round(per20, 0))

        pie_labels = ["Total Invested", "Total Returns"]
        

        if age<1 or age>130:
            str1 += "Dear User,\nPlease enter an appropriate age.\nAge should be between 1 year and 130 years.\n\nYou may press RESET to reset fields."

        else:
            if age < 18:
                str1 += "Dear user,\nAs your age is below 18 years,\nIt won't be possible for you to invest in Stocks or Mutual Funds.\nBut you may study about stock market to get a basic idea about the same.\n\nYou may read the following books to increase your knowledge.\n\n1. The Intelligent Investor\n2. Rich Dad Poor Dad"

                

            else:
                if 18<=age<=35:
                    
                    str1 += "Dear user,\nAs you are young, we recommend you the following investment strategies.\n\n>> 50% - For your needs (food, rent, EMI, etc.)\n\t[50 %    =>    ~ " + per50 + "    INR]\n\n>> 30% - For your wants (vacations, gadgets, etc.)\n\t[30 %    =>    ~ " + per30 + "    INR]\n\n>> 20% - Savings and Investments (Stocks, Mutual Funds, FD, etc.)\n\t[20 %    =>    ~ " + per20 + "    INR]\n"

                    str1 += "\n\n>> If you follow this Financial Discipline, \nEstimated Returns (at 12% Compound Interest) :"

                    invested = float(amount) * 0.2
                    invested = round(invested, 0)
                    str1 += "\nInvested/month      =>      " + str(invested) + " INR"
                    
                    str1 += "\n\nPeriod\tInvested (INR)\t\tFuture Value (INR)\n---------------------------------------------------------------"

                    str1 += "\n2 yrs\t~ " + str(total_invested(invested, 2)) + "\t\t~ " + str(future_value(invested, 2))                    
                    str1 += "\n5 yrs\t~ " + str(total_invested(invested, 5)) + "\t\t~ " + str(future_value(invested, 5))
                    str1 += "\n10 yrs\t~ " + str(total_invested(invested, 10)) + "\t\t~ " + str(future_value(invested, 10))

                    

                    

                elif age>35:
                    str1 += "Dear user,\nAs you are elder, we recommend you the following investment strategies.\n\n>> 40% - For your needs (food, rent, EMI, etc.)\n\t[40 %    =>    ~ " + per40 + "    INR]\n\n>> 20% - For your wants (vacations, gadgets, etc.)\n\t[20 %    =>    ~ " + per20 + "    INR]\n\n>> 40% - Savings and Investments (Stocks, Mutual Funds, FD, etc.)\n\t[40 %    =>    ~ " + per40 + "    INR]\n"

                    str1 += "\n\n>> If you follow this Financial Discipline, \nEstimated Returns (at 12% Compound Interest) :"

                    invested = float(amount) * 0.4
                    invested = round(invested, 0)
                    str1 += "\nInvested/month      =>      " + str(invested) + " INR"
                    
                    str1 += "\n\nPeriod\tInvested (INR)\t\tFuture Value (INR)\n---------------------------------------------------------------"

                    str1 += "\n2 yrs\t~ " + str(total_invested(invested, 2)) + "\t\t~ " + str(future_value(invested, 2))                    
                    str1 += "\n5 yrs\t~ " + str(total_invested(invested, 5)) + "\t\t~ " + str(future_value(invested, 5))
                    str1 += "\n10 yrs\t~ " + str(total_invested(invested, 10)) + "\t\t~ " + str(future_value(invested, 10))


            if occupation=="Student":
                str1 += "\n\n\n>> Self Investment is the Best Investment.\nAs you are a student, you may invest your time and energy in learning via various resources such as Online Courses.\nWe recommend checking out courses on the following sites:\n1. www.coursera.org\n2. www.udemy.com"

            elif occupation=="Employee":
                str1 += "\n\n\n>> Self Investment is the Best Investment.\nAs you are an employee, you may invest your time and energy in learning via various resources, reading books.\nWe recommend checking out courses on the following sites:\n1. www.coursera.org\n2. www.udemy.com\n\n>> This surely increases your chances of promotion and gives the most returns!"

            elif occupation=="Business":
                str1 += "\n\n\n>> Self Investment is the Best Investment.\nAs you are into business, you may invest your time in reading books which help grow your business.\nWe recommend checking out the following books:\n1. Think and Grow Rich\n2. Zero to One\n3. Rich Dad Poor Dad\n\n>> This surely increases your chances of growing your business and gives the most returns!"

            elif occupation=="Housemaker":
                str1 += "\n\n\n>> Self Investment is the Best Investment.\nAs you are a housemaker, you may invest your time in learning new skills at home.\nYou may help people through these skills via social media.\nHence, you can earn money via Digital Marketing.\nWe recommend you to learn about:\n1. Digital Marketing\n2. Adsense\n3. Blogging\n\n>> This surely increases your chances of improving your skills, make money as well as help others!"

            elif occupation=="Other":
                str1 += "\n\n\n>> Self Investment is the Best Investment.\nWe recommend you to invest your time and energy to learn new skills and try to be a better person.\n\nYou may read the following books to be a better version of yourself!\n1. Getting Things Done\n2. The 7 Habits of Highly Effective People\n3. Think and Grow Rich"


    text1=Text(frame3, height=10, width=50, bg='#DCDCDC',fg='blue', font=('',20), bd=-2)
    text1.insert(5.0, "Our Results")
    text1.config(state='disabled')
    text1.place(x=700, y=100)

    text1=scrolledtext.ScrolledText(frame3, height=13, width=45, bg='white',fg='green', font=('',16), bd=-2,wrap = WORD)
    text1.insert(5.0, str1)
    text1.config(state='disabled')
    text1.place(x=500, y=150)

    check_investment_options_button=Button(frame3, text = 'Check Investment Options', font=('',18), fg='red', bg='white', borderwidth=5, command=check_investment_options)
    check_investment_options_button.place(x=500,y=500)
    changeOnHover(check_investment_options_button)

    get_help_online_button=Button(frame3, text = 'Get Help Online', font=('',18), fg='red', bg='white', borderwidth=5, command=get_help_online)
    get_help_online_button.place(x=850,y=500)
    changeOnHover(get_help_online_button)


        


# GUI
text1=Text(frame3, height=1, width=25, bg='#DCDCDC',fg='red', font=('',26), bd=-2)
text1.insert(5.0, "Investment Recommendation")
text1.config(state='disabled')
text1.place(x=330, y=10)

label1 = Label(frame3, text='Monthly Income (in INR)', font=('',15), bg='#DCDCDC')
label1.place(x=30,y=100)
entry1=Entry(frame3)
entry1.place(x=270,y=100,height=30)

label1 = Label(frame3, text='Your Age (in Years)', font=('',15), bg='#DCDCDC')
label1.place(x=30,y=150)
entry2=Entry(frame3)
entry2.place(x=270,y=150,height=30)

occupation_selection=StringVar()
occupation_selection.set('Student')
label1 = Label(frame3, text='Occupation', font=('',15), bg='#DCDCDC')
label1.place(x=30,y=200)
entry_zone = OptionMenu(frame3,occupation_selection,'Student','Employee','Business','Housemaker','Other')
entry_zone.place(x=270,y=200,height=30,width=100)
changeOnHover(entry_zone)

submit_button=Button(frame3, text = 'SUBMIT', font=('',18), fg='red', bg='white', borderwidth=5, command=suggest)
submit_button.place(x=80,y=300)
changeOnHover(submit_button)
reset_button=Button(frame3, text = 'RESET', font=('',18), bg='white', borderwidth=5, command=reset_frame)
reset_button.place(x=250,y=300)
changeOnHover(reset_button)


back_button = Button(frame3, text = 'BACK', command = frame3.destroy, font=('',12), bd=-2, bg='white', borderwidth=5)
back_button.place(x=30,y=540)
changeOnHover(back_button)




frame3.mainloop()
