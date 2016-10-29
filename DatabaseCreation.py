#database creation file
import psycopg2

conn = psycopg2.connect("dbname=mood user=postgres")
cur = conn.cursor()

#not sure if timestamp will work; will need to work with Python time
#possible solution from stackoverflow:
# cur.execute("INSERT INTO test_table (buildingID,datetime) VALUES(%s, now() )",
#     ("01", ))
# now() returns the current time as a timestamp with time zone type, and will be run on the server side after the first %s is replaced by psycopg2 (via libpq) by 01.
#
# Also note that the tuple of args must have a trailing comma since it has just one element, else it won't be an actual tuple.
#note from psycopg website: datetime <-- python  gets converted to timestamp or timestamptz
#http://initd.org/psycopg/docs/usage.html#adapt-date
cur.execute("CREATE TABLE mood (id serial PRIMARY KEY, mood integer, datetime timestamp)")


#close communication with database (avoids problems)
cur.close()
conn.close()
