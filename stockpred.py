import streamlit as st
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")
st.title("Stock Prediction Web App")
st.caption('_by :blue[Ananya Salian]_')

st.caption("**Due to changes in Yahoo Finance's pricing model, as of September 6th, 2024, web-scraping of historical data is no longer permitted. As such, the following data can no longer be obtained without the use of an API, or another model. This personal project is no longer interactive,  but serves as a personal user interface guide for my stock prediction projects going forward**")

st.caption("-------")


st.caption('This web app uses the time series forecasting algorithm _FBProphet_ to determine non-linear trends of forecasting. \
           As such, here, I have used Prophet to forecast future prices of specific stocks.')
st.caption('Though Prophet is adaptable and user-friendly, these results should not be taken as a substitute for professional advice.')
st.caption('The current stocks available to forecast are the following: Apple (AAPL), \
           Google (GOOGL), Microsoft (MSFT), Goldman Sachs (GS), BlackRock (BLK), Meta (META), GameStop (GME), \
           Taiwan Semiconductors (TSM), Eli Lilly (LLY) and BHP Group (BHP).')
st.caption(":blue[Users are recommended to view this page in light mode, which can be accessed from the 'Settings' page from the menu in\
           the upper right corner.]")

stocks = ("AAPL", "GOOGL", "MSFT", "GS", "BLK", "META", "GME", "TSM", "LLY", "BHP" )
selected_stock = st.selectbox("Select stocks for prediction", stocks)
n_years = st.slider("Years of prediction:", 1, 10)
period = n_years * 365

@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace = True)
    return data

data_load_state = st.text("Load data...")
data = load_data(selected_stock)
data_load_state.text("Loading data...done!")

st.subheader('Raw data')
st.write(data.tail())

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close'))
    fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()

# forecasting time!! using fb prophet
df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date":"ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

st.subheader('Forecast data')
st.write(forecast.tail())

st.subheader('Forecast Graph')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.subheader('Forecast Components')
fig2 = m.plot_components(forecast)
st.write(fig2)


st.caption('As of the 6th of May, 2024, \
           this web app is yet to be finished. I aim \
           to create a few tables and graphs that can\
           forecast stocks following a certain point in the past, and compare it with its real trends\
           to determine the accuracy of the FBProphet.')

st.caption('Last updated: 09/06/2024')
st.caption('Created: 06/01/2024')

