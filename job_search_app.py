<<<<<<< HEAD
import pandas as pd
import streamlit as st

#testing to see if the changes get pushed
#another test

dashboard_page = st.Page("1_Journey_Dashboard.py", title = "Job Search Dashboard", icon = "👨‍🏭")
new_job_page = st.Page("2_Submit_New_Job.py", title = "Submit New Job", icon = "🉑")
event_tracker_page = st.Page("3_Application_Event_Tracking.py", title = "Application Tracker", icon = "🛤️")
resume_upload_page = st.Page("4_Resume_Cover_Letter_Storage.py", title = "Upload Resumes and Cover Letters", icon = "💌")
application_settings_page = st.Page("5_Application_Settings.py", title = "Customize Your Journey", icon = "🎡")


pg = st.navigation([dashboard_page, new_job_page, event_tracker_page, resume_upload_page, application_settings_page])
st.set_page_config(page_title = "Job Search Journey", page_icon="🛬")

=======
import pandas as pd
import streamlit as st

dashboard_page = st.Page("1_Journey_Dashboard.py", title = "Job Search Dashboard", icon = "👨‍🏭")
new_job_page = st.Page("2_Submit_New_Job.py", title = "Submit New Job", icon = "🉑")
event_tracker_page = st.Page("3_Application_Event_Tracking.py", title = "Application Tracker", icon = "🛤️")
resume_upload_page = st.Page("4_Resume_Cover_Letter_Storage.py", title = "Upload Resumes and Cover Letters", icon = "💌")
application_settings_page = st.Page("5_Application_Settings.py", title = "Customize Your Journey", icon = "🎡")


pg = st.navigation([dashboard_page, new_job_page, event_tracker_page, resume_upload_page, application_settings_page])
st.set_page_config(page_title = "Job Search Journey", page_icon="🛬")

>>>>>>> ae0f55839786f5b8d5fb87086a9a0ff123e8e78f
pg.run()