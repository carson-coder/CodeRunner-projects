import websockets
import asyncio
from colorama import Fore, Back, Style
import os
async def de_bug(websocket, message,type):
    # debugging function
    colortags = {
        "blue": "#0000FF",
        "red": "#FF0000",
        "green": "#00FF00",
        "yellow": "#FFFF00",
        "black": "#000000",
    }
    if type == "WARNING":
        output = "<color=#ffff00><<WARNING>></color>" + message
        await websocket.send(output)
        print(Fore.YELLOW + "<<WARNING>>" + message)
    elif type == "ERROR":
        output = "<color=#ff0000><<ERROR>></color>" + message
        await websocket.send(output)
        print(Fore.RED + "<<ERROR>>" + message)
    elif type == "INFO":
        output = "<color=#00ff00><<INFO>></color>" + message
        await websocket.send(output)
        print   (Fore.GREEN + "<<INFO>>" + message)
    elif type == "DEBUG":
        output = "<color=#0000ff><<DEBUG>></color>" + message
        await websocket.send(output)
        print(Fore.BLUE + "<<DEBUG>>" + message)
    else:
        await websocket.send(message)
async def de_bug(message,type):
    # debugging function
    colortags = {
        "blue": "#0000FF",
        "red": "#FF0000",
        "green": "#00FF00",
        "yellow": "#FFFF00",
        "black": "#000000",
    }
    if type == "WARNING":
        
        print(Fore.YELLOW + "<<WARNING>> " + message)
    elif type == "ERROR":
        
        print(Fore.RED + "<<ERROR>> " + message)
    elif type == "INFO":
        
        print   (Fore.GREEN + "<<INFO>> " + message)
    elif type == "DEBUG":
        
        print(Fore.BLUE + "<<DEBUG>> " + message)
    else:
        print(message)
        
async def debug(websocket, path):
    # connect the user to the debug socket
    await websocket.accept()
    # wait for a message from the server and send it to the debugging function
    while True:
        message = await websocket.recv()
        await de_bug(websocket, message, "DEBUG")
        