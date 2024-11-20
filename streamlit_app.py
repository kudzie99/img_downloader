import streamlit as st
import requests
from bs4 import BeautifulSoup

st.markdown("<h1 style='text-align: center;'>Image Downloader</h1>", unsafe_allow_html=True)
with st.form("Search"):
    keyword = st.text_input("Search Images")
    keyword = keyword.replace(" ", "+")
    search = st.form_submit_button("Search")
if search:
    col1, col2 = st.columns(2)
    requests.get(f"https://www.google.com/search?q={keyword}&sca_esv=3139d74b9444d6d5&sxsrf=ADLYWIKZ_rsC2aRwwgJG-9ydBfhDe7AFWw:1732105342622&source=hp&biw=388&bih=730&ei=ftQ9Z_yJJJCUhbIP0e_5iAE&iflsig=AL9hbdgAAAAAZz3ijoK4xgB2cRXXZuvZcmq9TQZR7hTk&ved=0ahUKEwj8wKKd8-qJAxUQSkEAHdF3HhEQ4dUDCBA&uact=5&oq=cute+cats&gs_lp=EgNpbWciCWN1dGUgY2F0c0gAUABYAHAAeACQAQCYAQCgAQCqAQC4AQPIAQCKAgtnd3Mtd2l6LWltZ5gCAKACAJgDAJIHAKAHAA&sclient=img&udm=2")
    soup = BeautifulSoup(page.content, "lxml")
    rows = soup.find_all("div", class="wIjY0d jFk0f")
    for row in rows:
        figure = row.find_all("g-img", class="mNsIhb")
        for i in range(10):
            img = figure[i].find("img", class="YQ4gaf")
            source = img["src"]
            if i == 0:
                col1.st.image(source)
            else:
                col2.st.image(source)
                
