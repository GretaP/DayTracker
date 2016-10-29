import psycopg2
import datetime

conn = psycopg2.connect("dbname=mood user=postgres")
cur = conn.cursor()


#collect mood from user
mood=

#adds time variable
#http://initd.org/psycopg/docs/usage.html#date-time-objects-adaptation
dt = datetime.datetime.now()
dtsql = cur.mogrify("SELECT %s, %s, %s;", (dt, dt.date(), dt.time()))

#adds current mood and date/time to database
cur.execute("INSERT INTO mood (mood, datetime) VALUES (%s, %s)", (mood, dtsql))


#commit changes, close communication with database (avoids problems)
conn.commit()
cur.close()
conn.close()