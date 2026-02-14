import streamlit as st
import os

STORAGE_FOLDER = "storage"
os.makedirs(STORAGE_FOLDER, exist_ok=True)

st.title("📂 PyDFS – Distributed File System (Web Demo)")

# Upload Section
uploaded_file = st.file_uploader("Choose a file to upload")

if uploaded_file is not None:
    file_path = os.path.join(STORAGE_FOLDER, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully!")

# Display Stored Files
st.subheader("Stored Files")

files = os.listdir(STORAGE_FOLDER)

if files:
    for file in files:
        file_path = os.path.join(STORAGE_FOLDER, file)

        col1, col2 = st.columns([3, 1])

        with col1:
            st.write(file)

        with col2:
            with open(file_path, "rb") as f:
                st.download_button(
                    label="Download",
                    data=f,
                    file_name=file,
                    mime="application/octet-stream"
                )

        # If image file → preview
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            st.image(file_path, caption=file)

else:
    st.write("No files stored yet.")
