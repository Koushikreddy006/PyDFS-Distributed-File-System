import streamlit as st
import os

STORAGE_FOLDER = "storage"
os.makedirs(STORAGE_FOLDER, exist_ok=True)

st.title("📂 PyDFS – Distributed File System (Web Demo)")

uploaded_file = st.file_uploader("Choose a file to upload")

if uploaded_file is not None:
    file_path = os.path.join(STORAGE_FOLDER, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully!")

st.subheader("Stored Files")

files = os.listdir(STORAGE_FOLDER)

if files:
    for file in files:
        st.write(file)
else:
    st.write("No files stored yet.")
Added Streamlit web demo app
