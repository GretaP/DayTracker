import asyncio
import websockets

host='localhost'
port=80

def ws_handler():



start_server = websockets.serve(>ws_handler, host, port)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()