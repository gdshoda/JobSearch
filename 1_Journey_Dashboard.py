import streamlit as st
import pandas as pd
import numpy as np
import time
import psycopg2
from utils.connections_class import PostgresqlQueries

#read database credentials from secrets.toml file

postgres_creds = st.secrets["connections"]["postgresql"]


st.markdown("# Job Search Journey")
st.write("In this page I will list out all of the jobs I have applied for")

pq = PostgresqlQueries(postgres_creds)

pq.connect()
df = pq.get_job_details()
df
pq.disconnect()