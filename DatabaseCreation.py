#database creation file
import psycopg2
import dbsettings.py


#Creates initial database using connection to postgress server
def createdatabase():
    #create connection with postgress 'server'.  note: under connect must include database=postgress
    conn = psycopg2.connect(user=dbsettings.user, host= dbsettings.host, password=dbsettings.password, database='postgres')
    cur = conn.cursor()

    #create database
    cur.execute("CREATE DATABASE " + dbsettings.database)
    conn.commit()
    cur.close()
    conn.close()

#Creates table within existing database
def createtable():
    #create connection to an existing database
    conn = psycopg2.connect(user=dbsettings.user, host= dbsettings.host, password=dbsettings.password, database=dbsettings.database)
    cur = conn.cursor()

    #table mood create
    cur.execute("CREATE TABLE mood (id serial PRIMARY KEY, mood integer, datetime timestamp)")

    #commit changes, close communication with database
    conn.commit()
    cur.close()
    conn.close()

#execute code (note: main check allows other code to be used elsewhere)
if __name__ == "__main__":
    createdatabase()
    createtable()
