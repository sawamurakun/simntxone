from django.db import models

class Profilepicture(models.Model):
    user_image=models.ImageField(upload_to='uploads/userimages/',default="uploads/store/71doo5dci8L._SL1200__flBZ8kI.jpg")
    user_type=models.CharField(max_length=50)
    user_id=models.IntegerField()
    status=models.IntegerField(default=1)