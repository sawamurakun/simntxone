from django.db import models
from .product import Product
from .user import User
from .order import Order
from .driver import Driver



class Driverorderpickup(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    driver=models.ForeignKey(Driver,on_delete=models.CASCADE)
    pickup=models.BooleanField(default=False)
    status=models.BooleanField(default=False)
    def placeOrder(self):
        self.save()
    @staticmethod
    def get_orders_by_user(userid):
        return Order\
            .objects\
            .filter(user=userid).order_by('-date')
    @staticmethod
    def get_all_order():
        return Order.objects.all()
    # def isExists(self):
    #     if Category.objects.filter(name=self.name):
    #         return True
    #     else:
    #         return False
    # def __str__(self):
    #     return self.name
    # @staticmethod
    # def get_all_categories():
    #     return Category.objects.all()
    # @staticmethod
    # def get_category_by_store_id(store_id):
    #     try:
    #         return Category.objects.filter(Shop_id=store_id)
    #     except:
    #         return False
    # @staticmethod
    # def get_category_by_category_id(category_id):
    #     try:
    #         return Category.objects.get(id=category_id)
    #     except:
    #         return False


    
    