import psycopg2
import datetime
import dbsettings
import json


#   collect mood from user by parsing JSON data.
#   Needs variables: parseinput, mood, later date to exist outside of def
def JSONhandler(clientinput):
  #  if (clientinput=="")

    parseinput=''
    mood = ''
    try:
        parseinput = json.loads(clientinput)
        print(parseinput)
    except Exception as err:
        #yay we made it cleaner by putting text directly into the function/method call, and returned the jsonstring value directly by return method(stuffs) =D
        return errhandle(err, "JSON parseinput error")

#old way: switching to errhandle:
        #print("JSON parseinput error", err)
        #future: create a logfile to report the error, and send data to it <-- easier than database for now
        #create JSON string
        #return JSON string

    try:
        mood = int(parseinput["mood"])
        print(mood)
    #create new exception for out of range
    except ValueError as err:
        #later, send request over websocket
        print("ValueError on attempt to parse mood input", err)
    except TypeError as err:
        print("Type error:", err)

    #insertmood(mood)

class errorobject:
    errorvalue = ""
    def toJSON(selfself):


def errhandle(err, text):
    print(text, "error message:", err)
    #err.message = to log file
    #text --> JSON
    errorsend = errorobject()
    errorsend.errorvalue = text

    #need to create serializer
    print(json.JSONEncoder().encode(errorsend))
    #send JSON to client (return JSON string)

#checks if input is an integer between 1 and 5
#def checkmood(mood):
#    pass




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


#get mood(S) on a given date time range
def getmoodlog(date1, date2):
    pass

#get average mood, possibly on a date time range
def getmoodaverage():
    pass



if __name__ == "__main__":
    #  later: remember to include try block for connection issues

    #testing JSON, will be from client
  #  clientinput = '{"mood": 4, "date": "2016-11-06 23:00:25.689784"}'
    clientinput ="whreeeeeee"
    returndata = JSONhandler(clientinput)
   # parseinput = json.loads(clientinput)
  #  print(parseinput)
  #  mood = int(parseinput["mood"])
   # datetime = parseinput["date"]
  #  insertmood(mood)