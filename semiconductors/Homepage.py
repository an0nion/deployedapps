import streamlit as st

st.set_page_config(
    page_title= "Multipage app",
    page_icon="🏡"
)

st.title("Home Page")
st.sidebar.success("Select a page above.")
st.caption("_By :blue[Ananya Salian]_")

st.subheader("Please ensure the menu on the right-hand side of your screen is visible!")
st.write("This is a small passion project I have made regarding the Semiconductor Industry following recent events and news.\
         The aim of this project is to consolidate knowledge regarding this growing field, whilst building on my coding and financial\
         understanding. This project will also obtain Financial Data of a few Semiconductor Companies, chosen due to their market share and/or my own\
         personal interests.")

st.write("This project is currently _ongoing_! I have placed this on a web app\
          so I can easily refer to it and add information from multiple devices.\
         If you see any errors or areas I can improve on, dont hesitate to send me a message via\
         my website, where my contacts are located!")

st.link_button("Go to website", "https://ananyadsal.webflow.io/")


