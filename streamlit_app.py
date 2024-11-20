import streamlit as st

st.markdown("<h1 style='text-align: center;'>Image Downloader</h1>", unsafe_allow_html=True)
with st.form("Search"):
    keyword = st.text_input("Search Images").replace(" ", "+")
    st.form_submit_button("Search")
