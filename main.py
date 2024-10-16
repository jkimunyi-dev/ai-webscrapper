import streamlit as st
from scrape import scrape_website_with_brightdata, custon_webscrapper

st.title("AI Web Scrapper")
url = st.text_input("Enter website URL")

if st.button("Scrape site"):
    st.write("Scrapping the website ...")
    result = scrape_website_with_brightdata(url)
    print(result)