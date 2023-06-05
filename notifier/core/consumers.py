from channels.generic.websocket import WebsocketConsumer
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

    def send_notification(self, event):
        value = event.get("value")
        self.send(text_data=value)
