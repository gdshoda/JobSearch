import requests
import psycopg2
import pandas as pd
import numpy as np
import os
import datetime
import streamlit as st
from bs4 import BeautifulSoup

class PostgresqlQueries():
    """
    A class to create connections to the postgresql instance, run queries, and write data for the
    """
    def __init__(self, creds):
        self.creds = creds
        self.host = creds["host"]
        self.dbname = creds["database"]
        self.user = creds["username"]
        self.password = creds["password"]
        self.port = creds["port"]

    def connect(self, export: bool = False):
        """
        Creating a new connection to the postgresql database
        """
        self.conn = psycopg2.connect(
            host = self.host,
            port = self.port,
            dbname = self.dbname,
            user = self.user,
            password = self.password
        )
        if bool:
            return self.conn

    def disconnect(self):
        """
        Closing the connection to the postgresql database
        """
        self.conn.close()
    
    def cursor(self):
        """
        creating a new cursor for executing queries to the postgresql database
        """
        self.cursor = self.conn.cursor()

    def close_cursor(self):
        """
        Closing the current cursor being used
        """
        self.cursor.close()

    def tables_and_columns(self):
        """
        Function to call all of the tables and columns in the postgres instance for updating purposes
        """
        query = """
                SELECT 
                    t.table_name, 
                    c.column_name, 
                    c.data_type
                FROM information_schema.tables t
                JOIN information_schema.columns c 
                    ON t.table_name = c.table_name
                WHERE t.table_schema = 'public'  -- Adjust if your tables are in a different schema
                    AND t.table_type = 'BASE TABLE'  -- Excludes views
                ORDER BY t.table_name, c.ordinal_position;
                """
        
        df = pd.read_sql(query, self.conn)
        return df

    def enum_values(self):
        """
        Function to call the enum values in the database so I can quickly see the values needed when writing to the database
        """
        query = """
                SELECT 
                    t.typname AS enum_type, 
                    e.enumlabel AS enum_value
                FROM 
                    pg_enum e
                JOIN 
                    pg_type t ON e.enumtypid = t.oid
                ORDER BY 
                    t.typname, e.enumsortorder;
                """
        df = pd.read_sql(query, self.conn)
        return df

    def get_job_details(self):
        """
        Function to return the information you would want from a job posting: including company name, job title, city, state, and last activity (status) of the job application
        """
        query = """
                SELECT company.name AS Company, 
                job_titles.title AS Title, 
                locality.name AS City, 
                region.name AS State, 
                hiring_activity.activity AS Activity
                FROM company
                LEFT JOIN job_details
                ON company.id = job_details.company_id
                LEFT JOIN job_titles
                ON job_details.job_title_id = job_titles.id
                LEFT JOIN locality
                ON job_details.job_locality_id = locality.id
                LEFT JOIN region
                ON locality.region_id = region.id
                LEFT JOIN hiring_process_activity
                ON job_details.id = hiring_process_activity.job_id
                LEFT JOIN hiring_activity
                ON hiring_process_activity.activity_id = hiring_activity.id
                """
        
        self.job_details = pd.read_sql(query, self.conn)
        return self.job_details
    