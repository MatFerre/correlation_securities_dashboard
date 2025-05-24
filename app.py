import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

st.set_page_config(layout="wide")
st.title("Correlation Securities Dashboard")

# Sidebar inputs : tickers, start date end date, reference index, time span

st.sidebar.title("Parameters")
tickers_input = st.sidebar.text_area("Enter a list of tickers :" , "AAPL, GOOGL, TSLA, MSFT")
tickers = [t.strip().upper() for t in tickers_input.split(",") if t.strip()]
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2020-01-01"))
end_date = st.sidebar.date_input("End Date", vaue=pd.to_datetime("today"))
reference_index = st.sidebar.text_area("Enter one reference ticker (e.g. SPGI)", "SPGI")

#Collect Data
data = yf.download(tickers, start=start_date, end=end_date)["Close"]

print(data)