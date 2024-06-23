import streamlit as st

st.header("My Fav SC Companies")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["TSM", "NVDA", "INTC", "AVGO", "AMD" ])

with tab1:
    st.write("Taiwan Semiconductors")

with tab2:
    st.write("Nvidia")

with tab3:
    st.write("Intel")

with tab4:
    st.write("Broadcom")

with tab5:
    st.write("AMD")
    st.caption("Advanced Micro Devices, Inc.")