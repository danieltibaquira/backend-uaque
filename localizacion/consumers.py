import json
#from channels.generic.websocket import WebsocketConsumer
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from random import choice
class LocConsumer(AsyncWebsocketConsumer):
    async def websocket_connect(self, event):
        self.connect = True
        await self.accept()
        await self.send(text_data=json.dumps({
            "type": "websocket.accept",
            "message": 'OK'
            }))
        
        asyncio.create_task(self.send_data()) 

    async def websocket_disconnect(self, event):
        print("disconnected", event)
        self.connect = False

    async def websocket_receive(self, event):
        print("receive", event)


    async def send_data(self): 
        lugares:list = ['biblioteca', 'parque', 'aulas', 'cafeteria']
        while self.connect:
          await asyncio.sleep(10)
          obj = choice(lugares)
          print({
            'type': 'websocket.send',
            'message':  obj,
            })
          await self.send(text_data=json.dumps({
                'type': 'websocket.send',
                'message': obj,
            }))
