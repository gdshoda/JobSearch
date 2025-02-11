import streamlit as st
from io import StringIO
import pandas as pd

# st.header("Upload your Resume and Cover Letters Here for Future Reference")

uploaded_resume = st.file_uploader("Upload your Resumes Here: ")

if uploaded_resume is not None:

    

    uploaded_resume_filename = uploaded_resume.name
    
    st.write(f"Successfully uploaded {uploaded_resume_filename}")

    # #read file as bytes
    # bytes_data = uploaded_file.getvalue()
    
    # st.header("Below is the bytes data")
    # st.write(bytes_data)



    # #Convert string byte data to IO
    # st.header("Converting")
    # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # st.write(stringio)

    # #Read file as string:
    # string_data = stringio.read()
    # st.write(string_data)


uploaded_cover_letter = st.file_uploader("Upload Your Cover Letters Here:")

if uploaded_cover_letter is not None:

    uploaded_cover_letter_filename = uploaded_cover_letter.name
    
    st.write(f"Successfully uploaded {uploaded_cover_letter_filename}")

    # #read file as bytes
    # bytes_data = uploaded_cover_letter.getvalue()
    
    # st.header("Below is the bytes data")
    # st.write(bytes_data)



    # #Convert string byte data to IO
    # st.header("Converting")
    # stringio = StringIO(uploaded_cover_letter.getvalue().decode("utf-8"))
    # st.write(stringio)

    # #Read file as string:
    # string_data = stringio.read()
    # st.write(string_data)

st.divider()

st.header("Below is a list of your Uploaded Resumes:")
