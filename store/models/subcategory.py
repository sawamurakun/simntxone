from django.db import models

class Subcategory(models.Model):
    name=models.CharField(max_length=100)
    Cat_id=models.IntegerField()
    store_id=models.IntegerField()
    status=models.IntegerField(default=1)
    def isExists(self):
        if Subcategory.objects.filter(name=self.name):
            return True
        else:
            return False
    def __str__(self):
        return self.name
    @staticmethod
    def get_all_subcategories():
        return Subcategory.objects.all()
    @staticmethod
    def get_sub_categories_by_store_id(store_id):
        try:
            return Subcategory.objects.filter(store_id=store_id)
        except:
            return False
    @staticmethod
    def get_subcategory_by_category_id(cat_id):
        try:
            return Subcategory.objects.filter(Cat_id=cat_id)
        except:
            return False
    @staticmethod
    def get_subcategory_by_subcategory_id(subcat_id):
        try:
            return Subcategory.objects.get(id=subcat_id)
        except:
            return False


    
    