from django.db import models

class Notification(models.Model):
    notification=models.CharField(max_length=500)
    notification_to=models.IntegerField()
    notification_from_type=models.CharField(max_length=100)
    notification_time=models.CharField(max_length=100)
    status=models.IntegerField(default=1)
    @staticmethod
    def get_notification_by_store_id(store_id):
        return Notification.objects.filter(notification_to=store_id).filter(notification_from_type='user')
