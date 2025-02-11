<<<<<<< HEAD
import streamlit as st

st.header("Enter a Job Application you've Submitted to your Tracker:")

pdf_option = st.radio("Input Method", ["Shortcut with PDF of application", "Submit Full Form"])

if pdf_option == "Shortcut with PDF of application":
    uploaded_application = st.file_uploader("Upload your Application PDF Here:")


with st.form("Job Application"):
    job_hyperlink = st.text_input("Link to Job Posting", "")
    st.write()

    job_title = st.text_input("Job Title", "")

    job_location = st.text_input("Job Location", "")

    job_company = st.text_input("Company Name", "")

    resume_used = st.selectbox("Which Resume did you use for this job application", "Select a Resume")

    uploaded_resume = st.file_uploader("Upload New Resume: ")

    cover_letter_required = st.radio("Was a cover letter required on this application?",
                                     ["Required", "Optional", "Not Available"],
                                     captions = ["Company Required a Cover Letter in the application",
                                                 "Cover Letter was optional",
                                                 "There was no option to upload a cover letter with this application"]
    )


    if cover_letter_required in ["Required", "Optional"]:
        cover_letter_used = st.selectbox("Which Cover Letter did you use for this job application?", ("Cover Letter 1", "Cover Letter 2"))

        uploaded_cover_letter = st.file_uploader("Upload New Cover Letter: ")

    additional_questions = st.radio("Did the Application have additional questions you had to answer (Non DEI Questions)?",
                                    ["Yes", "No"])
    
    additional_question1 = st.text_input("What was the first additional question?")

    additional_question1_response = st.text_input("What was your response to that question?")

    job_sentiment_scale = st.slider("Job Feeling", min_value = 1, max_value = 10)

    job_qualification_scale = st.slider("How Qualified did you feel for the Job?", min_value = 1, max_value = 10)

    #This is the last section of the form with the submit button
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(f"Application for {job_title} at {job_company} successfully submitted!")





# with cover_letter_placeholder:
=======
import streamlit as st

st.header("Enter a Job Application you've Submitted to your Tracker:")

pdf_option = st.radio("Input Method", ["Shortcut with PDF of application", "Submit Full Form"])

if pdf_option == "Shortcut with PDF of application":
    uploaded_application = st.file_uploader("Upload your Application PDF Here:")


with st.form("Job Application"):
    job_hyperlink = st.text_input("Link to Job Posting", "")
    st.write()

    job_title = st.text_input("Job Title", "")

    job_location = st.text_input("Job Location", "")

    job_company = st.text_input("Company Name", "")

    resume_used = st.selectbox("Which Resume did you use for this job application", "Select a Resume")

    uploaded_resume = st.file_uploader("Upload New Resume: ")

    cover_letter_required = st.radio("Was a cover letter required on this application?",
                                     ["Required", "Optional", "Not Available"],
                                     captions = ["Company Required a Cover Letter in the application",
                                                 "Cover Letter was optional",
                                                 "There was no option to upload a cover letter with this application"]
    )


    if cover_letter_required in ["Required", "Optional"]:
        cover_letter_used = st.selectbox("Which Cover Letter did you use for this job application?", ("Cover Letter 1", "Cover Letter 2"))

        uploaded_cover_letter = st.file_uploader("Upload New Cover Letter: ")

    additional_questions = st.radio("Did the Application have additional questions you had to answer (Non DEI Questions)?",
                                    ["Yes", "No"])
    
    additional_question1 = st.text_input("What was the first additional question?")

    additional_question1_response = st.text_input("What was your response to that question?")

    job_sentiment_scale = st.slider("Job Feeling", min_value = 1, max_value = 10)

    job_qualification_scale = st.slider("How Qualified did you feel for the Job?", min_value = 1, max_value = 10)

    #This is the last section of the form with the submit button
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(f"Application for {job_title} at {job_company} successfully submitted!")





# with cover_letter_placeholder:
>>>>>>> ae0f55839786f5b8d5fb87086a9a0ff123e8e78f
