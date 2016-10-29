#database creation file
import psycopg2

conn = psycopg2.connect("dbname=mood user=postgres")
cur = conn.cursor()

cur.execute("CREATE TABLE mood (id serial PRIMARY KEY, mood integer, datetime timestamp)")



#commit changes, close communication with database (avoids problems)
conn.commit()
cur.close()
conn.close()
