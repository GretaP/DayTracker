import psycopg2
import datetime
import dbsettings
import json


#   collect mood from user by parsing JSON data.
#   Needs variables: parseinput, mood, later date to exist outside of def
def parseinput(clientinput):
  #  if (clientinput=="")
    try:
        parseinput = json.loads(clientinput)
        print(parseinput)
    except:
        print("JSON parseinput error")

    try:
        mood = int(parseinput["mood"])
    except ValueError as err:
        #later, send request over websocket
        print("ValueError on attempt to parse mood input", err)


#adds entry to database with input mood (1-5) and server based auto timestamp [for now]
def insertmood(mood):
    #connect to db (create connection and cursor)
    conn = psycopg2.connect(user=dbsettings.user, host= dbsettings.host, password=dbsettings.password, database=dbsettings.database)
    cur = conn.cursor()
    #adds current mood and date/time to database, commit
    dt = datetime.datetime.now()
    cur.execute("INSERT INTO mood (mood, datetime) VALUES (%s, %s)", (mood, dt))
    conn.commit()
    # close communication with database (avoids problems)
    cur.close()
    conn.close()

#checks if input is an integer between 1 and 5
def checkmood(mood):
    pass

#get mood(S) on a given date time range
def getmoodlog(date):
    pass

#get average mood, possibly on a date time range
def getmoodaverage():
    pass



if __name__ == "__main__":
    #  later: remember to include try block for connection issues

    #testing JSON, will be from client
    clientinput = '{"mood": 4, "date": "2016-11-06 23:00:25.689784"}'
    parseinput = json.loads(clientinput)
    print(parseinput)
    mood = int(parseinput["mood"])
   # datetime = parseinput["date"]
  #  insertmood(mood)