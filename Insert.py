import psycopg2
import datetime

#later: try block for connection issues

#collect mood from user
mood=

#adds entry to database with input mood (1-5) and auto timestamp
def insertmood(mood):
    conn = psycopg2.connect("dbname=mood user=postgres")
    cur = conn.cursor()
    #adds time variable
    #http://initd.org/psycopg/docs/usage.html#date-time-objects-adaptation
    dt = datetime.datetime.now()
    dtsql = cur.mogrify("SELECT %s, %s, %s;", (dt, dt.date(), dt.time()))
    #adds current mood and date/time to database
    cur.execute("INSERT INTO mood (mood, datetime) VALUES (%s, %s)", (mood, dtsql))
    conn.commit()
    # close communication with database (avoids problems)
    cur.close()
    conn.close()

def getmood(date):
    pass

def getmoodaverage():
    pass







