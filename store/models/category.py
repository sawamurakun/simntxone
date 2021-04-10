from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=100)
    Shop_id=models.IntegerField()
    status=models.IntegerField(default=1)
    def isExists(self):
        if Category.objects.filter(name=self.name):
            return True
        else:
            return False
    def __str__(self):
        return self.name
    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    @staticmethod
    def get_category_by_store_id(store_id):
        try:
            return Category.objects.filter(Shop_id=store_id)
        except:
            return False
    @staticmethod
    def get_category_by_category_id(category_id):
        try:
            return Category.objects.get(id=category_id)
        except:
            return False


    
    