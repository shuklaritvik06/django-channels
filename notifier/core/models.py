from django.db import models
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification = models.TextField()
    is_seen = models.BooleanField(default=False)

    def save(self, *args, **kwargs) -> None:
        channel_layer = get_channel_layer()
        notifs_objs = Notification.objects.filter(is_seen=False)
        data = {"count": notifs_objs.count(), "current": self.notification}
        async_to_sync(channel_layer.group_send)(
            "test_group", {"type": "send_notification", "value": json.dumps(data)}
        )
        super(Notification, self).save(*args, **kwargs)
