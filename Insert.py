import psycopg2
import datetime
import dbsettings
import json

#later: try block for connection issues

#collect mood from user


#adds entry to database with input mood (1-5) and auto timestamp
def insertmood(mood):
    conn = psycopg2.connect(user=dbsettings.user, host= dbsettings.host, password=dbsettings.password, database=dbsettings.database)
#    conn = psycopg2.connect("dbname=mood user=postgres")
    cur = conn.cursor()
    #adds time variable (temporary - eventually will have client add this
    dt = datetime.datetime.now()
    #adds current mood and date/time to database
    cur.execute("INSERT INTO mood (mood, datetime) VALUES (%s, %s)", (mood, dt))
    conn.commit()
    # close communication with database (avoids problems)
    cur.close()
    conn.close()

#checks if input is an integer between 1 and 5
def checkmood(mood):
 #   try int(mood)
    pass


def getmood(date):
    pass

def getmoodaverage():
    pass



if __name__ == "__main__":
    #will include calls
    #  include try block for connection issues

    #testing JSON, will be from client
    clientinput = '{"mood": 4, "date": "2016-11-06 23:00:25.689784"}'
    parseinput = json.loads(clientinput)
    print(parseinput)
    mood = int(parseinput["mood"])
   # datetime = parseinput["date"]
    insertmood(mood)