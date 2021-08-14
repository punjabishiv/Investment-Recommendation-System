# GUI
from tkinter import *
from PIL import Image
import webbrowser


# LinearRegression is a machine learning library for linear regression
from sklearn.linear_model import LinearRegression
import datetime as dt

# pandas and numpy are used for data manipulation
import pandas as pd
import numpy as np


# matplotlib and seaborn are used for plotting graphs
import matplotlib.pyplot as plt
# %matplotlib inline
plt.style.use('seaborn-darkgrid')

# yahoo finance is used to fetch data
import yfinance as yf

def know_more_function():
    link1 = "https://groww.in/blog/beginners-guide-to-investing-in-gold-india/"
    webbrowser.open(link1)


def latest_trends_function():
    link1 = "https://goldprice.org/"
    webbrowser.open(link1)

def changeOnHover(button, colorOnHover = 'gray', colorOnLeave = 'white'):
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover, cursor="hand2"))

    # background color on leaving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

def load_and_generate_results():
    Df = yf.download('GLD', '2008-01-01', '2020-6-22', auto_adjust=True)
    
    ######################## Text Box
    text = Text(frame3, height=1, width=30, bg='#DCDCDC', fg='blue', font=('', 15), bd=-2)
    text.insert(5.0, "Dataset Loaded...")
    text.config(state='disabled')
    text.place(x=80, y=200)


    # Only keep close columns
    Df = Df[['Close']]

    # Drop rows with missing values
    Df = Df.dropna()

    # Plot the closing price of GLD
    Df.Close.plot(figsize=(10, 7),color='r')
    plt.ylabel("Gold ETF Prices")
    plt.title("Gold ETF Price Series")
    plt.plot()
    plt.savefig('gold_plotted_graph.png')
    plt.clf()
    ######################## Text Box
    text = Text(frame3, height=1, width=30, bg='#DCDCDC', fg='blue', font=('', 15), bd=-2)
    text.insert(5.0, "Original Values saved in Memory...")
    text.config(state='disabled')
    text.place(x=80, y=240)
    


    # Define explanatory variables
    Df['S_3'] = Df['Close'].rolling(window=3).mean()
    Df['S_9'] = Df['Close'].rolling(window=9).mean()
    Df['next_day_price'] = Df['Close'].shift(-1)

    Df = Df.dropna()
    X = Df[['S_3', 'S_9']]

    # Define dependent variable
    y = Df['next_day_price']



    # Split the data into train and test dataset
    t = .8
    t = int(t*len(Df))

    # Train dataset
    X_train = X[:t]
    y_train = y[:t]

    # Test dataset
    X_test = X[t:]
    y_test = y[t:]


    # Create a linear regression model
    linear = LinearRegression().fit(X_train, y_train)
    print("Linear Regression model")
    print("Gold ETF Price (y) = %.2f * 3 Days Moving Average (x1) \
    + %.2f * 9 Days Moving Average (x2) \
    + %.2f (constant)" % (linear.coef_[0], linear.coef_[1], linear.intercept_))


    # Predicting the Gold ETF prices
    predicted_price = linear.predict(X_test)
    predicted_price = pd.DataFrame(
        predicted_price, index=y_test.index, columns=['price'])
    predicted_price.plot(figsize=(10, 7))
    y_test.plot()
    plt.legend(['predicted_price', 'actual_price'])
    plt.ylabel("Gold ETF Price")
    plt.plot()
    plt.savefig('gold_predicted_graph.png')
    plt.clf()
    ######################## Text Box
    text = Text(frame3, height=1, width=30, bg='#DCDCDC', fg='blue', font=('', 15), bd=-2)
    text.insert(5.0, "Prediction Model Generated...")
    text.config(state='disabled')
    text.place(x=80, y=280)
    

    # R square
    r2_score = linear.score(X[t:], y[t:])*100
    print("R2 Score: ",float("{0:.2f}".format(r2_score)))


    gold = pd.DataFrame()

    gold['price'] = Df[t:]['Close']
    gold['predicted_price_next_day'] = predicted_price
    gold['actual_price_next_day'] = y_test
    gold['gold_returns'] = gold['price'].pct_change().shift(-1)

    gold['signal'] = np.where(gold.predicted_price_next_day.shift(1) < gold.predicted_price_next_day,1,0)

    gold['strategy_returns'] = gold.signal * gold['gold_returns']
    ((gold['strategy_returns']+1).cumprod()).plot(figsize=(10,7),color='g')
    plt.ylabel('Cumulative Returns')
    plt.savefig('gold_cumulative_graph.png')
    plt.clf()
    ######################## Text Box
    text = Text(frame3, height=1, width=30, bg='#DCDCDC', fg='blue', font=('', 15), bd=-2)
    text.insert(5.0, "Cumulative Values Calculated...")
    text.config(state='disabled')
    text.place(x=80, y=320)
    

    # Calculate sharpe ratio
    sharpe = gold['strategy_returns'].mean()/gold['strategy_returns'].std()*(252**0.5)
    'Sharpe Ratio %.2f' % (sharpe)


    # import datetime and get today's date
    current_date = dt.datetime.now()

    # Get the data
    data = yf.download('GLD', '2008-06-01', current_date, auto_adjust=True)
    data['S_3'] = data['Close'].rolling(window=3).mean()
    data['S_9'] = data['Close'].rolling(window=9).mean()
    data = data.dropna()

    # Forecast the price
    data['predicted_gold_price'] = linear.predict(data[['S_3', 'S_9']])
    data['signal'] = np.where(data.predicted_gold_price.shift(1) < data.predicted_gold_price,"Buy","Wait for Sometime")

    # Print the forecast
    data = data.tail(1)[['signal','predicted_gold_price']].T
    suggestion = data.iloc[0][0]
    prediction = data.iloc[1][0]
    prediction = round(prediction, 2)
    
    def show_result_function():
        text1=Text(frame3, height=1, width=35, bg='#DCDCDC',fg='green', font=('',14), bd=-2)
        text1.insert(5.0, "Our Suggestion  :   " + str(suggestion))
        text1.config(state='disabled')
        text1.place(x=650, y=250)

        text2=Text(frame3, height=1, width=25, bg='#DCDCDC',fg='green', font=('',14), bd=-2)
        text2.insert(5.0, "Our Prediction    :   " + str(prediction))
        text2.config(state='disabled')
        text2.place(x=650, y=300)
    

    def original_values():
        img = Image.open('gold_plotted_graph.png')
        img.show()

    def predicted_values():
        img = Image.open('gold_predicted_graph.png')
        img.show()

    def cumulative_results():
        img = Image.open('gold_cumulative_graph.png')
        img.show()

    b1=Button(frame3, text = 'Original Values', font=('',18), fg='red', bg='white', borderwidth=5, command=original_values)
    b1.place(x=80,y=400)
    b2=Button(frame3, text = 'Predicted Values', font=('',18), fg='red', bg='white', borderwidth=5, command=predicted_values)
    b2.place(x=310,y=400)
    b3=Button(frame3, text = 'Cumulative Returns', font=('',18), fg='red', bg='white', borderwidth=5, command=cumulative_results)
    b3.place(x=550,y=400)
    show_result_button=Button(frame3, text = 'Our Recommendation', font=('',18), fg='red', bg='white', borderwidth=5, command=show_result_function)
    show_result_button.place(x=700,y=130)
    
    changeOnHover(b1)
    changeOnHover(b2)
    changeOnHover(b3)
    changeOnHover(show_result_button)


######################## Window
frame3=Tk()
frame3.title('Gold Investment')
frame3.config(background='#DCDCDC')
frame3.geometry('1058x595')
windowWidth = 1058
windowHeight = 595
position_x = int(frame3.winfo_screenwidth()/2 - windowWidth/2)
position_y = int(frame3.winfo_screenheight()/2 - windowHeight/2)
frame3.geometry("+{}+{}".format(position_x, position_y))
########################

text1=Text(frame3, height=1, width=18, bg='#DCDCDC',fg='red', font=('',26), bd=-2)
text1.insert(5.0, "Gold Investment")
text1.config(state='disabled')
text1.place(x=400, y=10)

text1=Text(frame3, height=1, width=100, bg='#DCDCDC',fg='green', font=('',14), bd=-2)
text1.insert(5.0, "(An Investment trusted in India from long time)")
text1.config(state='disabled')
text1.place(x=330, y=50)

load_button=Button(frame3, text = 'Load Data and Generate Results', font=('',18), fg='red', bg='white', borderwidth=5, command=load_and_generate_results)
load_button.place(x=80,y=130)
changeOnHover(load_button)

back_button = Button(frame3, text = 'BACK', command = frame3.destroy, font=('',16), bd=-2, bg='white', borderwidth=5,)
back_button.place(x=50,y=500)
changeOnHover(back_button)

know_more = Button(frame3, text = 'Know More', font=('',18), bd=-2, bg='yellow', borderwidth=5, fg = 'red', command = know_more_function)
know_more.place(x=800,y=500)
changeOnHover(know_more, 'skyblue', 'yellow')

latest_trends = Button(frame3, text = 'Latest Trends', font=('',18), bd=-2, bg='yellow', borderwidth=5, fg = 'red', command = latest_trends_function)
latest_trends.place(x=600,y=500)
changeOnHover(latest_trends, 'skyblue', 'yellow')

frame3.mainloop()