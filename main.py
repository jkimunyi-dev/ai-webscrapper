import streamlit as st

st.title("AI Web Scrapper")
url = st.text_input("Enter website URL")

if st.button("Scrape site"):
    st.write("Scrapping the website ...")