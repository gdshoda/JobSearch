from faker import Faker
from faker.providers import DynamicProvider
from utils.connections_class import PostgresqlQueries
import warnings
warnings.filterwarnings("ignore")
import streamlit as st
import pandas as pd

postgres_creds = st.secrets["connections"]["postgresql"]


class FakeJobData:
    def __init__(self, conn, country):
        #establishing my database connection to use across the class
        self.conn = conn
        self.country = country
        #creating a faker version that will produce fake american data
        if self.country.lower() == 'us':
            self.faker = Faker('en_US')
            self.region_reference = "state"

        elif self.country.lower() == 'fr':
            self.faker = Faker('fr_FR')
            self.region_reference = "region"

        company_size_provider = DynamicProvider(
                                    provider_name = "company_size",
                                    elements = pd.read_sql("SELECT * FROM company_size;", self.conn).id.to_list()
                                )

        company_industry_provider = DynamicProvider(
                            provider_name = "company_industry",
                            elements = pd.read_sql("SELECT id FROM company_industry;", self.conn).id.to_list()
                        )
        
        cover_letter_provider = DynamicProvider(
                            provider_name = "cover_letter",
                            elements = pd.read_sql("""
                                                    SELECT 
                                                        enumlabel 
                                                    FROM pg_enum 
                                                    JOIN pg_type 
                                                        ON pg_enum.enumtypid = pg_type.oid 
                                                    WHERE pg_type.typname = 'cover_letter'
                                                   """, self.conn).enumlabel.to_list()
        )

        company_provider = DynamicProvider(
                            provider_name = "existing_company_id"
                            elements = pd.read_sql("SELECT id FROM company;", self.conn).id.to_list()
        )

        activity_provider = DynamicProvider(
                            provider_name= "application_activity",
                            elements = pd.read_sql("""
                                                    SELECT 
                                                        enumlabel 
                                                    FROM pg_enum 
                                                    JOIN pg_type 
                                                        ON pg_enum.enumtypid = pg_type.oid 
                                                    WHERE pg_type.typname = 'activity'
                                                   """, self.conn).enumlabel.to_list()
        )


        self.faker.add_provider(company_size_provider)
        self.faker.add_provider(company_industry_provider)
        self.faker.add_provider(cover_letter_provider)
        self.faker.add_provider(company_provider)
        self.faker.add_provider(activity_provider)
   
    def open_cursor(self):
        cursor = self.conn.cursor()
        return cursor

    def new_locality(self, cursor):
        self.city = self.faker.city()

        if self.region_reference == "state":
            self.state = self.faker.state().upper()

        elif self.region_reference == "region":
            self.state = self.faker.region().upper()
        
        print(f"""
                Attempting to find or insert {self.city} and {self.state} into the DB
                """
        )

        insert_or_find_locality_query = """ WITH inserted_locality AS (
                        INSERT INTO locality (name, region_id)
                        SELECT %s, region.id
                        FROM region
                        WHERE region.iso = %s
                        AND NOT EXISTS (
                            SELECT 1 
                            FROM locality
                            WHERE locality.name = %s AND locality.region_id = region.id
                        )
                        
                        RETURNING id
                    )

                    SELECT id 
                    FROM inserted_locality
                    UNION ALL
                    SELECT locality.id
                    FROM locality
                    JOIN region
                        ON locality.region_id = region.id
                    WHERE locality.name = %s and region.iso = %s
                """
        cursor.execute(insert_or_find_locality_query, (self.city, self.country, self.city, self.city, self.country))

        locality_id = cursor.fetchone()[0]

        self.conn.commit()
        
        print(f"Inserted or Found {self.city} in {self.state} and returned the locality id of {locality_id}")
        return locality_id

    def new_company(self):
        cursor = self.open_cursor()
        self.company_name = self.faker.company()
        self.logo = self.faker.url()
        self.hq_locality_id = self.new_locality(cursor)
        self.company_size_id = self.faker.company_size()
        self.company_industry_id = self.faker.company_industry()

        unique_company_query = """
                                SELECT 
                                    id
                                FROM company
                                WHERE name = %s
                                """
        insert_company_query = """
                                INSERT INTO company (name, logo, hq_locality_id, company_size_id, company_ind_id)
                                VALUES (%s, %s, %s, %s, %s)
                                """
        cursor.execute(unique_company_query, (self.company_name,))
        existing_company = cursor.fetchone()

        if not existing_company:
            cursor.execute(insert_company_query, (self.company_name, self.logo, self.hq_locality_id, self.company_size_id, self.company_industry_id))
            self.conn.commit()
            print(f"""
                Created the following company:\n
                Company: {self.company_name},\n
                Logo: {self.logo},\n
                HQ ID: {self.hq_locality_id},\n
                Company Size ID: {self.company_size_id},\n
                Company Industry ID: {self.company_industry_id})
                """)
        
        else:
            print(f"Company {self.company_name} already exists in db")

        cursor.close()

    def new_job_title(self, cursor):
        test = "test"

    def new_job(self):
        cursor = self.open_cursor()
        posting = self.faker.url()
        notes = self.faker.text(max_nb_chars = 140)
        job_title_id = self.new_job_title(cursor)
        job_locality_id = self.new_locality(cursor)
        company_id = self.faker.existing_company_id()
    
    def new_language(self):
        
        
        language = "english"

    def new_application_entry(self):
        cover_letter = self.faker.cover_letter()
        addt_ques = self.faker.random_element([1,0])
        reference = self.faker.random_element([1,0])
        expiration = f"{self.faker.random_int(min = 2, max = 30)} days"
        if self.country.lower() == 'us':
            language = 'english'
        elif self.country.lower() == 'fr':
            language = 'french'
        
        language_id = "english"






    






# pq = PostgresqlQueries(postgres_creds)
# cnxn = pq.connect(export = True)
# enums = pq.enum_values()

# # tables = pq.tables_and_columns()

# for _, row in enums.iterrows():
#     print(row)

# test = FakeJobData(conn = cnxn, country = "US")
# test.new_company()

# pq.disconnect()