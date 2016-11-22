import asyncio
import dbsettings
import websockets
import Insert

port=8080


async def ws_handler(websocket, path):
    #open connection w/client, get data from them, and send back that data
    print("client connected")
    clientstring = await websocket.recv()
    print(clientstring, "received")

    #parse the JSON string received... temporary version, and insert mood to database
    mood = Insert.TempJSONparser(clientstring)
    Insert.insertmood(mood)

    #later: message will reflect status of program, be in JSON format, etc
    response = "The server has received your message" #returned JSON data from parser
    await websocket.send(response)
    #leave socket open leave to client.  make sure websockets has an auto timeout



if __name__ == "__main__":

    start_server = websockets.serve(ws_handler, dbsettings.host, port)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()