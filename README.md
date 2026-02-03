### LIFE_TRACE
A full stack webdev project done using nextjs

## MVP
Users can log daily entries
app shows last 7 day summary and 
3-5 actionable isights


## DATABASE SCHEMA
# users

user_id        UUID / INT (PK)
name           VARCHAR
date_of_birth  DATE
gender         ENUM / VARCHAR (nullable)
created_at     TIMESTAMP

# entries

entry_id           UUID / INT (PK)
user_id            FK → users(user_id)
entry_date         DATE

sleep_hours        FLOAT
work_hours         FLOAT
screen_time_total  FLOAT
screen_time_unprod FLOAT

stress_level       INT   -- 1 to 10
mood               INT   -- 1 to 10
social_level       INT   -- 1 to 10

good_remarks       TEXT
bad_remarks        TEXT

created_at         TIMESTAMP
UNIQUE (user_id, entry_date)


## How to Run
pip install -r requirements.txt
uvicorn main:app --reload // to run backend