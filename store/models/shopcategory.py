from django.db import models

class Shopcategory(models.Model):
    name=models.CharField(max_length=100)
    status=models.IntegerField(default=1)
    def isExists(self):
        if Shopcategory.objects.filter(name=self.name):
            return True
        else:
            return False
    def __str__(self):
        return self.name
    @staticmethod
    def get_all_shopcategory():
        return Shopcategory.objects.all()
    # @staticmethod
    # def get_shopcategory_by_store_id(store_id):
    #     try:
    #         return Shopcategory.objects.filter(Shop_id=store_id)
    #     except:
    #         return False
    # @staticmethod
    # def get_shopcategory_by_category_id(category_id):
    #     try:
    #         return Shopcategory.objects.get(id=category_id)
    #     except:
    #         return False


    
    