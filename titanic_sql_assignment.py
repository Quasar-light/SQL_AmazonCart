"""This repo contains a file named Titanic. Your task is to load the data from the provided file(use pandas).

Using the psycopg2 and pandas library:

Read in the titanic.csv file to a DataFrame object.
Use df.to_sql() or create a Base class to insert the data into a new table named titanic in a PostGreSQL database.
Then, in SQL, write the following queries to test:

Count how many rows you have.
How many people survived?
What passenger class has the largest population?
These queries should be saved to a .sql file and uploaded along with your pipeline to create the database/table"""
import psycopg2
import pandas as pd

from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)

df = pd.read_csv('/Users/kali/Documents/GitHub/SQL_AmazonCart/Titanic copy.csv')
df.head()

df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('/', '_')
df.head()

connection = "postgresql://kpzssiwa:PHjvV16MAozR4OZE2ia_s33DsWEHawDN@peanut.db.elephantsql.com/kpzssiwa"
df.to_sql('df', con=connection, if_exists='fail')

""" 
How many rows?
sql
SELECT COUNT(*) FROM titanic
answer: 887
"""

"""
how many ppl survived?
SELECT SUM(survived) FROM df
answer: 0.342e3 (342)
"""

"""
what class had the largest population
SELECT pclass, COUNT(pclass) FROM df
GROUP BY pclass

answer:
pclass	count
1	216
3	487
2	184

"""






