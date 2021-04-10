from django.db import models


class Store(models.Model):
    store_name=models.CharField(max_length=50)
    #vendor_id=models.IntegerField(default=0)
    store_email=models.EmailField()
    store_image=models.ImageField(upload_to='uploads/store/',default="uploads/store/71doo5dci8L._SL1200__flBZ8kI.jpg")
    store_password=models.CharField(max_length=500)
    store_open_date=models.DateField()
    store_category=models.IntegerField()
    #store_desc=models.CharField(max_length=200,default='')
    store_address=models.CharField(max_length=200,default='')
    store_suit=models.CharField(max_length=200,default='')
    store_city=models.CharField(max_length=200,default='')
    store_state=models.CharField(max_length=200,default='')
    store_phone=models.CharField(max_length=20,default='')
    store_zipcode=models.CharField(max_length=50,default='')
    store_tax=models.DecimalField(max_digits=7,decimal_places=2,default=0)
    store_delivery_fees=models.DecimalField(max_digits=7,decimal_places=2,default=0)
    store_aggrement=models.CharField(max_length=50,default='')
    store_active=models.IntegerField(default=0)
    status=models.IntegerField(default=1)
    def isExists(self):
        if Store.objects.filter(store_email=self.store_email):
            if Store.objects.filter(store_name=self.store_name):
                return True
            return True
        else:
            return False
    def add(self):
        self.save()
    @staticmethod
    def get_store_by_email(email):
        return Store.objects.filter(store_email=email,status=1)
    @staticmethod
    def get_store_by_store_id(store_id):
        try:
            return Store.objects.get(id=store_id)
        except:
            return False
    @staticmethod
    def get_all_active_stores(email):
        try:
            return Store.objects.get(store_email=email)
        except:
            return False
    @staticmethod
    def get_active_stores():
        return Store.objects.filter(store_active=1,status=1)

    @staticmethod
    def get_stores_by_store_id(store_id):
        try:
            return Store.objects.filter(id=store_id)
        except:
            return False
    @staticmethod
    def get_store_by_shopcategory(shopcategory_id):
        try:
            return Store.objects.filter(store_category=shopcategory_id)
        except:
            return False
    # @staticmethod
    # def get_store_by_vendor_id(vendor_id):
    #     try:
    #         #print(username)
    #         return Store.objects.filter(vendor_id=vendor_id)
    #     except:
    #         return False
    @staticmethod
    def get_all_stores():
        return Store.objects.all()
    
    # def isExists(self):
    #     if Store.objects.filter(store_name=self.store_name):
    #         return True
    #     else:
    #         return False
