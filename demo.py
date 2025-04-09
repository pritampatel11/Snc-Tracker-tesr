import streamlit as st
import os
from datetime import datetime

# Local folder path
local_folder_path = r"C:\Users\patel\Oldendorff Carriers\Performance Desk - Documents\Performance Evaluations\1SNC"

st.title("Upload File to Local Folder - 1SNC")

name_input = st.text_input("Enter your name")
date_input = st.date_input("Select a date")

uploaded_file = st.file_uploader("Choose a file to upload")

if st.button("Upload File"):
    if not name_input:
        st.warning("Please enter your name.")
    elif not uploaded_file:
        st.warning("Please choose a file to upload.")
    else:
        file_extension = os.path.splitext(uploaded_file.name)[1]
        date_str = date_input.strftime("%Y-%m-%d")
        new_file_name = f"{name_input}_{date_str}{file_extension}"
        file_path = os.path.join(local_folder_path, new_file_name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        st.success(f"File saved successfully to the local folder as '{new_file_name}'!")
