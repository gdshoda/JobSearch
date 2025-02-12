CREATE TABLE [IF NOT EXISTS] country (
    iso VARCHAR(2) PRIMARY KEY,
    name VARCHAR UNIQUE NOT NULL
);

CREATE TABLE [IF NOT EXISTS] region (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    abbreviation VARCHAR,
    FOREIGN KEY (iso) REFERENCES country (iso)
);

CREATE TABLE [IF NOT EXISTS] locality (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    FOREIGN KEY (region_id) REFERENCES region (id)
);

CREATE TYPE company_size AS ENUM ('1-10, 11-50', '51-200', '201-500', '501-1000', '1001-5000', '5001-10,000', '10,000+')

CREATE TABLE [IF NOT EXISTS] company_size (
    id SERIAL PRIMARY KEY,
    size company_size
);

CREATE TABLE [IF NOT EXISTS] company_industry (
    id SERIAL PRIMARY KEY,
    industry VARCHAR UNIQUE NOT NULL
);

CREATE TABLE [IF NOT EXISTS] company (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    logo VARCHAR,
    FOREIGN KEY (hq_locality_id) REFERENCES locality (id),
    FOREIGN KEY (company_size_id) REFERENCES company_size (id),
    FOREIGN KEY (company_ind_id) REFERENCES company_industry (id)
);

CREATE TABLE [IF NOT EXISTS] job_titles (
    id SERIAL PRIMARY KEY,
    title VARCHAR UNIQUE NOT NULL
);

CREATE TABLE [IF NOT EXISTS] job_details (
    id SERIAL PRIMARY KEY,
    posting VARCHAR NOT NULL,
    notes VARCHAR,
    FOREIGN KEY (job_title_id) REFERENCES job_titles (id),
    FOREIGN KEY (job_locality_id) REFERENCES locality (id),
    FOREIGN KEY (company_id) REFERENCES company (id)
);

CREATE TABLE [IF NOT EXISTS] languages (
    id SERIAL PRIMARY KEY,
    language VARCHAR UNIQUE NOT NULL
);

CREATE TABLE [IF NOT EXISTS] username (
    id SERIAL PRIMARY KEY,
    username VARCHAR UNIQUE NOT NULL
);

CREATE TABLE [IF NOT EXISTS] password (
    id VARCHAR PRIMARY KEY,
    pass_hash TEXT NOT NULL
);

CREATE TABLE [IF NOT EXISTS] email (
    id SERIAL PRIMARY KEY,
    email VARCHAR UNIQUE NOT NULL
);

CREATE TABLE [IF NOT EXISTS] company_account (
    id SERIAL PRIMARY KEY,
    website VARCHAR NOT NULL,
    FOREIGN KEY (company_id) REFERENCES company (id),
    FOREIGN KEY (username_id) REFERENCES username (id),
    FOREIGN KEY (password_id) REFERENCES password (id),
    FOREIGN KEY (email_id) REFERENCES email (id)
);

CREATE TYPE cover_letter AS ENUM ('REQUIRED', 'OPTIONAL', 'NONE')

CREATE TABLE [IF NOT EXISTS] application_details (
    id SERIAL PRIMARY KEY,
    cover_letter cover_letter NOT NULL,
    addt_ques BIT(1) NOT NULL,
    references BIT(1) NOT NULL,
    expiration interval,
    FOREIGN KEY (language_id) REFERENCES languages (id),
    FOREIGN KEY (account_id) REFERENCES company_account (id),
    FOREIGN KEY (job_id) REFERENCES job_details (id)
);

CREATE TYPE activity AS ENUM ('APPLICATION', 'INTERVIEW', 'ASSESSMENT', 'REJECTION')

CREATE TABLE [IF NOT EXISTS] hiring_activity (
    id SERIAL PRIMARY KEY,
    activity activity NOT NULL
);

CREATE TABLE [IF NOT EXISTS] hiring_process_activity (
    id SERIAL PRIMARY KEY,
    activity_date TIMESTAMP,
    FOREIGN KEY (activity_id) REFERENCES hiring_activity (id),
    FOREIGN KEY (job_id) REFERENCES job_details (id)
);

