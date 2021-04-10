from django.db import models
from .user import User
class Chat(models.Model):
    msgfrom =models.CharField(max_length=50)
    msgto =models.CharField(max_length=50)
    msgfromusertype=models.CharField(max_length=50)
    msgtusertype=models.CharField(max_length=50)
    msgtime=models.CharField(max_length=50)
    msg=models.CharField(max_length=500)
    @staticmethod
    def get_all_chat():
        return Chat.objects.all()
    @staticmethod
    def get_all_chat_by_vendor_id(vendor_id):
        return Chat.objects.filter(msgto=vendor_id)

from rest_framework import serializers

class ChatSerializer(serializers.Serializer):
    msgfrom =models.CharField(max_length=50)
    msgto =models.CharField(max_length=50)
    msgfromusertype=models.CharField(max_length=50)
    msgtusertype=models.CharField(max_length=50)
    msgtime=models.CharField(max_length=50)
    msg=models.CharField(max_length=500)
