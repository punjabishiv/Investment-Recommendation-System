# Fuzzy Logic
from tkinter import *
import os
import requests
import pandas as pd
from tkinter import scrolledtext

def current_market():
    os.system("python current_market_module.py")

def changeOnHover(button, colorOnHover = 'gray', colorOnLeave = 'white'):
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover, cursor="hand2"))

    # background color on leaving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

def show_recommendations():
    # tickers = si.tickers_sp500()          # 500 stocks on Yahoo Finance
    tickers = ['INDUSINDBK.NS','NATIONALUM.NS','LT.NS','BANKBARODA.NS','TITAN.NS','RPOWER.NS','SAIL.NS','IDEA.BO','HDFCLIFE.NS','PNB.NS','BHEL.NS','CANBK.NS','WIPRO.NS','UCOBANK.NS','INDOCO.NS','L&TFH.NS','JPPOWER.NS','LAKSHVILAS.NS','HCC.NS','IBULHSGFIN.NS','JPASSOCIAT.NS','UNIONBANK.NS','TCI.NS','RUBYMILLS.NS','REDINGTON.BO']
    # tickers.extend(['RCOM.NS','IDEA.NS','PNB.NS','RPOWER.NS','RCOM.BO','RPOWER.BO','IDEA.BO','SAIL.NS','DISHTV.NS','BANKBARODA.NS','SBIN.NS','UCOBANK.NS','GTLINFRA.NS','YESBANK.NS','BHEL.NS','IDFCFIRSTB.NS','CANBK.NS','NATIONALUM.NS','RELINFRA.NS','RTNPOWER.NS','MTNL.NS','TATASTLBSL.NS','3IINFOTECH.NS','RELCAPITAL.NS','ZEEL.NS'])
    recommendations = []

    for ticker in tickers:
        lhs_url = 'https://query2.finance.yahoo.com/v10/finance/quoteSummary/'
        rhs_url = '?formatted=true&crumb=swg7qs5y9UP&lang=en-US&region=US&' \
                'modules=upgradeDowngradeHistory,recommendationTrend,' \
                'financialData,earningsHistory,earningsTrend,industryTrend&' \
                'corsDomain=finance.yahoo.com'
                
        url =  lhs_url + ticker + rhs_url
        r = requests.get(url)
        if not r.ok:
            recommendation = 6
        try:
            result = r.json()['quoteSummary']['result'][0]
            recommendation =result['financialData']['recommendationMean']['fmt']
        except:
            recommendation = 6
        
        recommendations.append(recommendation)
        
        print("--------------------------------------------")
        print ("{} has an average recommendation of: ".format(ticker), float(recommendation))
        
        
    dataframe = pd.DataFrame(list(zip(tickers, recommendations)), columns =['Company', 'Recommendations']) 
    dataframe = dataframe.set_index('Company')

    dataframe.to_csv('recommendations.csv')

    data1 = pd.read_csv('recommendations.csv')
    data1 = data1.sort_values(['Recommendations'])
    str1 = "Symbol\t\tRating\tNormalized\tFuzzy O/P\n-----------------------------------------------------------------------"
    for i in range(len(tickers)):

        if data1.iloc[i][1] == 6:
            continue

        str1 += "\n" + str(data1.iloc[i][0]) + "\t\t" + str(data1.iloc[i][1])
        rating = float(data1.iloc[i][1])

        old_value = rating
        old_min = 1
        old_max = 5
        new_min = 0
        new_max = 1
        normalized_value = ( (old_value - old_min) / (old_max - old_min) ) * (new_max - new_min) + new_min
        
        fuzzy_normalized_value = 1-normalized_value
        fuzzy_normalized_value = round(fuzzy_normalized_value, 2)

        str1 += "\t" + str(fuzzy_normalized_value)

        fuzzy = ""
        if 0<=fuzzy_normalized_value<=0.2:
            fuzzy = "Sell"
        elif 0.2<fuzzy_normalized_value<=0.4:
            fuzzy = "Underperforming"
        elif 0.4<fuzzy_normalized_value<=0.6:
            fuzzy = "Hold"
        elif 0.6<fuzzy_normalized_value<=0.8:
            fuzzy = "Buy"
        elif fuzzy_normalized_value>0.8:
            fuzzy = "Strong Buy"
        str1 += "\t" + fuzzy

    text1=scrolledtext.ScrolledText(frame3, height=13, width=45, bg='white',fg='green', font=('',16), bd=-2,wrap = WORD)
    text1.insert(5.0, str1)
    text1.config(state='disabled')
    text1.place(x=500, y=150)

    know_more_button = Button(frame3, text = 'Know More About\na Particular Stock', command = current_market, font=('',12), bd=-2, bg='white', borderwidth=5)
    know_more_button.place(x=500,y=500)
    changeOnHover(know_more_button)

    text2=Text(frame3, height=3, width=40, bg='#DCDCDC',fg='red', font=('',12), bd=-2, wrap = WORD)
    text2.insert(5.0, "Please note the Stock Symbol and then enter the same after clicking on this button to get more information about that stock.")
    text2.config(state='disabled')
    text2.place(x=680, y=500)


frame3=Tk()
frame3.title('Investment Recommendation Window')
frame3.config(background='#DCDCDC')
frame3.geometry('1058x595')
windowWidth = 1058
windowHeight = 595
position_x = int(frame3.winfo_screenwidth()/2 - windowWidth/2)
position_y = int(frame3.winfo_screenheight()/2 - windowHeight/2)
frame3.geometry("+{}+{}".format(position_x, position_y))

######################## Images
image1 = PhotoImage(file='our_recommendations_bg.png')
background = Label(frame3, image=image1)
background.place(x=0, y=0)
########################

show_recommendations_button = Button(frame3, text = 'Load Real Time Recommendations', command = show_recommendations, font=('',12), bd=-2, bg='white', borderwidth=5)
show_recommendations_button.place(x=100,y=400)
changeOnHover(show_recommendations_button)

back_button = Button(frame3, text = 'BACK', command = frame3.destroy, font=('',12), bd=-2, bg='white', borderwidth=5)
back_button.place(x=30,y=540)
changeOnHover(back_button)


frame3.mainloop()

