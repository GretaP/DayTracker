import psycopg2
import datetime
import dbsettings
import json


#adds entry to database with input mood (1-5) and server based auto timestamp [for now]
def insertmood(mood):
    #connect to db (create connection and cursor)
    conn = psycopg2.connect(user=dbsettings.user, host= dbsettings.host, password=dbsettings.password, database=dbsettings.database)
    cur = conn.cursor()
    #adds current mood and date/time to database, commit
    dt = datetime.datetime.now()
    cur.execute("INSERT INTO mood (mood, datetime) VALUES (%s, %s)", (mood, dt))
    conn.commit()
    print("Mood inserted")
    # close communication with database (avoids problems)
    cur.close()
    conn.close()

#simplified JSON handler, assumes correct data
def TempJSONparser(clientinput):
    parseinput = json.loads(clientinput)
    print("parsed input:", parseinput)
    mood = int(parseinput["mood"])
    print("Mood as an int:", mood)
    print("end TempJSONparser")
    return mood

#get mood(S) on a given date time range
def getmoodlog(date1, date2):
    pass

#get average mood, possibly on a date time range
def getmoodaverage():
    pass

    # simplified JSON handler, assumes correct data
def TempJSONparser(clientinput):
    parseinput = json.loads(clientinput)
    print("parsed input:", parseinput)
    mood = int(parseinput["mood"])
    print("Mood as an int:", mood)
    print("end TempJSONparser")
    return mood

#if __name__ == "__main__":
    #  later: remember to include try block for connection issues

#TESTING PURPOSES WITH CONNECT
   # mood = TempJSONparser('{"mood": 4, "date": "2016-11-06 23:00:25.689784"}')
    #insertmood(mood)

    #testing JSON, will be from client
  #  clientinput = '{"mood": 4, "date": "2016-11-06 23:00:25.689784"}'

  #  parseinput = json.loads(clientinput)
  #  print(parseinput)
  #  mood = int(parseinput["mood"])
   # datetime = parseinput["date"]
  #  insertmood(mood)