import asyncio
import dbsettings
import websockets

port=8080

#needs a web socket handler for stuffs.
async def ws_handler(websocket, path):
    print("server invoked")
    clientstring = await websocket.recv()
    print(clientstring, "received")
    response = "You sent stuff"
    await websocket.send(response)
    #leave socket open leave to client.  make sure websockets has an auto timeout


if __name__ == "__main__":

    start_server = websockets.serve(ws_handler, dbsettings.host, port)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()