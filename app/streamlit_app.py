import streamlit as st
import os
from datetime import datetime

STORAGE_FOLDER = "storage"
os.makedirs(STORAGE_FOLDER, exist_ok=True)

st.title("📂 PyDFS – Distributed File System (Web Demo)")

# =========================
# Upload Section
# =========================

uploaded_file = st.file_uploader("Choose a file to upload")

if uploaded_file is not None:
    file_path = os.path.join(STORAGE_FOLDER, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully!")

# =========================
# Stored Files Section
# =========================

st.subheader("📁 Stored Files")

files = os.listdir(STORAGE_FOLDER)

if files:
    for file in files:
        file_path = os.path.join(STORAGE_FOLDER, file)

        file_size = os.path.getsize(file_path) / 1024  # KB
        upload_time = datetime.fromtimestamp(
            os.path.getctime(file_path)
        ).strftime("%Y-%m-%d %H:%M:%S")

        col1, col2, col3 = st.columns([4, 2, 2])

        # File Info
        with col1:
            st.write(f"**{file}**")
            st.caption(f"Size: {file_size:.2f} KB")
            st.caption(f"Uploaded: {upload_time}")

        # Download Button
        with col2:
            with open(file_path, "rb") as f:
                st.download_button(
                    label="⬇ Download",
                    data=f,
                    file_name=file,
                    mime="application/octet-stream",
                    key=f"download_{file}"
                )

        # Delete Button
        with col3:
            if st.button("🗑 Delete", key=f"delete_{file}"):
                os.remove(file_path)
                st.success(f"{file} deleted successfully!")
                st.rerun()

        # Image Preview
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            st.image(file_path, caption=file)

        st.divider()

else:
    st.write("No files stored yet.")
