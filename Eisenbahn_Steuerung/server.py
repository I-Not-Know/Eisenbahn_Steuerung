# Der Webserver, welcher für die Kommunikation verantwotlich ist
# Empfängt die Nummer und gibt die Schalt-reihenfolge wieder zurück
# Jegliche Kommunikation wird durch diese Datei organisiert und verwaltet

# Nutze die Positionsbestimmung, damit die Weiche passend gestellt werden können
import asyncio
import websockets

ip_webserver = "localhost"

async def call_server_pos(websocket):
    # Der Server soll alle wichtigen Informationen abfragen
    await websocket.send("start")
    global start 
    global end 
    start = await websocket.recv()
    await websocket.send("end")
    end = await websocket.recv()

async def call_server_switch(websocket, switching_order):
    await websocket.send(switching_order)

async def call_server_1():
    async with websockets.serve(call_server_pos, ip_webserver, 8765):
        await asyncio.Future()

async def call_server_2(switching_order):
        async with websockets.serve(call_server_switch, ip_webserver, 8765, switching_order):
            await asyncio.Future()

def get_position_from_controller():
    call_server_1()

def send_switching_order(switching_order):
    call_server_2(switching_order)
    