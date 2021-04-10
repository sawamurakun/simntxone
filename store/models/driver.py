from django.db import models

class Driver(models.Model):
    first_name=models.CharField(max_length=50,default="")
    last_name=models.CharField(max_length=50,default="")
    email=models.EmailField()
    driver_image=models.ImageField(upload_to='uploads/driver/')
    password=models.CharField(max_length=500)
    birthday=models.DateField()#default=datetime.datetime.today)
    gender=models.CharField(max_length=50,default="")
    address1=models.CharField(max_length=200,default="")
    apt=models.CharField(max_length=200,default="")
    city=models.CharField(max_length=100,default="")
    state=models.CharField(max_length=100,default="")
    zipcode=models.CharField(max_length=100,default="")
    phone_number=models.CharField(max_length=100,default="")
    vehical_type=models.CharField(max_length=100,default="")
    social_security=models.CharField(max_length=200,default="")
    license_number=models.CharField(max_length=200,default="")
    islicense=models.CharField(max_length=100,default="")
    account_number=models.CharField(max_length=100,default="")
    routing_number=models.CharField(max_length=100,default="")
    convicted_of_any_felonies=models.CharField(max_length=100,default="")
    concede_to_a_background_check=models.CharField(max_length=100,default="")
    status=models.IntegerField(default=1)
    @staticmethod
    def get_driver_by_email(email):
        return Driver.objects.filter(email=email,status=1)
    @staticmethod
    def get_driver_by_driver_id(driver_id):
        try:
            return Driver.objects.get(id=driver_id)
        except:
            return False
    def isExists(self):
        if Driver.objects.filter(email=self.email):
            return True
        else:
            return False

    