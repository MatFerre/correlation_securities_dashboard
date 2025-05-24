import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

st.set_page_config(layout=wide)
st.title("Correlation Securities Dashboard")

# Sidebar inputs : tickers, start date end date, reference index, time span

st.sidebar.title("Parameters")