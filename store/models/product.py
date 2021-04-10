from django.db import models
from .category import Category
class Product(models.Model):
    product_name=models.CharField(max_length=50)
    product_color=models.CharField(max_length=50)
    product_size=models.CharField(max_length=30)
    product_price=models.DecimalField(max_digits=7,decimal_places=2,default=0)
    product_category=models.CharField(max_length=50)#models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    product_descriptions=models.CharField(max_length=200,default='')
    product_image=models.ImageField(upload_to='uploads/products/')
    store_id=models.IntegerField(default=0)
    status=models.IntegerField(default=0)
    def add(self):
        self.save()
    # @staticmethod
    # def get_products_by_id(ids):
    #     return Product.objects.filter(id__in=ids)
    # @staticmethod
    # def get_all_products():
    #     return Product.objects.all()
    @staticmethod
    def get_all_product():
        return Product.objects.all()
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)
    @staticmethod
    def get_all_products_by_store_id(store_id):
        return Product.objects.filter(store_id=store_id)
    @staticmethod
    def get_product_by_product_id(product_id):
        return Product.objects.get(id=product_id)
    @staticmethod
    def get_product_by_category(category_id):
        return Product.objects.filter(product_category=category_id)
    # @staticmethod
    # def get_all_products_by_product_id(product_id):
    #     return Product.objects.filter(id=product_id)



