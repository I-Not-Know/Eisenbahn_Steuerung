# Der Webserver, welcher für die Kommunikation verantwotlich ist
# Empfängt die Nummer und gibt die Schalt-reihenfolge wieder zurück
# Jegliche Kommunikation wird durch diese Datei organisiert und verwaltet

# Nutze die Positionsbestimmung, damit

import asyncio
import websockets

ip_webserver = ""

async def position(websocket):
    # Der Server soll alle wichtigen Informationen abfragen
    await websocket.send("start")
    start = await websocket.recv()
    await websocket.send("end")
    end = await websocket.recv()

    return start, end


async def get_position_from_pc():
    async with websockets.serve(position, ip_webserver, 8765):
        await asyncio.Future()
