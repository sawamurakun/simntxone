from django.db import models

class Productfilter(models.Model):
    filter_name=models.CharField(max_length=100)
    filter_category=models.IntegerField()
    filter_store_id=models.IntegerField()
    status=models.IntegerField()
    def isExists(self):
        if Productfilter.objects.filter(filter_name=self.filter_name):
            return True
        else:
            return False
    @staticmethod
    def get_filter_by_store_id(store_id):
        try:
            return Productfilter.objects.filter(filter_store_id=store_id)
        except:
            return False
    @staticmethod
    def get_filter_by_filter_id(filter_id):
        try:
            return Productfilter.objects.get(id=filter_id)
        except:
            return False