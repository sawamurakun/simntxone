from django.db import models


class Advertising(models.Model):
    advertising_image=models.ImageField(upload_to='uploads/advertising/')
    advertising_start_date=models.DateField()
    advertising_end_date=models.DateField()
    advertising_message=models.CharField(max_length=200)
    store_id=models.IntegerField(default=1)
    status=models.IntegerField(default=1)
    @staticmethod
    def get_all_advertising_by(store_id):
        try:
            return Advertising.objects.filter(store_id=store_id)
        except:
            return False
    @staticmethod
    def get_by_advertisement_id(advertisement_id):
        try:
            return Advertising.objects.get(id=advertisement_id)
        except:
            return False
    @staticmethod
    def get_all_advertisement():
        return Advertising.objects.all()

    def add(self):
        self.save()