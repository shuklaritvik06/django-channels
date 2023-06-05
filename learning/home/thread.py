import threading
from typing import Any
from channels.layers import get_channel_layer
import json
from asgiref.sync import async_to_sync
import time


class CreateData(threading.Thread):
    total = 0

    def __init__(self, count):
        self.total = count
        threading.Thread.__init__(self)

    def run(self):
        try:
            channel_layer = get_channel_layer()
            for i in range(1, 100):
                data = {"count": i}
                async_to_sync(channel_layer.group_send)(
                    "test_group_json",
                    {"type": "send_notification", "value": json.dumps(data)},
                )
                time.sleept(2)
        except Exception as e:
            print(e)
