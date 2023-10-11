from dotenv import load_dotenv
from os import getenv
import psycopg2

load_dotenv()

user = getenv("USER")
password = getenv("PASSWORD")
server = getenv("SERVER")
#print(user, password, server)

pg_connection = psycopg2.connect(
    dbname=user,
    user=user,
    password=password,
    host=server
)

cur = pg_connection.cursor()

def read_sql_file(fpath:str):
    #open a sql file, read it, and return it to us in the function
    with open(fpath, "r") as f:
        sql_file = f.read()
    return sql_file

def create_table(sql_filepath:str):
    start = read_sql_file(sql_filepath)
    tables = start.split(';')
    for table in tables:
        try:
            print(table)
            cur.execute(table)
            pg_connection.commit()
        except psycopg2.ProgrammingError as msg:
            print(f'Command Skipped: {msg}')

    if__name__ == '__main__':
    create_tables('/Users/kali/Documents/GitHub/SQL_AmazonCart/amazon_mock_create.sql')
            
