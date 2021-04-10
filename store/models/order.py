from django.db import models
from .product import Product
from .user import User



class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    stripe_charge_id=models.CharField(max_length=200)
    address=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    date=models.DateField()
    orderpickup=models.BooleanField(default=False)
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
    @staticmethod
    def get_order_by_order_id(order_id):
        return Order.objects.get(id=order_id)
    @staticmethod
    def get_order_pickup():
        return Order.objects.filter(orderpickup=True)
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


    
    