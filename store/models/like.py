from django.db import models
from .product import Product
from .user import User


class Like(models.Model):
    product=models.IntegerField()
    user=models.IntegerField()
    like=models.BooleanField(default=False)
    status=models.BooleanField(default=False)
    @staticmethod
    def get_like_by_user_id_product_id(userac_id,product_id):
        try:
            return Like.objects.get(user=userac_id,product=product_id)
        except:
            return False