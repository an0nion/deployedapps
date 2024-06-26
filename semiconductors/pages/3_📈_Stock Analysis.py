import streamlit as st
import yfinance as yf

st.header("My Fav SC Companies")
st.caption("_by :blue[Ananya Salian]_")

st.set_page_config(
    page_icon="📈"
)

st.caption("This tab is currently in progress. Still currently choosing between an API-run and static page!")
st.caption("However, for the time-being, I will be making this static, and updating\
           info as I go, to personally stay on track of the performance of these stocks.")
st.caption("_Expected to be up & running: **27th June, 2024**_")
t = yf.Ticker("TSM")
n = yf.Ticker("NVDA")
q = yf.Ticker("QCOM")
i = yf.Ticker("INTC")
b = yf.Ticker("AVGO")
a = yf.Ticker("AMD")

st.caption("The information currently provided consists of data obtained from the YFinance API, and though highly accurate, has a delay of up to 15 minutes from time of web-app reload. ")
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([f"{t.info['underlyingSymbol']}", f"{n.info['underlyingSymbol']}", f"{i.info['underlyingSymbol']}", f"{q.info['underlyingSymbol']}", f"{b.info['underlyingSymbol']}", f"{a.info['underlyingSymbol']}"])



with tab1:
    st.write(f"{t.info['underlyingSymbol']}")
    st.caption(f"{t.info['longName']}")
    st.write(f"Current Share Price: {t.info['currentPrice']}")
    st.write(f"Trailing P/E Ratio: {t.info['trailingPE']}")

with tab2:
    st.write(f"{n.info['underlyingSymbol']}")
    st.caption(f"{n.info['longName']}")
    st.write(f"Current Share Price: {n.info['currentPrice']}")
    st.write(f"Trailing P/E Ratio: {n.info['trailingPE']}")

with tab3:
    st.write(f"{i.info['underlyingSymbol']}")
    st.caption(f"{i.info['longName']}")
    st.write(f"Current Share Price: {i.info['currentPrice']}")
    st.write(f"Trailing P/E Ratio: {i.info['trailingPE']}")

with tab4:
    st.write(f"{q.info['underlyingSymbol']}")
    st.caption(f"{q.info['longName']}")
    st.write(f"Current Share Price: {q.info['currentPrice']}")
    st.write(f"Trailing P/E Ratio: {q.info['trailingPE']}")

with tab5:
    st.write(f"{b.info['underlyingSymbol']}")
    st.caption(f"{b.info['longName']}")
    st.write(f"Current Share Price: {b.info['currentPrice']}")
    st.write(f"Trailing P/E Ratio: {b.info['trailingPE']}")

with tab6:
    st.write(f"{a.info['underlyingSymbol']}")
    st.caption(f"{a.info['longName']}")
    st.write(f"Current Share Price: {a.info['currentPrice']}")
    st.write(f"Trailing P/E Ratio: {a.info['trailingPE']}")
