import streamlit as st
import requests

# App title
st.markdown("<h1 style='text-align: center;'>Image Downloader</h1>", unsafe_allow_html=True)

# Form for user input
with st.form("Search"):
    keyword = st.text_input("Search Images")
    search = st.form_submit_button("Search")

if search:
    # Use Unsplash API for image search
    access_key = "35T2jv2NAKACfnkaEyUMvVY-ACp0ADaOmFCNfBB-imI"
    url = f"https://api.unsplash.com/search/photos?query={keyword}&client_id={access_key}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        results = data.get("results", [])
        if results:
            # Display images in two columns
            col1, col2 = st.columns(2)
            for i, result in enumerate(results[:10]):
                image_url = result.get("urls", {}).get("small", "")
                if i % 2 == 0:
                    col1.image(image_url, use_column_width=True)
                else:
                    col2.image(image_url, use_column_width=True)
        else:
            st.write("No images found.")
    else:
        st.write("Error fetching images. Please try again later.")
