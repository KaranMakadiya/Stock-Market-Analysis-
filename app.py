import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import streamlit as st
from datetime import datetime


st.title('Stock Market Analysis')

ticker_data=st.text_input('Enter Stock Ticker','AAPL')
today_date = datetime.today().date()
start_date= st.text_input('Enter Start Date',placeholder='YYYY-MM-DD')
end_date=st.text_input('Enter End Date', today_date)

data = yf.download(ticker_data, start_date, end_date)
stock_data = yf.Ticker(ticker_data)
one_year=stock_data.history(period="1y")

def operation_on_stockdata():
         st.write(f"Displaying data for {ticker_data} from {start_date} to {end_date}")
         latest_data = data.iloc[-1]
         year_high = one_year['High'].max()
         year_low = one_year['Low'].min()
         st.write(f"Previous Close: {float(latest_data['Close']):.2f} &nbsp;&nbsp;&nbsp;&nbsp;      Open: {float(latest_data['Open']):.2f} &nbsp;&nbsp;&nbsp;&nbsp; High: {float(latest_data['High']):.2f}  &nbsp;&nbsp;&nbsp;&nbsp;     Low: {float(latest_data['Low']):.2f}")
         st.write(f"52-Week High: {float(year_high):.2f} &nbsp;&nbsp;&nbsp;&nbsp; 52-Week Low: {float(year_low):.2f} &nbsp;&nbsp;&nbsp;&nbsp;Volume: {int(latest_data['Volume']):,}")



if data.empty:
    st.error(f"No data found for {ticker_data} between {start_date} and {end_date}.")
else:    
     operation_on_stockdata()

df= data.reset_index()
 
left, middle, right = st.columns(3)
st.subheader('Closing price')
fig=plt.figure(figsize=(12,6))
plt.plot(df.Close,'b', label='price')

if left.button("MA - 50", use_container_width=True):
     ma50 = df.Close.rolling(50).mean()
     plt.plot(ma50,'y',label='ma50')
    
if middle.button("MA - 100", use_container_width=True):
    ma100 = df.Close.rolling(100).mean()
    plt.plot(ma100,'r',label='ma100')
    
if right.button("MA - 200", use_container_width=True):
     ma200 = df.Close.rolling(200).mean()
     plt.plot(ma200,'g',label='ma200')
    
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
st.pyplot(fig)

