from django.db import models

class Productattribute(models.Model):
    product_id=models.IntegerField()
    filter_names=models.CharField(max_length=500)
    filter_values=models.CharField(max_length=500)
    status=models.IntegerField(default=1)   
    @staticmethod
    def get_filter_by_product_id(product_id):
        try:
            return Productattribute.objects.get(product_id=product_id)
        except:
            return False