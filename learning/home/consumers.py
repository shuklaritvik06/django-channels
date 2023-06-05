from channels.generic.websocket import WebsocketConsumer, AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync
import json


class Consumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "test_room"
        self.room_group_name = "test_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({"status": "connected"}))

    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        self.send(json.dumps({"message": data["message"], "success": True}))

    def disconnect(self, *args, **kwargs):
        print("disconnect")


class AsynConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = "test_room_json"
        self.room_group_name = "test_group_json"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        await self.send_json(content={"status": "connected"})

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        await self.send_json(content={"status": "connected", "data": data})

    async def disconnect(self, *args, **kwargs):
        await self.send_json(content={"status": "disconnect"})

    async def send_notification(self, event):
        await self.send_json(content=event["value"])
