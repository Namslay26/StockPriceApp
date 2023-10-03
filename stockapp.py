import yfinance as yf
import streamlit as st

#header, 
st.write("""
# Simple Stock Price App
    Search your desired stock and find out the close and volume price!
""")

st.write("Give your input ticket symbol here, ")
ticketSym =st.text_input("Input stock symbol", "GOOGL")
tickerData = yf.Ticker(ticketSym)
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
st.write("""
## Showing Closing and Volume for
""", ticketSym)
st.write("""# Closing Price""")
st.line_chart(tickerDf.Close)
st.write("""# Volume Price""")
st.line_chart(tickerDf.Volume)