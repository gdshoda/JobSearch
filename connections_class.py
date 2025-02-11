import requests
import psycopg2
import pandas as pd
import numpy as np
import os
import datetime
import streamlit as st
from bs4 import BeautifulSoup

class ConnectionsManager():
    def __init__(self):
        self.cnxn = None

    #@st.cache_resource
    def get_postgres(self):
        if self.cnxn is None:
            self.cnxn = psycopg2.connect(
                host = "jobsearch-test.cz8su8kcabuv.us-east-2.rds.amazonaws.com",
                database = "postgres",
                user = "gdshoda",
                password = "p)aK1g3yW]1(6UbIeOGQN2j[u*B]",
                port = 5432
            )
        
        return self.cnxn
    


    def fetch_data(self, query):
        cursor = self.cnxn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    
instance = ConnectionsManager()
conn = instance.get_postgres()

cursor = conn.cursor()
cursor.execute("SELECT version();")
print(cursor.fetchone())
cursor.close()
