from django.db import models

class Coupon(models.Model):
    coupon_code=models.CharField(max_length=50,default="")
    coupon_discount=models.DecimalField(max_digits=7,decimal_places=2,default=0)
    coupon_store_id=models.IntegerField()
    coupon_status=models.IntegerField(default=1)
    def isExists(self):
        if Coupon.objects.filter(coupon_code=self.coupon_code):
            return True
        else:
            return False
    @staticmethod
    def get_coupon_by_store_id(store_id):
        try:
            return Coupon.objects.filter(coupon_store_id=store_id)
        except:
            return False
    @staticmethod
    def getCouponbyCoupon_id(coupon_id):
        try:
            return Coupon.objects.get(id=coupon_id)
        except:
            return False
    @staticmethod
    def get_coupon_by_coupon_code(coupon_code):
        try:
            return Coupon.objects.get(coupon_code=coupon_code)
        except:
            return False

    