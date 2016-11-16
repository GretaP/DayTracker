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

#no longer!
class errorobject:
    errorvalue = ""
    def toJSON(selfself):


#temporarily: JSON parser is in another file.
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

#was in main:
#    clientinput ="whreeeeeee"
#    returndata = JSONhandler(clientinput)