import streamlit as st
import pandas as pd
import numpy as np
import time






st.markdown("# Job Search Journey")
st.write("In this page I will list out all of the jobs I have applied for")

conn = st.connection("postgresql", type = "sql")
df = conn.query('SELECT * FROM job_details;')
df