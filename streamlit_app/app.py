import streamlit as st
import tempfile

def upload_file():
    uploaded_file = st.file_uploader("Upload Image", type=['csv'])
        
    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as temp_image:
            temp_image.write(uploaded_file.getvalue())
            temp_image_path = temp_image.name
            st.success("Image uploaded successfully!")

if __name__ == "__main__":
    upload_file()