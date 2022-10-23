import streamlit
import yfinance

streamlit.title("""Stock Market App with *Streamlit*""")
streamlit.header("Simple Data Sience Web App")
streamlit.sidebar.header("Made by:\nAwad Soleman")

# Fetching historical data  by valid periods
data = yfinance.Ticker("AAPL").history(period="3mo")

# Markdown
streamlit.write ( """ ### Apple""")

#Detailed summary about Apple
streamlit.write(yfinance.Ticker("AAPL").info['longBusinessSummary'])

#Fetching data for DataFrame with yfinance.download() and write them.
streamlit.write(yfinance.download("AAPL",start="2012-10-13",end="2022-10-13"))

#Chart
streamlit.line_chart(yfinance.Ticker("AAPL").history(period="3mo").values)

# Calendar of events
yfinance.Ticker("AAPL").calendar

# dividend
yfinance.Ticker("AAPL").dividends

# the major shareholder of the stock
yfinance.Ticker("AAPL").major_holders

# the list of institutional_holders of the stock
yfinance.Ticker("AAPL").institutional_holders
